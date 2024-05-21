import numpy as np

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


class Cube:
    def __init__(self,app):
        self.app = app
        self.context = app.context
        self.VBO = self.get_VBO()
        self.ShaderProgram = self.get_shader_program('default')
        self.VAO = self.get_VAO()
        self.on_init()
    
    def on_init(self):
        self.ShaderProgram['projection_matrix'].write(self.app.camera.projection_matrix)
        self.ShaderProgram['view_matrix'].write(self.app.camera.view_matrix)

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
        vertices = [(-1, -1, 1),(1, -1, 1),(1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1),(-1,-1,-1),(1,-1,-1), (1,1,-1)]
        

        indices =[(0,2,3), (0,1,2),
                  (1,7,2), (1,6,7),
                  (6,5,4), (4,7,6),
                  (3,4,5), (3,5,0),
                  (3,7,4), (3,2,7),
                  (0,6,1), (0,5,6)]
        
        vertex_data = self.get_data(vertices,indices)
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