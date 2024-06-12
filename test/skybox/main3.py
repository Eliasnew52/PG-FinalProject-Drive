import pygame
import sys
import time
import glob
import numpy as np
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *

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
        size = 100  # Tamaño del skybox
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
    def __init__(self, position, speed, bounds):
        self.position = np.array(position, dtype=np.float32)
        self.speed = speed
        self.bounds = bounds
        self.pitch = 0
        self.yaw = -90
        self.sensitivity = 0.1
        self.front = np.array([0, 0, -1], dtype=np.float32)

    def move(self, direction):
        new_position = self.position + self.speed * np.array(direction, dtype=np.float32)
        self.position = np.clip(new_position, self.bounds[0], self.bounds[1])

    def rotate(self, xoffset, yoffset):
        xoffset *= self.sensitivity
        yoffset *= self.sensitivity

        self.yaw += xoffset
        self.pitch += yoffset

        if self.pitch > 89:
            self.pitch = 89
        if self.pitch < -89:
            self.pitch = -89

        front = np.array([
            np.cos(np.radians(self.yaw)) * np.cos(np.radians(self.pitch)),
            np.sin(np.radians(self.pitch)),
            np.sin(np.radians(self.yaw)) * np.cos(np.radians(self.pitch))
        ], dtype=np.float32)
        self.front = front / np.linalg.norm(front)

    def get_view_matrix(self):
        center = self.position + self.front
        gluLookAt(*self.position, *center, 0, 1, 0)

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
        try:
            with open(vert_url, 'r') as vert_file, open(frag_url, 'r') as frag_file:
                vert_str = vert_file.read()
                frag_str = frag_file.read()
            
            vert_shader = shaders.compileShader(vert_str, GL_VERTEX_SHADER)
            frag_shader = shaders.compileShader(frag_str, GL_FRAGMENT_SHADER)
            program = shaders.compileProgram(vert_shader, frag_shader)
            return program
        except (IOError, shaders.ShaderCompilationError, shaders.ShaderProgramError) as e:
            print(f"Error loading shaders: {e}")
            sys.exit()

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
        self.camera.get_view_matrix()

        self.skybox.render(self.program)
        self.render_cube()

        pygame.display.flip()

    def render_cube(self):
        glBegin(GL_QUADS)

        # Front face
        glColor3f(1.0, 0.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)

        # Back face
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)

        # Top face
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)

        # Bottom face
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)

        # Right face
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)

        # Left face
        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)

        glEnd()

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("Skybox with Cube Example")

    skybox = Skybox("./images4/")
    camera = Camera([0, 0, 0], 0.1, [[-50, -50, -50], [50, 50, 50]])
    renderer = Renderer(width, height, "Skybox Example", skybox, camera)

    clock = pygame.time.Clock()
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    last_mouse_pos = pygame.mouse.get_pos()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            camera.move([0, 0, -1])
        if keys[pygame.K_s]:
            camera.move([0, 0, 1])
        if keys[pygame.K_a]:
            camera.move([-1, 0, 0])
        if keys[pygame.K_d]:
            camera.move([1, 0, 0])
        if keys[pygame.K_q]:
            camera.move([0, -1, 0])
        if keys[pygame.K_e]:
            camera.move([0, 1, 0])

        mouse_pos = pygame.mouse.get_pos()
        xoffset = mouse_pos[0] - last_mouse_pos[0]
        yoffset = last_mouse_pos[1] - mouse_pos[1]
        last_mouse_pos = mouse_pos

        camera.rotate(xoffset, yoffset)

        renderer.render()
        clock.tick(60)

if __name__ == "__main__":
    main()