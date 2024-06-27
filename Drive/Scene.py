from Model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # cat
        #add(Cat(app, pos=(0, 10, -10)))

        #City
        self.City = City(app, pos=(0, 0, 0), scale=(3, 3, 3), tex_id='city')
        add(self.City)

    def update(self):
        pass
        #self.moving_cube.rot.xyz = self.app.time