import glm

class Light:
    def __init__(self,position=(3,3,3)):
        color =(1,1,1)
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)

        #intensities
        self.Ambient = 0.1 * self.color #Ambient Light
        self.Diffuse = 0.8 * self.color #Diffuse Light
        self.Specular = 1.0 * self.color #Specular Light

    def Color_Change(self, new_color):
        self.color = glm.vec3(new_color)
        self.ambient = 0.1 * self.color
        self.diffuse = 0.8 * self.color
        self.specular = 1.0 * self.color