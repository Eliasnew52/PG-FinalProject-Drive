import pygame as PG
import moderngl as mgl
import numpy
import sys

class GraphicsEngine:
    def __init__(self, win_size = (720,400)):
        #inicializamos el modulo de PyGame
        PG.init()
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

        #Detectamos y Creamos el Contexto de OpenGL
        self.context= mgl.create_context()

        #Creacion de un Objeto para medir el Tiempo
        self.clock = PG.time.Clock()


    def Check_Events(self):
        for event in PG.event.get():
            if event == PG.QUIT or (event.type == PG.KEYDOWN and event.type == PG.K_ESCAPE):
                PG.quit()
                sys.exit()

    def Render(self):
        #Limpiar el FrameBuffer
        self.context.clear(color=(0.08,0.16,0.18))
        PG.display.flip()

    def Run(self):
        while True:
            self.Check_Events()
            self.Render()
            self.clock.tick(60)


if __name__ =='__main__':
    app = GraphicsEngine()
    app.Run()



