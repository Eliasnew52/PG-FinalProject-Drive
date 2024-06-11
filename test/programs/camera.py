import glm
import pygame as PG
from programs.SoundEngine import AudioEngine

FieldOfView = 50
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSIVITY = 0.25
class Camera:
    def __init__(self,app, position =(0,0,4), pitch = 0 , yaw = 90 ):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.yaw = yaw
        self.pitch = pitch

        #Camera Movement Parameters
        self.up = glm.vec3(0,1,0)
        self.right = glm.vec3(1,0,0)
        self.forward = glm.vec3(0,0,-1)

        #Matriz de Vista
        self.view_matrix = self.get_view_matrix()

        #Matriz de Proyeccion
        self.projection_matrix = self.get_projection_matrix()


    def Rotate(self):
        rel_x, rel_y = PG.mouse.get_rel()
        self.yaw += rel_x * SENSIVITY
        self.pitch -= rel_y * SENSIVITY
        self. pitch = max(-89,min(89,self.pitch))
    
    def Update_Camera_Vect(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z =glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward,glm.vec3(0,1,0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))


    
    def Update(self):
        self.Movement()
        self.Rotate()
        self.Update_Camera_Vect()
        self.view_matrix = self.get_view_matrix()

    def Movement(self):
        velocity = SPEED * self.app.delta_time
        keys = PG.key.get_pressed()
        
        # Forward and Back Buttons
        # KEY W PRESSED
        if keys[PG.K_w]:
            self.position += self.forward * velocity
        # KEY S PRESSED
        if keys[PG.K_s]:
            self.position -= self.forward * velocity

        #Right and Left Buttons
        # KEY D PRESSED
        if keys[PG.K_d]:
            self.position += self.right * velocity
        # KEY A PRESSED
        if keys[PG.K_a]:
            self.position -= self.right * velocity
        
        # Up and Down Buttons
        # KEY Q PRESSED
        if keys[PG.K_q]:
            self.position += self.up * velocity
        # KEY E PRESSED
        if keys[PG.K_e]:
            self.position -= self.up * velocity
        
        if keys[PG.K_SPACE]:
            AudioEngine.Pause_GA()

        if keys[PG.K_BACKSPACE]:
            AudioEngine.Resume_GA()
    

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

        #Este Modo de Camara se asemeja a la Camara Lock In de los Juegos
        #return glm.lookAt(self.position, glm.vec3(0), self.up)
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FieldOfView), self.aspect_ratio, NEAR, FAR)

