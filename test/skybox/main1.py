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
        size = 500  # Tamaño del skybox
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

    def move(self, direction):
        new_position = self.position + self.speed * np.array(direction, dtype=np.float32)
        self.position = np.clip(new_position, self.bounds[0], self.bounds[1])

    def get_view_matrix(self):
        gluLookAt(*self.position, *self.position + [0, 0, -1], 0, 1, 0)


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
        self.camera.get_view_matrix()

        self.skybox.render(self.program)

        pygame.display.flip()


def main():
    pygame.init()
    title = "Skybox Demo"
    target_fps = 60
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
    clock = pygame.time.Clock()

    skybox = Skybox("./images1/")
    camera = Camera([0, 0, 0], 0.1, [[-450, -450, -450], [450, 450, 450]])  # Límites de la cámara
    renderer = Renderer(width, height, title, skybox, camera)

    moving = [False, False, False, False]
    keys = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                for i, key in enumerate(keys):
                    if event.key == key:
                        moving[i] = event.type == pygame.KEYDOWN

        if moving[0]:
            camera.move([0, 0, -1])
        if moving[1]:
            camera.move([0, 0, 1])
        if moving[2]:
            camera.move([-1, 0, 0])
        if moving[3]:
            camera.move([1, 0, 0])

        renderer.render()
        clock.tick(target_fps)
        fps = clock.get_fps()
        pygame.display.set_caption(f"{title}, FPS: {fps:.0f}")

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()