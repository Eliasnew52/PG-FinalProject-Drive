import numpy as np
import glm
import pygame as PG

class Triangle:
    def __init__(self,app):
        self.app = app
        self.context = app.context
        self.VBO = self.get_VBO()
        self.ShaderProgram = self.get_shader_program('default')
        self.VAO = self.get_VAO()

    def render(self):
        self.VAO.render()
    
    def destroy(self):
        self.VBO.release()
        self.ShaderProgram.release()
        self.VAO.release()

    
    def get_VAO(self):
        vao = self.context.vertex_array(self.ShaderProgram,[(self.VBO, '3f', 'in_position')])
        return vao

    def get_vertex_data(self):
        vertex_data =[(-0.6,-0.8,0.0),(0.6,-0.8,0.0),(0.0,0.8,0.0)]
        vertex_data = np.array(vertex_data,dtype='f4')
        return vertex_data
    
    def get_VBO(self):
        vertex_data = self.get_vertex_data()
        VBO = self.context.buffer(vertex_data)
        return VBO
    
    def get_shader_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        
        program = self.context.program(vertex_shader = vertex_shader, fragment_shader = fragment_shader)
        
        return program


## 3D CUBE MODEL RENDERING
class Cube:
    def __init__(self,app):
        self.app = app
        self.context = app.context
        self.VBO = self.get_VBO()
        self.ShaderProgram = self.get_shader_program('default')
        self.VAO = self.get_VAO()
        self.model_matrix = self.get_model_matrix()
        self.texture = self.get_texture(path='textures/ryan_gosling.jpeg')
        self.on_init()


    def get_texture(self, path):
        texture = PG.image.load(path).convert()
        texture = PG.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.context.texture(size = texture.get_size(), components =3, data=PG.image.tostring(texture,'RGB'))
        return texture

    def update(self):
        matrix_model = glm.rotate(self.model_matrix, self.app.time, glm.vec3(0,1,0))
        self.ShaderProgram['model_matrix'].write(matrix_model)
        self.ShaderProgram['view_matrix'].write(self.app.camera.view_matrix)
    

    def get_model_matrix(self):
        matrix_model = glm.mat4()
        return matrix_model
    
    def on_init(self):
        #Textures
        self.ShaderProgram['u_texture_0'] =0
        self.texture.use()

        #Matrix
        self.ShaderProgram['projection_matrix'].write(self.app.camera.projection_matrix)
        self.ShaderProgram['view_matrix'].write(self.app.camera.view_matrix)
        self.ShaderProgram['model_matrix'].write(self.model_matrix)

    def render(self):
        self.update()
        self.VAO.render()
    
    def destroy(self):
        self.VBO.release()
        self.ShaderProgram.release()
        self.VAO.release()

    
    def get_VAO(self):
        vao = self.context.vertex_array(self.ShaderProgram,[(self.VBO, '2f 3f', 'in_texcoord_0','in_position')])
        return vao

    def get_vertex_data(self):
        vertices = [(-1, -1, 1),(1, -1, 1),(1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1),(-1,-1,-1),(1,-1,-1), (1,1,-1)]
        

        indices =[(0,2,3), (0,1,2),
                  (1,7,2), (1,6,7),
                  (6,5,4), (4,7,6),
                  (3,4,5), (3,5,0),
                  (3,7,4), (3,2,7),
                  (0,6,1), (0,5,6)]
        
        vertex_data = self.get_data(vertices,indices)

        texture_coords = [(0,0),(1,0),(1,1),(0,1)]

        texture_coords_indices = [(0,2,3),(0,1,2),
                                  (0,2,3),(0,1,2),
                                  (0,1,2),(2,3,0),
                                  (2,3,0),(2,0,1),
                                  (0,2,3),(0,1,2),
                                  (3,1,2),(3,0,1)]
        texture_coords_data = self.get_data(texture_coords,texture_coords_indices)

        vertex_data = np.hstack([texture_coords_data,vertex_data])
        return vertex_data
    
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind]for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')
    
    def get_VBO(self):
        vertex_data = self.get_vertex_data()
        VBO = self.context.buffer(vertex_data)
        return VBO
    
    def get_shader_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        
        program = self.context.program(vertex_shader = vertex_shader, fragment_shader = fragment_shader)
        
        return program