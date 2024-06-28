from VBO import VBO
from ShaderProgram import ShaderProgram


#VERTEX OBJECT ARRAY
class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # cat vao
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['cat'])
        
    
        # city1 vao
        self.vaos['city1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city1'])

        # shadow city1 vao
        self.vaos['shadow_city1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city1'])
        
        # city2 vao
        self.vaos['city2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city2'])

        # shadow city2 vao
        self.vaos['shadow_city2'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city2'])
        
        # city3 vao
        self.vaos['city3'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city3'])

        # shadow city3 vao
        self.vaos['shadow_city3'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city3'])


        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()