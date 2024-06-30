from VBO import VBO
from ShaderProgram import ShaderProgram


#VERTEX OBJECT ARRAY
class VAO:
    def _init_(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # shadow cube vao
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
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

        # car1 vao
        self.vaos['car1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['car1'])

        # shadow car1 vao
        self.vaos['shadow_car1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['car1'])
        
        # car2 vao
        self.vaos['car2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['car2'])

        # shadow car2 vao
        self.vaos['shadow_car2'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['car2'])
        
        # car3 vao
        self.vaos['car3'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['car3'])

        # shadow car3 vao
        self.vaos['shadow_car3'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['car3'])
        
        # car4 vao
        self.vaos['car4'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['car4'])

        # shadow car4 vao
        self.vaos['shadow_car4'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['car4'])
        
        # car5 vao
        self.vaos['car5'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['car5'])

        # shadow car5 vao
        self.vaos['shadow_car5'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['car5'])
        
        # car6 vao
        self.vaos['car6'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['car6'])

        # shadow car6 vao
        self.vaos['shadow_car6'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['car6'])


        # City4_1 vao
        self.vaos['city4_1'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_1'])
        
        # shadow city4_1 vao
        self.vaos['shadow_city4_1'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_1'])

        # City4_2 vao
        self.vaos['city4_2'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_2'])
        
        # shadow city4_2 vao
        self.vaos['shadow_city4_2'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_2'])

        # City4_3 vao
        self.vaos['city4_3'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_3'])
        
        # shadow city4_3 vao
        self.vaos['shadow_city4_3'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_3'])

        # City4_4 vao
        self.vaos['city4_4'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_4'])
        
        # shadow city4_4 vao
        self.vaos['shadow_city4_4'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_4'])

        # City4_5 vao
        self.vaos['city4_5'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_5'])
        
        # shadow city4_5 vao
        self.vaos['shadow_city4_5'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_5'])

        # City4_6 vao
        self.vaos['city4_6'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_6'])
        
        # shadow city4_6 vao
        self.vaos['shadow_city4_6'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_6'])

        # City4_7 vao
        self.vaos['city4_7'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_7'])
        
        # shadow city4_7 vao
        self.vaos['shadow_city4_7'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_7'])

        # City4_8 vao
        self.vaos['city4_8'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_8'])
        
        # shadow city4_8 vao
        self.vaos['shadow_city4_8'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_8'])

        # City4_9 vao
        self.vaos['city4_9'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_9'])
        
        # shadow city4_9 vao
        self.vaos['shadow_city4_9'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_9'])

        # City4_10 vao
        self.vaos['city4_10'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_10'])
        
        # shadow city4_10 vao
        self.vaos['shadow_city4_10'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_10'])
        
        # City4_11 vao
        self.vaos['city4_11'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_11'])

        # shadow city4_11 vao
        self.vaos['shadow_city4_11'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_11'])

        # City4_12 vao
        self.vaos['city4_12'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_12'])

        # shadow city4_12 vao
        self.vaos['shadow_city4_12'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_12'])

        # City4_13 vao
        self.vaos['city4_13'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_13'])

        # shadow city4_13 vao
        self.vaos['shadow_city4_13'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_13'])

        # City4_14 vao
        self.vaos['city4_14'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_14'])

        # shadow city4_14 vao
        self.vaos['shadow_city4_14'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_14'])

        # City4_15 vao
        self.vaos['city4_15'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_15'])

        # shadow city4_15 vao
        self.vaos['shadow_city4_15'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_15'])

        # City4_16 vao
        self.vaos['city4_16'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_16'])

        # shadow city4_16 vao
        self.vaos['shadow_city4_16'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_16'])

        # City4_17 vao
        self.vaos['city4_17'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_17'])

        # shadow city4_17 vao
        self.vaos['shadow_city4_17'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_17'])

        # City4_18 vao
        self.vaos['city4_18'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_18'])

        # shadow city4_18 vao
        self.vaos['shadow_city4_18'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_18'])

        # City4_19 vao
        self.vaos['city4_19'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_19'])

        # shadow city4_19 vao
        self.vaos['shadow_city4_19'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_19'])

        # City4_20 vao
        self.vaos['city4_20'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_20'])

        # shadow city4_20 vao
        self.vaos['shadow_city4_20'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_20'])

        # City4_21 vao
        self.vaos['city4_21'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_21'])

        # shadow city4_21 vao
        self.vaos['shadow_city4_21'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_21'])

        # City4_22 vao
        self.vaos['city4_22'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_22'])

        # shadow city4_22 vao
        self.vaos['shadow_city4_22'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_22'])

        # City4_23 vao
        self.vaos['city4_23'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_23'])

        # shadow city4_23 vao
        self.vaos['shadow_city4_23'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_23'])

        # City4_24 vao
        self.vaos['city4_24'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_24'])

        # shadow city4_24 vao
        self.vaos['shadow_city4_24'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_24'])

        # City4_25 vao
        self.vaos['city4_25'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_25'])

        # shadow city4_25 vao
        self.vaos['shadow_city4_25'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_25'])

        # City4_26 vao
        self.vaos['city4_26'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_26'])

        # shadow city4_26 vao
        self.vaos['shadow_city4_26'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_26'])

        # City4_27 vao
        self.vaos['city4_27'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_27'])

        # shadow city4_27 vao
        self.vaos['shadow_city4_27'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_27'])

        # City4_28 vao
        self.vaos['city4_28'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_28'])

        # shadow city4_28 vao
        self.vaos['shadow_city4_28'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_28'])

        # City4_29 vao
        self.vaos['city4_29'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_29'])

        # shadow city4_29 vao
        self.vaos['shadow_city4_29'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_29'])

        # City4_30 vao
        self.vaos['city4_30'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_30'])

        # shadow city4_30 vao
        self.vaos['shadow_city4_30'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_30'])

        # City4_31 vao
        self.vaos['city4_31'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_31'])

        # shadow city4_31 vao
        self.vaos['shadow_city4_31'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_31'])

        # City4_32 vao
        self.vaos['city4_32'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_32'])

        # shadow city4_32 vao
        self.vaos['shadow_city4_32'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_32'])

        # City4_33 vao
        self.vaos['city4_33'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_33'])

        # shadow city4_33 vao
        self.vaos['shadow_city4_33'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_33'])

        # City4_34 vao
        self.vaos['city4_34'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_34'])

        # shadow city4_34 vao
        self.vaos['shadow_city4_34'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_34'])

        # City4_35 vao
        self.vaos['city4_35'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_35'])

        # shadow city4_35 vao
        self.vaos['shadow_city4_35'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_35'])

        # City4_36 vao
        self.vaos['city4_36'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_36'])

        # shadow city4_36 vao
        self.vaos['shadow_city4_36'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_36'])

        # City4_37 vao
        self.vaos['city4_37'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_37'])

        # shadow city4_37 vao
        self.vaos['shadow_city4_37'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_37'])

        # City4_38 vao
        self.vaos['city4_38'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_38'])

        # shadow city4_38 vao
        self.vaos['shadow_city4_38'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_38'])

        # City4_39 vao
        self.vaos['city4_39'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_39'])

        # shadow city4_39 vao
        self.vaos['shadow_city4_39'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_39'])

        # City4_40 vao
        self.vaos['city4_40'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_40'])

        # shadow city4_40 vao
        self.vaos['shadow_city4_40'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_40'])
        
        # City4_41 vao
        self.vaos['city4_41'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_41'])

        # shadow city4_41 vao
        self.vaos['shadow_city4_41'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_41'])

        # City4_42 vao
        self.vaos['city4_42'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_42'])

        # shadow city4_42 vao
        self.vaos['shadow_city4_42'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_42'])

        # City4_43 vao
        self.vaos['city4_43'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_43'])

        # shadow city4_43 vao
        self.vaos['shadow_city4_43'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_43'])

        # City4_44 vao
        self.vaos['city4_44'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_44'])

        # shadow city4_44 vao
        self.vaos['shadow_city4_44'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_44'])

        # City4_45 vao
        self.vaos['city4_45'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_45'])

        # shadow city4_45 vao
        self.vaos['shadow_city4_45'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_45'])

        # City4_46 vao
        self.vaos['city4_46'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_46'])

        # shadow city4_46 vao
        self.vaos['shadow_city4_46'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_46'])

        # City4_47 vao
        self.vaos['city4_47'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_47'])

        # shadow city4_47 vao
        self.vaos['shadow_city4_47'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_47'])

        # City4_48 vao
        self.vaos['city4_48'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_48'])

        # shadow city4_48 vao
        self.vaos['shadow_city4_48'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_48'])

        # City4_49 vao
        self.vaos['city4_49'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_49'])

        # shadow city4_49 vao
        self.vaos['shadow_city4_49'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_49'])

        # City4_50 vao
        self.vaos['city4_50'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_50'])

        # shadow city4_50 vao
        self.vaos['shadow_city4_50'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_50'])
        
        # City4_51 vao
        self.vaos['city4_51'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_51'])

        # shadow city4_51 vao
        self.vaos['shadow_city4_51'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_51'])

        # City4_52 vao
        self.vaos['city4_52'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_52'])

        # shadow city4_52 vao
        self.vaos['shadow_city4_52'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_52'])

        # City4_53 vao
        self.vaos['city4_53'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_53'])

        # shadow city4_53 vao
        self.vaos['shadow_city4_53'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_53'])

        # City4_54 vao
        self.vaos['city4_54'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_54'])

        # shadow city4_54 vao
        self.vaos['shadow_city4_54'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_54'])

        # City4_55 vao
        self.vaos['city4_55'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_55'])

        # shadow city4_55 vao
        self.vaos['shadow_city4_55'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_55'])

        # City4_56 vao
        self.vaos['city4_56'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_56'])

        # shadow city4_56 vao
        self.vaos['shadow_city4_56'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_56'])

        # City4_57 vao
        self.vaos['city4_57'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_57'])

        # shadow city4_57 vao
        self.vaos['shadow_city4_57'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_57'])

        # City4_58 vao
        self.vaos['city4_58'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_58'])

        # shadow city4_58 vao
        self.vaos['shadow_city4_58'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_58'])

        # City4_59 vao
        self.vaos['city4_59'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_59'])

        # shadow city4_59 vao
        self.vaos['shadow_city4_59'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_59'])

        # City4_60 vao
        self.vaos['city4_60'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_60'])

        # shadow city4_60 vao
        self.vaos['shadow_city4_60'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_60'])

        # City4_61 vao
        self.vaos['city4_61'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_61'])

        # shadow city4_61 vao
        self.vaos['shadow_city4_61'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_61'])

        # City4_62 vao
        self.vaos['city4_62'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_62'])

        # shadow city4_62 vao
        self.vaos['shadow_city4_62'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_62'])

        # City4_63 vao
        self.vaos['city4_63'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_63'])

        # shadow city4_63 vao
        self.vaos['shadow_city4_63'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_63'])

        # City4_64 vao
        self.vaos['city4_64'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_64'])

        # shadow city4_64 vao
        self.vaos['shadow_city4_64'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_64'])

        # City4_65 vao
        self.vaos['city4_65'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_65'])

        # shadow city4_65 vao
        self.vaos['shadow_city4_65'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_65'])

        # City4_66 vao
        self.vaos['city4_66'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_66'])

        # shadow city4_66 vao
        self.vaos['shadow_city4_66'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_66'])

        # City4_67 vao
        self.vaos['city4_67'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_67'])

        # shadow city4_67 vao
        self.vaos['shadow_city4_67'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_67'])

        # City4_68 vao
        self.vaos['city4_68'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_68'])

        # shadow city4_68 vao
        self.vaos['shadow_city4_68'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_68'])

        # City4_69 vao
        self.vaos['city4_69'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_69'])

        # shadow city4_69 vao
        self.vaos['shadow_city4_69'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_69'])

        # City4_70 vao
        self.vaos['city4_70'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_70'])

        # shadow city4_70 vao
        self.vaos['shadow_city4_70'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_70'])

        # City4_71 vao
        self.vaos['city4_71'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_71'])

        # shadow city4_71 vao
        self.vaos['shadow_city4_71'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_71'])

        # City4_72 vao
        self.vaos['city4_72'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_72'])

        # shadow city4_72 vao
        self.vaos['shadow_city4_72'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_72'])

        # City4_73 vao
        self.vaos['city4_73'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_73'])

        # shadow city4_73 vao
        self.vaos['shadow_city4_73'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_73'])

        # City4_74 vao
        self.vaos['city4_74'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_74'])

        # shadow city4_74 vao
        self.vaos['shadow_city4_74'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_74'])

        # City4_75 vao
        self.vaos['city4_75'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_75'])

        # shadow city4_75 vao
        self.vaos['shadow_city4_75'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_75'])

        # City4_76 vao
        self.vaos['city4_76'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_76'])

        # shadow city4_76 vao
        self.vaos['shadow_city4_76'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_76'])

        # City4_77 vao
        self.vaos['city4_77'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_77'])

        # shadow city4_77 vao
        self.vaos['shadow_city4_77'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_77'])

        # City4_78 vao
        self.vaos['city4_78'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_78'])

        # shadow city4_78 vao
        self.vaos['shadow_city4_78'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_78'])

        # City4_79 vao
        self.vaos['city4_79'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_79'])

        # shadow city4_79 vao
        self.vaos['shadow_city4_79'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_79'])

        # City4_80 vao
        self.vaos['city4_80'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_80'])

        # shadow city4_80 vao
        self.vaos['shadow_city4_80'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_80'])

        # City4_81 vao
        self.vaos['city4_81'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_81'])

        # shadow city4_81 vao
        self.vaos['shadow_city4_81'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_81'])

        # City4_82 vao
        self.vaos['city4_82'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_82'])

        # shadow city4_82 vao
        self.vaos['shadow_city4_82'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_82'])

        # City4_83 vao
        self.vaos['city4_83'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_83'])

        # shadow city4_83 vao
        self.vaos['shadow_city4_83'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_83'])

        # City4_84 vao
        self.vaos['city4_84'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_84'])

        # shadow city4_84 vao
        self.vaos['shadow_city4_84'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_84'])
        
                # City4_85 vao
        self.vaos['city4_85'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_85'])

        # shadow city4_85 vao
        self.vaos['shadow_city4_85'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_85'])

        # City4_86 vao
        self.vaos['city4_86'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_86'])

        # shadow city4_86 vao
        self.vaos['shadow_city4_86'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_86'])

        # City4_87 vao
        self.vaos['city4_87'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_87'])

        # shadow city4_87 vao
        self.vaos['shadow_city4_87'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_87'])

        # City4_88 vao
        self.vaos['city4_88'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_88'])

        # shadow city4_88 vao
        self.vaos['shadow_city4_88'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_88'])
        
         # City4_89 vao
        self.vaos['city4_89'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_89'])

        # shadow city4_89 vao
        self.vaos['shadow_city4_89'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_89'])

        # City4_90 vao
        self.vaos['city4_90'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_90'])

        # shadow city4_90 vao
        self.vaos['shadow_city4_90'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_90'])

        # City4_91 vao
        self.vaos['city4_91'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_91'])

        # shadow city4_91 vao
        self.vaos['shadow_city4_91'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_91'])

        # City4_92 vao
        self.vaos['city4_92'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_92'])

        # shadow city4_92 vao
        self.vaos['shadow_city4_92'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_92'])

        # City4_93 vao
        self.vaos['city4_93'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_93'])

        # shadow city4_93 vao
        self.vaos['shadow_city4_93'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_93'])

        # City4_94 vao
        self.vaos['city4_94'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_94'])

        # shadow city4_94 vao
        self.vaos['shadow_city4_94'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_94'])

        # City4_95 vao
        self.vaos['city4_95'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_95'])

        # shadow city4_95 vao
        self.vaos['shadow_city4_95'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_95'])
        
        # City4_96 vao
        self.vaos['city4_96'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_96'])

        # shadow city4_96 vao
        self.vaos['shadow_city4_96'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_96'])

        # City4_97 vao
        self.vaos['city4_97'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_97'])

        # shadow city4_97 vao
        self.vaos['shadow_city4_97'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_97'])

        # City4_98 vao
        self.vaos['city4_98'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_98'])

        # shadow city4_98 vao
        self.vaos['shadow_city4_98'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_98'])

        # City4_99 vao
        self.vaos['city4_99'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_99'])

        # shadow city4_99 vao
        self.vaos['shadow_city4_99'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_99'])

        # City4_100 vao
        self.vaos['city4_100'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_100'])

        # shadow city4_100 vao
        self.vaos['shadow_city4_100'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_100'])

        # City4_101 vao
        self.vaos['city4_101'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_101'])

        # shadow city4_101 vao
        self.vaos['shadow_city4_101'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_101'])

        # City4_102 vao
        self.vaos['city4_102'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_102'])

        # shadow city4_102 vao
        self.vaos['shadow_city4_102'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_102'])

        # City4_103 vao
        self.vaos['city4_103'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_103'])

        # shadow city4_103 vao
        self.vaos['shadow_city4_103'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_103'])

        # City4_104 vao
        self.vaos['city4_104'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_104'])

        # shadow city4_104 vao
        self.vaos['shadow_city4_104'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_104'])

        # City4_105 vao
        self.vaos['city4_105'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_105'])

        # shadow city4_105 vao
        self.vaos['shadow_city4_105'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_105'])
        
        
        # City4_106 vao
        self.vaos['city4_106'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_106'])

        # shadow city4_106 vao
        self.vaos['shadow_city4_106'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_106'])

        # City4_107 vao
        self.vaos['city4_107'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_107'])

        # shadow city4_107 vao
        self.vaos['shadow_city4_107'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_107'])

        # City4_108 vao
        self.vaos['city4_108'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_108'])

        # shadow city4_108 vao
        self.vaos['shadow_city4_108'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_108'])

        # City4_109 vao
        self.vaos['city4_109'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_109'])

        # shadow city4_109 vao
        self.vaos['shadow_city4_109'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_109'])

        # City4_110 vao
        self.vaos['city4_110'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_110'])

        # shadow city4_110 vao
        self.vaos['shadow_city4_110'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_110'])

        # City4_111 vao
        self.vaos['city4_111'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_111'])

        # shadow city4_111 vao
        self.vaos['shadow_city4_111'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_111'])

        # City4_112 vao
        self.vaos['city4_112'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_112'])

        # shadow city4_112 vao
        self.vaos['shadow_city4_112'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_112'])

        # City4_113 vao
        self.vaos['city4_113'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_113'])

        # shadow city4_113 vao
        self.vaos['shadow_city4_113'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_113'])

        # City4_114 vao
        self.vaos['city4_114'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_114'])

        # shadow city4_114 vao
        self.vaos['shadow_city4_114'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_114'])

        # City4_115 vao
        self.vaos['city4_115'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_115'])

        # shadow city4_115 vao
        self.vaos['shadow_city4_115'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_115'])

        # City4_116 vao
        self.vaos['city4_116'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_116'])

        # shadow city4_116 vao
        self.vaos['shadow_city4_116'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_116'])

        # City4_117 vao
        self.vaos['city4_117'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_117'])

        # shadow city4_117 vao
        self.vaos['shadow_city4_117'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_117'])

        # City4_118 vao
        self.vaos['city4_118'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_118'])

        # shadow city4_118 vao
        self.vaos['shadow_city4_118'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_118'])

        # City4_119 vao
        self.vaos['city4_119'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_119'])

        # shadow city4_119 vao
        self.vaos['shadow_city4_119'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_119'])

        # City4_120 vao
        self.vaos['city4_120'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_120'])

        # shadow city4_120 vao
        self.vaos['shadow_city4_120'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_120'])

        # City4_121 vao
        self.vaos['city4_121'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_121'])

        # shadow city4_121 vao
        self.vaos['shadow_city4_121'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_121'])

        # City4_122 vao
        self.vaos['city4_122'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_122'])

        # shadow city4_122 vao
        self.vaos['shadow_city4_122'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_122'])

        # City4_123 vao
        self.vaos['city4_123'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_123'])

        # shadow city4_123 vao
        self.vaos['shadow_city4_123'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_123'])

        # City4_124 vao
        self.vaos['city4_124'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_124'])

        # shadow city4_124 vao
        self.vaos['shadow_city4_124'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_124'])

        # City4_125 vao
        self.vaos['city4_125'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_125'])

        # shadow city4_125 vao
        self.vaos['shadow_city4_125'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_125'])

        # City4_126 vao
        self.vaos['city4_126'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_126'])

        # shadow city4_126 vao
        self.vaos['shadow_city4_126'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_126'])

        # City4_127 vao
        self.vaos['city4_127'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_127'])

        # shadow city4_127 vao
        self.vaos['shadow_city4_127'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_127'])

        # City4_128 vao
        self.vaos['city4_128'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_128'])

        # shadow city4_128 vao
        self.vaos['shadow_city4_128'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_128'])

        # City4_129 vao
        self.vaos['city4_129'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_129'])

        # shadow city4_129 vao
        self.vaos['shadow_city4_129'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_129'])
        
        # City4_130 vao
        self.vaos['city4_130'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_130'])

        # shadow city4_130 vao
        self.vaos['shadow_city4_130'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_130'])

        # City4_131 vao
        self.vaos['city4_131'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_131'])

        # shadow city4_131 vao
        self.vaos['shadow_city4_131'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_131'])
        
        # City4_132 vao
        self.vaos['city4_132'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_132'])

        # shadow city4_132 vao
        self.vaos['shadow_city4_132'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_132'])

        # City4_133 vao
        self.vaos['city4_133'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_133'])

        # shadow city4_133 vao
        self.vaos['shadow_city4_133'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_133'])

        # City4_134 vao
        self.vaos['city4_134'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_134'])

        # shadow city4_134 vao
        self.vaos['shadow_city4_134'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_134'])

        # City4_135 vao
        self.vaos['city4_135'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_135'])

        # shadow city4_135 vao
        self.vaos['shadow_city4_135'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_135'])

        # City4_136 vao
        self.vaos['city4_136'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_136'])

        # shadow city4_136 vao
        self.vaos['shadow_city4_136'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_136'])

        # City4_137 vao
        self.vaos['city4_137'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_137'])

        # shadow city4_137 vao
        self.vaos['shadow_city4_137'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_137'])

        # City4_138 vao
        self.vaos['city4_138'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_138'])

        # shadow city4_138 vao
        self.vaos['shadow_city4_138'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_138'])

        # City4_139 vao
        self.vaos['city4_139'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_139'])

        # shadow city4_139 vao
        self.vaos['shadow_city4_139'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_139'])

        # City4_140 vao
        self.vaos['city4_140'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_140'])

        # shadow city4_140 vao
        self.vaos['shadow_city4_140'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_140'])

        # City4_141 vao
        self.vaos['city4_141'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_141'])

        # shadow city4_141 vao
        self.vaos['shadow_city4_141'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_141'])

        # City4_142 vao
        self.vaos['city4_142'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_142'])

        # shadow city4_142 vao
        self.vaos['shadow_city4_142'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_142'])

        # City4_143 vao
        self.vaos['city4_143'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_143'])

        # shadow city4_143 vao
        self.vaos['shadow_city4_143'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_143'])

        # City4_144 vao
        self.vaos['city4_144'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_144'])

        # shadow city4_144 vao
        self.vaos['shadow_city4_144'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_144'])

        # City4_145 vao
        self.vaos['city4_145'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_145'])

        # shadow city4_145 vao
        self.vaos['shadow_city4_145'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_145'])

        # City4_146 vao
        self.vaos['city4_146'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_146'])

        # shadow city4_146 vao
        self.vaos['shadow_city4_146'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_146'])

        # City4_147 vao
        self.vaos['city4_147'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_147'])

        # shadow city4_147 vao
        self.vaos['shadow_city4_147'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_147'])

        # City4_148 vao
        self.vaos['city4_148'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_148'])

        # shadow city4_148 vao
        self.vaos['shadow_city4_148'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_148'])

        # City4_149 vao
        self.vaos['city4_149'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_149'])

        # shadow city4_149 vao
        self.vaos['shadow_city4_149'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_149'])

        # City4_150 vao
        self.vaos['city4_150'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_150'])

        # shadow city4_150 vao
        self.vaos['shadow_city4_150'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_150'])

        # City4_151 vao
        self.vaos['city4_151'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_151'])

        # shadow city4_151 vao
        self.vaos['shadow_city4_151'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_151'])

        # City4_152 vao
        self.vaos['city4_152'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_152'])

        # shadow city4_152 vao
        self.vaos['shadow_city4_152'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_152'])

        # City4_153 vao
        self.vaos['city4_153'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_153'])

        # shadow city4_153 vao
        self.vaos['shadow_city4_153'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_153'])

        # City4_154 vao
        self.vaos['city4_154'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_154'])

        # shadow city4_154 vao
        self.vaos['shadow_city4_154'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_154'])

        # City4_155 vao
        self.vaos['city4_155'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_155'])

        # shadow city4_155 vao
        self.vaos['shadow_city4_155'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_155'])

        # City4_156 vao
        self.vaos['city4_156'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_156'])

        # shadow city4_156 vao
        self.vaos['shadow_city4_156'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_156'])

        # City4_157 vao
        self.vaos['city4_157'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_157'])

        # shadow city4_157 vao
        self.vaos['shadow_city4_157'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_157'])

        # City4_158 vao
        self.vaos['city4_158'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_158'])

        # shadow city4_158 vao
        self.vaos['shadow_city4_158'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_158'])

        # City4_159 vao
        self.vaos['city4_159'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_159'])

        # shadow city4_159 vao
        self.vaos['shadow_city4_159'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_159'])

        # City4_160 vao
        self.vaos['city4_160'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_160'])

        # shadow city4_160 vao
        self.vaos['shadow_city4_160'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_160'])

        # City4_161 vao
        self.vaos['city4_161'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_161'])

        # shadow city4_161 vao
        self.vaos['shadow_city4_161'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_161'])

        # City4_162 vao
        self.vaos['city4_162'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_162'])

        # shadow city4_162 vao
        self.vaos['shadow_city4_162'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_162'])

        # City4_163 vao
        self.vaos['city4_163'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_163'])

        # shadow city4_163 vao
        self.vaos['shadow_city4_163'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_163'])

        # City4_164 vao
        self.vaos['city4_164'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_164'])

        # shadow city4_164 vao
        self.vaos['shadow_city4_164'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_164'])
        
        
        # City4_165 vao
        self.vaos['city4_165'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_165'])

        # shadow city4_165 vao
        self.vaos['shadow_city4_165'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_165'])

        # City4_166 vao
        self.vaos['city4_166'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_166'])

        # shadow city4_166 vao
        self.vaos['shadow_city4_166'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_166'])

        # City4_167 vao
        self.vaos['city4_167'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_167'])

        # shadow city4_167 vao
        self.vaos['shadow_city4_167'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_167'])

        # City4_168 vao
        self.vaos['city4_168'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['city4_168'])

        # shadow city4_168 vao
        self.vaos['shadow_city4_168'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['city4_168'])


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