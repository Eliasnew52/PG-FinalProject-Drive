import pygame
import sys
import time
import glob
import numpy as np
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *
import glm

# Constantes
FIELD_OF_VIEW = 50
NEAR = 0.1
FAR = 100
SPEED = 0.1
SENSITIVITY = 0.1

class Skybox:
    def __init__(self, folder_url):
        self.cubemap_texture = self.load_cubemap(folder_url)
        self.skybox_vbo = self.create_skybox_vbo()

    def load_cubemap(self, folder_url):
        tex_id = glGenTextures(1)
        face_order = ["right", "left", "top", "bottom", "back", "front"]
        face_urls = sorted(glob.glob(folder_url + "*"))

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)

        for i, face in enumerate(face_order):
            face_url = next((url for url in face_urls if face in url.lower()), None)
            if not face_url:
                raise FileNotFoundError(f"No image found for {face}")
            face_image = pygame.image.load(face_url).convert()
            face_width, face_height = face_image.get_size()
            face_surface = pygame.image.tostring(face_image, 'RGB')
            glTexImage2D(GL_TEXTURE_CUBE_MAP_POSITIVE_X + i, 0, GL_RGB, face_width, face_height, 0, GL_RGB, GL_UNSIGNED_BYTE, face_surface)

        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_CUBE_MAP, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
        glBindTexture(GL_TEXTURE_CUBE_MAP, 0)
        return tex_id

    def create_skybox_vbo(self):
        size = 100 # Tamaño del skybox
        skybox_faces = [
            [size, -size, -size, size, -size,  size, size,  size,  size, size,  size,  size, size,  size, -size, size, -size, -size],  # right
            [-size, -size,  size, -size, -size, -size, -size,  size, -size, -size,  size, -size, -size,  size,  size, -size, -size,  size],  # left
            [-size,  size, -size, size,  size, -size, size,  size,  size, size,  size,  size, -size,  size,  size, -size,  size, -size],  # top
            [-size, -size, -size, -size, -size,  size, size, -size, -size, size, -size, -size, -size, -size,  size, size, -size,  size],  # bottom
            [-size,  size, -size, -size, -size, -size, size, -size, -size, size, -size, -size, size,  size, -size, -size,  size, -size],  # back
            [-size, -size,  size, -size,  size,  size, size,  size,  size, size,  size,  size, size, -size,  size, -size, -size,  size],  # front
        ]

        skybox_vertices = np.array(skybox_faces, dtype=np.float32).flatten()
        skybox_vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, skybox_vbo)
        glBufferData(GL_ARRAY_BUFFER, skybox_vertices.nbytes, skybox_vertices, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        return skybox_vbo

    def render(self, program):
        glUseProgram(program)
        glDepthMask(GL_FALSE)
        glBindTexture(GL_TEXTURE_CUBE_MAP, self.cubemap_texture)
        glEnableClientState(GL_VERTEX_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, self.skybox_vbo)
        glVertexPointer(3, GL_FLOAT, 0, None)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glDisableClientState(GL_VERTEX_ARRAY)
        glBindTexture(GL_TEXTURE_CUBE_MAP, 0)
        glDepthMask(GL_TRUE)
        glUseProgram(0)

class Camera:
    def __init__(self, app):
        self.app = app
        self.aspect_ratio = app.width / app.height
        self.position = glm.vec3(0, 0, 3)
        self.up = glm.vec3(0, 1, 0)
        self.front = glm.vec3(0, 0, -1)
        self.right = glm.vec3(1, 0, 0)
        self.yaw = -90.0
        self.pitch = 0.0

        self.view_matrix = self.get_view_matrix()
        self.projection_matrix = self.get_projection_matrix()

    def update(self):
        self.handle_input()
        self.view_matrix = self.get_view_matrix()

    def handle_input(self):
        velocity = SPEED * self.app.delta_time
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.position += self.front * velocity
        if keys[pygame.K_s]:
            self.position -= self.front * velocity
        if keys[pygame.K_a]:
            self.position -= self.right * velocity
        if keys[pygame.K_d]:
            self.position += self.right * velocity
        if keys[pygame.K_q]:
            self.position += self.up * velocity
        if keys[pygame.K_e]:
            self.position -= self.up * velocity

        mouse_movement = pygame.mouse.get_rel()
        self.process_mouse_movement(mouse_movement[0], mouse_movement[1])

    def process_mouse_movement(self, xoffset, yoffset):
        xoffset *= SENSITIVITY
        yoffset *= SENSITIVITY

        self.yaw += xoffset
        self.pitch -= yoffset

        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        direction = glm.vec3()
        direction.x = np.cos(glm.radians(self.yaw)) * np.cos(glm.radians(self.pitch))
        direction.y = np.sin(glm.radians(self.pitch))
        direction.z = np.sin(glm.radians(self.yaw)) * np.cos(glm.radians(self.pitch))
        self.front = glm.normalize(direction)
        self.right = glm.normalize(glm.cross(self.front, self.up))

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.front, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FIELD_OF_VIEW), self.aspect_ratio, NEAR, FAR)

class Renderer:
    def __init__(self, width, height, title, skybox, camera):
        self.width = width
        self.height = height
        self.title = title
        self.skybox = skybox
        self.camera = camera
        self.program = self.load_shaders("./shaders/skybox.vert", "./shaders/skybox.frag")
        self.init_opengl()

    def load_shaders(self, vert_url, frag_url):
        with open(vert_url, 'r') as vert_file, open(frag_url, 'r') as frag_file:
            vert_str = vert_file.read()
            frag_str = frag_file.read()

        vert_shader = shaders.compileShader(vert_str, GL_VERTEX_SHADER)
        frag_shader = shaders.compileShader(frag_str, GL_FRAGMENT_SHADER)
        program = shaders.compileProgram(vert_shader, frag_shader)
        return program

    def init_opengl(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_TEXTURE_CUBE_MAP)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, float(self.width) / self.height, 0.1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        view = glm.mat4_cast(self.camera.get_view_matrix())
        glMultMatrixf(glm.value_ptr(view))

        self.skybox.render(self.program)
        pygame.display.flip()

class App:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win_size = (width, height)
        pygame.init()
        self.screen = pygame.display.set_mode(self.win_size, pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("Skybox Example")
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.last_time = time.time()
        self.skybox = Skybox("./images4/")
        self.camera = Camera(self)
        self.renderer = Renderer(width, height, "Skybox Example", self.skybox, self.camera)
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            current_time = time.time()
            self.delta_time = current_time - self.last_time
            self.last_time = current_time

            self.camera.update()
            self.renderer.render()
            self.clock.tick(60)

if __name__ == "__main__":
    app = App(800, 600)
    app.run()
