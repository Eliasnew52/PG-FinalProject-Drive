import numpy as np
import moderngl as mgl
import pywavefront


class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['cat'] = CatVBO(ctx)
        self.vbos['skybox'] = SkyBoxVBO(ctx)
        self.vbos['advanced_skybox'] = AdvancedSkyBoxVBO(ctx)
        self.vbos['city1'] = City1VBO(ctx)
        self.vbos['city2'] = City2VBO(ctx)
        self.vbos['city3'] = City3VBO(ctx)
        self.vbos['car1'] = Car1VBO(ctx)
        self.vbos['car2'] = Car2VBO(ctx)
        self.vbos['car3'] = Car3VBO(ctx)
        self.vbos['car4'] = Car4VBO(ctx)
        self.vbos['car5'] = Car5VBO(ctx)
        self.vbos['car6'] = Car6VBO(ctx)
        self.vbos['city4_1'] = City4_1VBO(ctx)
        self.vbos['city4_2'] = City4_2VBO(ctx)
        self.vbos['city4_3'] = City4_3VBO(ctx)
        self.vbos['city4_4'] = City4_4VBO(ctx)
        self.vbos['city4_5'] = City4_5VBO(ctx)
        self.vbos['city4_6'] = City4_6VBO(ctx)
        self.vbos['city4_7'] = City4_7VBO(ctx)
        self.vbos['city4_8'] = City4_8VBO(ctx)
        self.vbos['city4_9'] = City4_9VBO(ctx)
        self.vbos['city4_10'] = City4_10VBO(ctx)
        self.vbos['city4_11'] = City4_11VBO(ctx)
        self.vbos['city4_12'] = City4_12VBO(ctx)
        self.vbos['city4_13'] = City4_13VBO(ctx)
        self.vbos['city4_14'] = City4_14VBO(ctx)
        self.vbos['city4_15'] = City4_15VBO(ctx)
        self.vbos['city4_16'] = City4_16VBO(ctx)
        self.vbos['city4_17'] = City4_17VBO(ctx)
        self.vbos['city4_18'] = City4_18VBO(ctx)
        self.vbos['city4_19'] = City4_19VBO(ctx)
        self.vbos['city4_20'] = City4_20VBO(ctx)
        self.vbos['city4_21'] = City4_21VBO(ctx)
        self.vbos['city4_22'] = City4_22VBO(ctx)
        self.vbos['city4_23'] = City4_23VBO(ctx)
        self.vbos['city4_24'] = City4_24VBO(ctx)
        self.vbos['city4_25'] = City4_25VBO(ctx)
        self.vbos['city4_26'] = City4_26VBO(ctx)
        self.vbos['city4_27'] = City4_27VBO(ctx)
        self.vbos['city4_28'] = City4_28VBO(ctx)
        self.vbos['city4_29'] = City4_29VBO(ctx)
        self.vbos['city4_30'] = City4_30VBO(ctx)
        self.vbos['city4_31'] = City4_31VBO(ctx)
        self.vbos['city4_32'] = City4_32VBO(ctx)
        self.vbos['city4_33'] = City4_33VBO(ctx)
        self.vbos['city4_34'] = City4_34VBO(ctx)
        self.vbos['city4_35'] = City4_35VBO(ctx)
        self.vbos['city4_36'] = City4_36VBO(ctx)
        self.vbos['city4_37'] = City4_37VBO(ctx)
        self.vbos['city4_38'] = City4_38VBO(ctx)
        self.vbos['city4_39'] = City4_39VBO(ctx)
        self.vbos['city4_40'] = City4_40VBO(ctx)
        self.vbos['city4_40'] = City4_40VBO(ctx)
        self.vbos['city4_41'] = City4_41VBO(ctx)
        self.vbos['city4_42'] = City4_42VBO(ctx)
        self.vbos['city4_43'] = City4_43VBO(ctx)
        self.vbos['city4_44'] = City4_44VBO(ctx)
        self.vbos['city4_45'] = City4_45VBO(ctx)
        self.vbos['city4_46'] = City4_46VBO(ctx)
        self.vbos['city4_47'] = City4_47VBO(ctx)
        self.vbos['city4_48'] = City4_48VBO(ctx)
        self.vbos['city4_49'] = City4_49VBO(ctx)
        self.vbos['city4_50'] = City4_50VBO(ctx)
        self.vbos['city4_51'] = City4_51VBO(ctx)
        self.vbos['city4_52'] = City4_52VBO(ctx)
        self.vbos['city4_53'] = City4_53VBO(ctx)
        self.vbos['city4_54'] = City4_54VBO(ctx)
        self.vbos['city4_55'] = City4_55VBO(ctx)
        self.vbos['city4_56'] = City4_56VBO(ctx)
        self.vbos['city4_57'] = City4_57VBO(ctx)
        self.vbos['city4_58'] = City4_58VBO(ctx)
        self.vbos['city4_59'] = City4_59VBO(ctx)
        self.vbos['city4_60'] = City4_60VBO(ctx)
        self.vbos['city4_61'] = City4_61VBO(ctx)
        self.vbos['city4_62'] = City4_62VBO(ctx)
        self.vbos['city4_63'] = City4_63VBO(ctx)
        self.vbos['city4_64'] = City4_64VBO(ctx)
        self.vbos['city4_65'] = City4_65VBO(ctx)
        self.vbos['city4_66'] = City4_66VBO(ctx)
        self.vbos['city4_67'] = City4_67VBO(ctx)
        self.vbos['city4_68'] = City4_68VBO(ctx)
        self.vbos['city4_69'] = City4_69VBO(ctx)
        self.vbos['city4_70'] = City4_70VBO(ctx)
        self.vbos['city4_71'] = City4_71VBO(ctx)
        self.vbos['city4_72'] = City4_72VBO(ctx)
        self.vbos['city4_73'] = City4_73VBO(ctx)
        self.vbos['city4_74'] = City4_74VBO(ctx)
        self.vbos['city4_75'] = City4_75VBO(ctx)
        self.vbos['city4_76'] = City4_76VBO(ctx)
        self.vbos['city4_77'] = City4_77VBO(ctx)
        self.vbos['city4_78'] = City4_78VBO(ctx)
        self.vbos['city4_79'] = City4_79VBO(ctx)
        self.vbos['city4_80'] = City4_80VBO(ctx)
        self.vbos['city4_81'] = City4_81VBO(ctx)
        self.vbos['city4_82'] = City4_82VBO(ctx)
        self.vbos['city4_83'] = City4_83VBO(ctx)
        self.vbos['city4_84'] = City4_84VBO(ctx)
        self.vbos['city4_85'] = City4_85VBO(ctx)
        self.vbos['city4_86'] = City4_86VBO(ctx)
        self.vbos['city4_87'] = City4_87VBO(ctx)
        self.vbos['city4_88'] = City4_88VBO(ctx)
        self.vbos['city4_89'] = City4_89VBO(ctx)
        self.vbos['city4_90'] = City4_90VBO(ctx)
        self.vbos['city4_91'] = City4_91VBO(ctx)
        self.vbos['city4_92'] = City4_92VBO(ctx)
        self.vbos['city4_93'] = City4_93VBO(ctx)
        self.vbos['city4_94'] = City4_94VBO(ctx)
        self.vbos['city4_95'] = City4_95VBO(ctx)
        self.vbos['city4_96'] = City4_96VBO(ctx)
        self.vbos['city4_97'] = City4_97VBO(ctx)
        self.vbos['city4_98'] = City4_98VBO(ctx)
        self.vbos['city4_99'] = City4_99VBO(ctx)
        self.vbos['city4_100'] = City4_100VBO(ctx)
        self.vbos['city4_101'] = City4_101VBO(ctx)
        self.vbos['city4_102'] = City4_102VBO(ctx)
        self.vbos['city4_103'] = City4_103VBO(ctx)
        self.vbos['city4_104'] = City4_104VBO(ctx)
        self.vbos['city4_105'] = City4_105VBO(ctx)
        self.vbos['city4_106'] = City4_106VBO(ctx)
        self.vbos['city4_107'] = City4_107VBO(ctx)
        self.vbos['city4_108'] = City4_108VBO(ctx)
        self.vbos['city4_109'] = City4_109VBO(ctx)
        self.vbos['city4_110'] = City4_110VBO(ctx)
        self.vbos['city4_111'] = City4_111VBO(ctx)
        self.vbos['city4_112'] = City4_112VBO(ctx)
        self.vbos['city4_113'] = City4_113VBO(ctx)
        self.vbos['city4_114'] = City4_114VBO(ctx)
        self.vbos['city4_115'] = City4_115VBO(ctx)
        self.vbos['city4_116'] = City4_116VBO(ctx)
        self.vbos['city4_117'] = City4_117VBO(ctx)
        self.vbos['city4_118'] = City4_118VBO(ctx)
        self.vbos['city4_119'] = City4_119VBO(ctx)
        self.vbos['city4_120'] = City4_120VBO(ctx)
        self.vbos['city4_121'] = City4_121VBO(ctx)
        self.vbos['city4_122'] = City4_122VBO(ctx)
        self.vbos['city4_123'] = City4_123VBO(ctx)
        self.vbos['city4_124'] = City4_124VBO(ctx)
        self.vbos['city4_125'] = City4_125VBO(ctx)
        self.vbos['city4_126'] = City4_126VBO(ctx)
        self.vbos['city4_127'] = City4_127VBO(ctx)
        self.vbos['city4_128'] = City4_128VBO(ctx)
        self.vbos['city4_129'] = City4_129VBO(ctx)
        self.vbos['city4_130'] = City4_130VBO(ctx)
        self.vbos['city4_131'] = City4_131VBO(ctx)
        self.vbos['city4_132'] = City4_132VBO(ctx)
        self.vbos['city4_133'] = City4_133VBO(ctx)
        self.vbos['city4_134'] = City4_134VBO(ctx)
        self.vbos['city4_135'] = City4_135VBO(ctx)
        self.vbos['city4_136'] = City4_136VBO(ctx)
        self.vbos['city4_137'] = City4_137VBO(ctx)
        self.vbos['city4_138'] = City4_138VBO(ctx)
        self.vbos['city4_139'] = City4_139VBO(ctx)
        self.vbos['city4_140'] = City4_140VBO(ctx)
        self.vbos['city4_141'] = City4_141VBO(ctx)
        self.vbos['city4_142'] = City4_142VBO(ctx)
        self.vbos['city4_143'] = City4_143VBO(ctx)
        self.vbos['city4_144'] = City4_144VBO(ctx)
        self.vbos['city4_145'] = City4_145VBO(ctx)
        self.vbos['city4_146'] = City4_146VBO(ctx)
        self.vbos['city4_147'] = City4_147VBO(ctx)
        self.vbos['city4_148'] = City4_148VBO(ctx)
        self.vbos['city4_149'] = City4_149VBO(ctx)
        self.vbos['city4_150'] = City4_150VBO(ctx)
        self.vbos['city4_151'] = City4_151VBO(ctx)
        self.vbos['city4_152'] = City4_152VBO(ctx)
        self.vbos['city4_153'] = City4_153VBO(ctx)
        self.vbos['city4_154'] = City4_154VBO(ctx)
        self.vbos['city4_155'] = City4_155VBO(ctx)
        self.vbos['city4_156'] = City4_156VBO(ctx)
        self.vbos['city4_157'] = City4_157VBO(ctx)
        self.vbos['city4_158'] = City4_158VBO(ctx)
        self.vbos['city4_159'] = City4_159VBO(ctx)
        self.vbos['city4_160'] = City4_160VBO(ctx)
        self.vbos['city4_161'] = City4_161VBO(ctx)
        self.vbos['city4_162'] = City4_162VBO(ctx)
        self.vbos['city4_163'] = City4_163VBO(ctx)
        self.vbos['city4_164'] = City4_164VBO(ctx)
        self.vbos['city4_165'] = City4_165VBO(ctx)
        self.vbos['city4_166'] = City4_166VBO(ctx)
        self.vbos['city4_167'] = City4_167VBO(ctx)
        self.vbos['city4_168'] = City4_168VBO(ctx)


    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1),]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data


class CatVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):       
        try:
        # Load the OBJ file with caching and parsing enabled
            objs = pywavefront.Wavefront('objects/cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        
        # Check if there are any materials loaded
            if not objs.materials:
                raise ValueError("No materials found in the OBJ file.")
        
        # Extract a material from the loaded OBJ
            material = objs.materials.popitem()[1]
        
        # Check if the material has vertex data
            if not hasattr(material, 'vertices'):
                raise ValueError("No vertex data found in the material.")
        
        # Get the vertex data from the material
            vertex_data = material.vertices
        
        # Convert the vertex data to a NumPy array of type float32
            vertex_data = np.array(vertex_data, dtype='f4')
        
            return vertex_data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class City1VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city1/scene.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class City2VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city2/gta_city.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class City3VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city3/gta_city2.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Car1VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car/nissan_370_red1.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Car2VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car/nissan_370_red2.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Car3VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car/nissan_370_red3.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Car4VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car/nissan_370_red4.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Car5VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car/nissan_370_red5.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Car6VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/car/nissan_370_red6.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class SkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f'
        self.attribs = ['in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)
        vertex_data = np.flip(vertex_data, 1).copy(order='C')
        return vertex_data


class AdvancedSkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f'
        self.attribs = ['in_position']

    def get_vertex_data(self):
        # in clip space
        z = 0.9999
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        vertex_data = np.array(vertices, dtype='f4')
        return vertex_data

class City4_1VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/city_base.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_2VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/city_hospital.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_3VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_4VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca1.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_5VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca2.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_6VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca3.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_7VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca4.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_8VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca5.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_9VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca6.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_10VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca7.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
    
class City4_11VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca8.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_12VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca9.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_13VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca10.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_14VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca11.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_15VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca12.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_16VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca13.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_17VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca14.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_18VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca15.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_19VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca16.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_20VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca17.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_21VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca18.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_22VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca19.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_23VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca20.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_24VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca21.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data
    
class City4_25VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca22.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_26VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca23.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_27VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca24.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_28VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca25.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_29VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca26.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_30VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca27.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_31VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca28.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_32VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca29.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_33VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca30.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_34VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca31.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_35VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca32.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_36VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca33.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_37VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca34.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_38VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca35.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_39VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca36.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_40VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca37.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data
    
class City4_41VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca38.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_42VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca39.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_43VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca40.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_44VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca41.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_45VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca42.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_46VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca43.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_47VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca44.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_48VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca45.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_49VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca46.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_50VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/city4/source/city_factory_cerca/city_factory_cerca47.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_51VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_52VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_53VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_54VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_55VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_56VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio6.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_57VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio7.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_58VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio8.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_59VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio9.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_60VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio10.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_61VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio11.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_62VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio12.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_63VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio13.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_64VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio14.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_65VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio15.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_66VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio16.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_67VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio17.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_68VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio18.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_69VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio19.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_70VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio20.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_71VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio21.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_72VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio22.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_73VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio23.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_74VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio24.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_75VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio25.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_76VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio26.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_77VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio27.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_78VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio28.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_79VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio29.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_80VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio30.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_81VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio31.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_82VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio32.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_83VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_cancha_edificio/city_cancha_edificio.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_84VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/city_cancha.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_85VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lavanderia/city_lavanderia1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_86VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lavanderia/city_lavanderia2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_87VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lavanderia/city_lavanderia3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_88VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lavanderia/city_lavanderia4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_89VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_90VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_91VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_92VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_93VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_94VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas6.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_95VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas7.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_96VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_97VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_98VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_99VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_100VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_101VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm6.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_102VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm7.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_103VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm8.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_104VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm9.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_105VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm10.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data
    

class City4_106VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_107VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas_piso.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_108VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_109VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_110VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_111VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor6.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_112VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor7.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_113VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor8.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_114VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor9.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_115VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_liquor/city_liquor10.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_116VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_117VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_118VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_119VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_120VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_121VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount6.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_122VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount7.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_123VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount8.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_124VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount9.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_125VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount10.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_126VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount11.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_127VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount12.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_128VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount13.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_129VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_paramount/city_paramount14.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data


class City4_130VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_arm/city_edificio_arm_piso.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_131VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_tienda_armas/city_tienda_armas_piso2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_132VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_133VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_134VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_135VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_136VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_137VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw6.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_138VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw7.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_139VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw8.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_140VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw9.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_141VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw10.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_142VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw11.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_143VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw12.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_144VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw13.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_145VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_pauw/city_edificio_pauw14.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_146VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_chino/city_edificio_chino1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_147VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_chino/city_edificio_chino2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_148VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_chino/city_edificio_chino3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_149VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_chino/city_edificio_chino4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_150VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_chino/city_edificio_chino5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_151VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_152VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_153VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_154VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_155VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo5.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_156VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo6.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_157VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo7.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_158VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo8.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_159VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo9.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_160VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo10.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_161VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo11.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_162VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo12.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_163VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo13.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_164VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_edificio_gemelo/city_edificio_gemelo14.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_165VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lamppost/city_lamppost1.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_166VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lamppost/city_lamppost2.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_167VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lamppost/city_lamppost3.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data

class City4_168VBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        obj_path = 'objects/city4/source/city_lamppost/city_lamppost4.obj'
        objs = pywavefront.Wavefront(obj_path, cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = np.array(obj.vertices, dtype='f4')
        return vertex_data








