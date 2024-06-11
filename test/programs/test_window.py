import pygame as PG
import moderngl as mgl
import numpy
import sys

from programs.models import *
from programs.camera import Camera
from programs.RayCast import RayCast_Camera
from programs.SoundEngine import AudioEngine
from programs.LightEngine import Light

class GraphicsEngine:
    def __init__(self, win_size = (1920, 1080)):
        #inicializamos el modulo de PyGame
       
        PG.init()
        
        #Music
        PG.mixer.init()

        #Definimos un tamaño de Pantalla
        self.WIN_SIZE = win_size
        #Configuracion de Atributos de OpenGL
        PG.display.gl_set_attribute(PG.GL_CONTEXT_MAJOR_VERSION,3)
        PG.display.gl_set_attribute(PG.GL_CONTEXT_MINOR_VERSION,3)
        PG.display.gl_set_attribute(PG.GL_CONTEXT_PROFILE_MASK, PG.GL_CONTEXT_PROFILE_CORE)

        #Creacion del Contexto de OpenGL (Buffers)
        PG.display.set_mode(self.WIN_SIZE, flags=PG.OPENGL | PG.DOUBLEBUF)
        #Trabajaremos con Dos Buffers para Dibujar, Uno se Muestra, mientras que el otro Dibuja
        #Una vez se termine de dibujar, los Buffers se cambia de lugar para mostrar el Dibujo y se repite

        #Configuracion del Mouse
        PG.event.set_grab(True)
        PG.mouse.set_visible(True)

        #Detectamos y Creamos el Contexto de OpenGL
        self.context= mgl.create_context()
        #self.context.front_face='cw'
        self.context.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)

        #Creacion del Objeto Camera
        self.camera = RayCast_Camera(self)

        #Creacion de un Objeto para medir el Tiempo
        self.clock = PG.time.Clock()
        self.time = 0
        self.delta_time = 0

        #Light

        self.Light = Light()
        #Scene
        self.scene = Cube(self)
        self.AudioEng = AudioEngine

      

    def Check_Events(self):
        for event in PG.event.get():
            if event == PG.QUIT or (event.type == PG.KEYDOWN and event.key == PG.K_ESCAPE):
                self.scene.destroy()
                PG.quit()
                sys.exit()

    def Render(self):
        #Limpiar el FrameBuffer
        self.context.clear(color=(0.08,0.16,0.18))
        self.scene.render()
        PG.display.flip()
    
    def get_time(self):
        self.time = PG.time.get_ticks() * 0.001

    def Run(self):
        self.AudioEng.Global_Audio("Nightcall")
        while True:
            self.get_time()
            self.Check_Events()
            self.camera.Update()
            self.Render()
            self.delta_time = self.clock.tick(60)


if __name__ =='__main__':
    app = GraphicsEngine()
    app.Run()



