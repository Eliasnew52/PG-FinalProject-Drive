import glm

class Light:
    def __init__(self,position=(3,3,3), color =(1,1,1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)

        #intensities
        self.Ambient = 0.1 * self.color #Ambient Light
        self.Diffuse = 0.8 * self.color #Diffuse Light
        self.Specular = 1.0 * self.color #Specular Light
