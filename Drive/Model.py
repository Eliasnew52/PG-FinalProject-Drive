import moderngl as mgl
import numpy as np
import glm
import pygame as pg



class BaseModel:
    def _init_(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()


class ExtendedBaseModel(BaseModel):
    def _init_(self, app, vao_name, tex_id, pos, rot, scale):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    def on_init(self):
        self.program['m_view_light'].write(self.app.light.m_view_light)
        # resolution
        self.program['u_resolution'].write(glm.vec2(self.app.WIN_SIZE))
        # depth texture
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        # shadow
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


class Cube(ExtendedBaseModel):
    def _init_(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class MovingCube(Cube):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

    def update(self):
        self.m_model = self.get_model_matrix()
        super().update()

class Cat(ExtendedBaseModel):
    def _init_(self, app, vao_name='cat', tex_id='cat',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City1(ExtendedBaseModel):
    def _init_(self, app, vao_name='city1', tex_id='city1',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(50, 50, 50)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        
class City2(ExtendedBaseModel):
    def _init_(self, app, vao_name='city2', tex_id='city2',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1000, 1000, 1000)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        
class City3(ExtendedBaseModel):
    def _init_(self, app, vao_name='city3', tex_id='city3',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1000, 1000, 1000)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class Car1(ExtendedBaseModel):
    def _init_(self, app, vao_name='car1', tex_id='car1',
                 pos=(0, 0, 0), rot=(0, 180, 0), scale=(5,5,5)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class MovingCar1(Car1):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)


    def update(self):
        
        


        self.m_model = self.get_model_matrix()
        super().update()
        
class Car2(ExtendedBaseModel):
    def _init_(self, app, vao_name='car2', tex_id='car2',
                 pos=(0, 0, 0), rot=(0, 180, 0), scale=(5, 5, 5)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        
class MovingCar2(Car2):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)


    def update(self):
       


        self.m_model = self.get_model_matrix()
        super().update()
        
class Car3(ExtendedBaseModel):
    def _init_(self, app, vao_name='car3', tex_id='car3',
                 pos=(0, 0, 0), rot=(0, 180, 0), scale=(5, 5, 5)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        
class MovingCar3(Car3):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)


    def update(self):
        
    
        self.m_model = self.get_model_matrix()
        super().update()
        
class Car4(ExtendedBaseModel):
    def _init_(self, app, vao_name='car4', tex_id='car4',
                 pos=(0, 0, 0), rot=(0, 180, 0), scale=(5, 5, 5)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        
class MovingCar4(Car4):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)


    def update(self):

        self.m_model = self.get_model_matrix()
        super().update()
        
class Car5(ExtendedBaseModel):
    def _init_(self, app, vao_name='car5', tex_id='car5',
                 pos=(0, 0, 0), rot=(0, 180, 0), scale=(5, 5, 5)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class MovingCar5(Car5):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)


    def update(self):

        self.m_model = self.get_model_matrix()
        super().update()

class Car6(ExtendedBaseModel):
    def _init_(self, app, vao_name='car6', tex_id='car6',
                 pos=(0, 0, 0), rot=(0, 180, 0), scale=(5, 5, 5)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class MovingCar6(Car6):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)


    def update(self):
       

        self.m_model = self.get_model_matrix()
        super().update()

class City4_1(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_1', tex_id='city4_1',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_2(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_2', tex_id='city4_2',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_3(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_3', tex_id='city4_3',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_4(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_4', tex_id='city4_4',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_5(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_5', tex_id='city4_5',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_6(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_6', tex_id='city4_6',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_7(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_7', tex_id='city4_7',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_8(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_8', tex_id='city4_8',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_9(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_9', tex_id='city4_9',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_10(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_10', tex_id='city4_10',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_11(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_11', tex_id='city4_11',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_12(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_12', tex_id='city4_12',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_13(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_13', tex_id='city4_13',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_14(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_14', tex_id='city4_14',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_15(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_15', tex_id='city4_15',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_16(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_16', tex_id='city4_16',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_17(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_17', tex_id='city4_17',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_18(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_18', tex_id='city4_18',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_19(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_19', tex_id='city4_19',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_20(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_20', tex_id='city4_20',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_21(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_21', tex_id='city4_21',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_22(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_22', tex_id='city4_22',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_23(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_23', tex_id='city4_23',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_24(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_24', tex_id='city4_24',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_25(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_25', tex_id='city4_25',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_26(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_26', tex_id='city4_26',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_27(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_27', tex_id='city4_27',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_28(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_28', tex_id='city4_28',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_29(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_29', tex_id='city4_29',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_30(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_30', tex_id='city4_30',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_31(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_31', tex_id='city4_31',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_32(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_32', tex_id='city4_32',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_33(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_33', tex_id='city4_33',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_34(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_34', tex_id='city4_34',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_35(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_35', tex_id='city4_35',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_36(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_36', tex_id='city4_36',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_37(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_37', tex_id='city4_37',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_38(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_38', tex_id='city4_38',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_39(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_39', tex_id='city4_39',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_40(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_40', tex_id='city4_40',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
    
class City4_41(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_41', tex_id='city4_41',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_42(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_42', tex_id='city4_42',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_43(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_43', tex_id='city4_43',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_44(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_44', tex_id='city4_44',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_45(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_45', tex_id='city4_45',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_46(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_46', tex_id='city4_46',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_47(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_47', tex_id='city4_47',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_48(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_48', tex_id='city4_48',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_49(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_49', tex_id='city4_49',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_50(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_50', tex_id='city4_50',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_51(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_51', tex_id='city4_51',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_52(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_52', tex_id='city4_52',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_53(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_53', tex_id='city4_53',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_54(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_54', tex_id='city4_54',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_55(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_55', tex_id='city4_55',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_56(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_56', tex_id='city4_56',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_57(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_57', tex_id='city4_57',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_58(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_58', tex_id='city4_58',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_59(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_59', tex_id='city4_59',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_60(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_60', tex_id='city4_60',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_61(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_61', tex_id='city4_61',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_62(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_62', tex_id='city4_62',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_63(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_63', tex_id='city4_63',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_64(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_64', tex_id='city4_64',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_65(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_65', tex_id='city4_65',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_66(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_66', tex_id='city4_66',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_67(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_67', tex_id='city4_67',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_68(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_68', tex_id='city4_68',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_69(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_69', tex_id='city4_69',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_70(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_70', tex_id='city4_70',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_71(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_71', tex_id='city4_71',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_72(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_72', tex_id='city4_72',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_73(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_73', tex_id='city4_73',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_74(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_74', tex_id='city4_74',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_75(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_75', tex_id='city4_75',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_76(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_76', tex_id='city4_76',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_77(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_77', tex_id='city4_77',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_78(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_78', tex_id='city4_78',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_79(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_79', tex_id='city4_79',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_80(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_80', tex_id='city4_80',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_81(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_81', tex_id='city4_81',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_82(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_82', tex_id='city4_82',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_83(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_83', tex_id='city4_83',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_84(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_84', tex_id='city4_84',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_85(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_85', tex_id='city4_85',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_86(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_86', tex_id='city4_86',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_87(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_87', tex_id='city4_87',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_88(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_88', tex_id='city4_88',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_89(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_89', tex_id='city4_89',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_90(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_90', tex_id='city4_90',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_91(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_91', tex_id='city4_91',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_92(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_92', tex_id='city4_92',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_93(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_93', tex_id='city4_93',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_94(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_94', tex_id='city4_94',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_95(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_95', tex_id='city4_95',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_96(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_96', tex_id='city4_96',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_97(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_97', tex_id='city4_97',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_98(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_98', tex_id='city4_98',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_99(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_99', tex_id='city4_99',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_100(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_100', tex_id='city4_100',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_101(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_101', tex_id='city4_101',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_102(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_102', tex_id='city4_102',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_103(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_103', tex_id='city4_103',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_104(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_104', tex_id='city4_104',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_105(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_105', tex_id='city4_105',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_106(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_106', tex_id='city4_106',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_107(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_107', tex_id='city4_107',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_108(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_108', tex_id='city4_108',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_109(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_109', tex_id='city4_109',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_110(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_110', tex_id='city4_110',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_111(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_111', tex_id='city4_111',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_112(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_112', tex_id='city4_112',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_113(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_113', tex_id='city4_113',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_114(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_114', tex_id='city4_114',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_115(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_115', tex_id='city4_115',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_116(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_116', tex_id='city4_116',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_117(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_117', tex_id='city4_117',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_118(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_118', tex_id='city4_118',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_119(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_119', tex_id='city4_119',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_120(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_120', tex_id='city4_120',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_121(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_121', tex_id='city4_121',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_122(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_122', tex_id='city4_122',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_123(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_123', tex_id='city4_123',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_124(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_124', tex_id='city4_124',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_125(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_125', tex_id='city4_125',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_126(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_126', tex_id='city4_126',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_127(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_127', tex_id='city4_127',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_128(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_128', tex_id='city4_128',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_129(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_129', tex_id='city4_129',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_130(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_130', tex_id='city4_130',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_131(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_131', tex_id='city4_131',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)


class City4_132(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_132', tex_id='city4_132',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_133(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_133', tex_id='city4_133',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_134(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_134', tex_id='city4_134',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_135(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_135', tex_id='city4_135',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_136(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_136', tex_id='city4_136',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_137(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_137', tex_id='city4_137',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_138(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_138', tex_id='city4_138',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_139(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_139', tex_id='city4_139',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_140(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_140', tex_id='city4_140',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_141(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_141', tex_id='city4_141',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_142(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_142', tex_id='city4_142',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_143(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_143', tex_id='city4_143',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_144(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_144', tex_id='city4_144',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_145(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_145', tex_id='city4_145',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_146(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_146', tex_id='city4_146',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_147(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_147', tex_id='city4_147',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_148(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_148', tex_id='city4_148',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_149(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_149', tex_id='city4_149',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_150(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_150', tex_id='city4_150',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_151(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_151', tex_id='city4_151',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_152(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_152', tex_id='city4_152',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_153(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_153', tex_id='city4_153',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_154(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_154', tex_id='city4_154',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_155(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_155', tex_id='city4_155',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_156(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_156', tex_id='city4_156',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_157(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_157', tex_id='city4_157',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_158(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_158', tex_id='city4_158',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_159(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_159', tex_id='city4_159',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_160(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_160', tex_id='city4_160',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_161(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_161', tex_id='city4_161',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_162(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_162', tex_id='city4_162',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_163(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_163', tex_id='city4_163',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_164(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_164', tex_id='city4_164',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_165(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_165', tex_id='city4_165',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_166(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_166', tex_id='city4_166',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_167(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_167', tex_id='city4_167',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class City4_168(ExtendedBaseModel):
    def _init_(self, app, vao_name='city4_168', tex_id='city4_168',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(7, 7, 7)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)

class SkyBox(BaseModel):
    def _init_(self, app, vao_name='skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))


class AdvancedSkyBox(BaseModel):
    def _init_(self, app, vao_name='advanced_skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super()._init_(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        m_view = glm.mat4(glm.mat3(self.camera.m_view))
        self.program['m_invProjView'].write(glm.inverse(self.camera.m_proj * m_view))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)