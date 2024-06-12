import pygame
import sys
import time
import glob
import numpy as np
from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *

def load_shaders(vert_url, frag_url):
    """Carga y compila shaders desde archivos."""
    with open(vert_url, 'r') as vert_file, open(frag_url, 'r') as frag_file:
        vert_str = vert_file.read()
        frag_str = frag_file.read()

    vert_shader = shaders.compileShader(vert_str, GL_VERTEX_SHADER)
    frag_shader = shaders.compileShader(frag_str, GL_FRAGMENT_SHADER)
    program = shaders.compileProgram(vert_shader, frag_shader)
    return program

def load_cubemap(folder_url):
    """Carga una textura de cubemap desde una carpeta."""
    tex_id = glGenTextures(1)
    face_order = ["right", "left", "top", "bottom", "back", "front"]
    face_urls = sorted(glob.glob(folder_url + "*"))

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_CUBE_MAP, tex_id)

    for i, face in enumerate(face_order):
        face_url = [face_url for face_url in face_urls if face in face_url.lower()][0]
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

def render(width, height, program, cubemap, camera_pos):
    """Renderiza la escena."""
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_TEXTURE_CUBE_MAP)

    skybox_right = [1, -1, -1, 1, -1,  1, 1,  1,  1, 1,  1,  1, 1,  1, -1, 1, -1, -1]
    skybox_left = [-1, -1,  1, -1, -1, -1, -1,  1, -1, -1,  1, -1, -1,  1,  1, -1, -1,  1]
    skybox_top = [-1,  1, -1, 1,  1, -1, 1,  1,  1, 1,  1,  1, -1,  1,  1, -1,  1, -1]
    skybox_bottom = [-1, -1, -1, -1, -1,  1, 1, -1, -1, 1, -1, -1, -1, -1,  1, 1, -1,  1]
    skybox_back = [-1,  1, -1, -1, -1, -1, 1, -1, -1, 1, -1, -1, 1,  1, -1, -1,  1, -1]
    skybox_front = [-1, -1,  1, -1,  1,  1, 1,  1,  1, 1,  1,  1, 1, -1,  1, -1, -1,  1]

    skybox_vertices = np.array([skybox_right, skybox_left, skybox_top, skybox_bottom, skybox_back, skybox_front], dtype=np.float32).flatten()
    skybox_vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, skybox_vbo)
    glBufferData(GL_ARRAY_BUFFER, skybox_vertices.nbytes, skybox_vertices, GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, 0)

    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, float(width) / height, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*camera_pos, *camera_pos + [0, 0, -1], 0, 1, 0)

    glUseProgram(program)
    glDepthMask(GL_FALSE)
    glBindTexture(GL_TEXTURE_CUBE_MAP, cubemap)
    glEnableClientState(GL_VERTEX_ARRAY)
    glBindBuffer(GL_ARRAY_BUFFER, skybox_vbo)
    glVertexPointer(3, GL_FLOAT, 0, None)
    glDrawArrays(GL_TRIANGLES, 0, 36)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glDisableClientState(GL_VERTEX_ARRAY)
    glBindTexture(GL_TEXTURE_CUBE_MAP, 0)
    glDepthMask(GL_TRUE)
    glUseProgram(0)

    pygame.display.flip()

def main():
    """Función principal."""
    title = "Skybox Demo"
    target_fps = 60
    width, height = 800, 600
    flags = pygame.DOUBLEBUF | pygame.OPENGL
    screen = pygame.display.set_mode((width, height), flags)
    prev_time = time.time()
    camera_pos = np.array([0, 0, 0], dtype=np.float32)
    camera_speed = 0.1
    cubemap = load_cubemap("./images1/")
    program = load_shaders("./shaders/skybox.vert", "./shaders/skybox.frag")

    moving = [False, False, False, False]
    keys = [pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                for i, key in enumerate(keys):
                    if event.key == key:
                        moving[i] = event.type == pygame.KEYDOWN

        if moving[0]:
            camera_pos += camera_speed * np.array([0, 0, -1])
        if moving[1]:
            camera_pos -= camera_speed * np.array([0, 0, -1])
        if moving[2]:
            camera_pos -= camera_speed * np.cross([0, 1, 0], [0, 0, -1])
        if moving[3]:
            camera_pos += camera_speed * np.cross([0, 1, 0], [0, 0, -1])

        render(width, height, program, cubemap, camera_pos)

        curr_time = time.time()
        diff = curr_time - prev_time
        delay = max(1.0 / target_fps - diff, 0)
        time.sleep(delay)
        fps = 1.0 / (delay + diff)
        prev_time = curr_time
        pygame.display.set_caption("{0}, FPS: {1:.0f}".format(title, fps))

if __name__ == "__main__":
    pygame.init()
    main()
