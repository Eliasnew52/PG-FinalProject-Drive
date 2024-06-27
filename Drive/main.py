import pygame as pg
import moderngl as mgl
import sys

from Model import *
from RayCast import RayCast_Camera
from LightEngine import Light
from Mesh import Mesh
from Scene import Scene
from SoundEngine import AudioEngine
from Scene_Renderer import SceneRenderer


class GraphicsEngine:
    def __init__(self, win_size=(1920, 1080)):
        # init pygame modules
        pg.init()

         
        # Music
        pg.mixer.init()

        # Definimos un tamaño de Pantalla
        self.WIN_SIZE = win_size
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = self.WIN_SIZE
        self.HALF_WIDTH = self.SCREEN_WIDTH // 2
        self.HALF_HEIGHT = self.SCREEN_HEIGHT // 2

        # Configuración de Atributos de OpenGL
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        # Configuración del Mouse
        pg.event.set_grab(True)
        pg.mouse.set_visible(True)
        # Inicialmente, establecer el mouse en el centro
        pg.mouse.set_pos((self.HALF_WIDTH, self.HALF_HEIGHT))

        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST)
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = RayCast_Camera(self)
        # mesh
        self.mesh = Mesh(self)
        # scene
        self.scene = Scene(self)

         # renderer
        self.scene_renderer = SceneRenderer(self)

        #Audio Engine
        self.AudioEng = AudioEngine

        # Calcular los límites del mouse dinámicamente
        self.BOUND_LEFT = self.HALF_WIDTH - 100
        self.BOUND_TOP = self.HALF_HEIGHT - 100
        self.BOUND_RIGHT = self.HALF_WIDTH + 100
        self.BOUND_BOTTOM = self.HALF_HEIGHT + 100

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # render scene
        self.scene_renderer.render()
        # swap buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        self.AudioEng.Global_Audio("Nightcall")
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()

            # Limitar el movimiento del Mouse
            mouse_x, mouse_y = pg.mouse.get_pos()
            # Ajustar la posición del mouse a los límites
            clamped_x = max(self.BOUND_LEFT, min(mouse_x, self.BOUND_RIGHT))
            clamped_y = max(self.BOUND_TOP, min(mouse_y, self.BOUND_BOTTOM))
            # Actualizar la posición del mouse si está fuera de los límites
            if (mouse_x, mouse_y) != (clamped_x, clamped_y):
                pg.mouse.set_pos((clamped_x, clamped_y))

            self.delta_time = self.clock.tick(60)


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()






























