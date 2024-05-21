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