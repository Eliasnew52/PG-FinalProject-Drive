from Model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.camera_offset = glm.vec3(-1, -9, -2)
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
        # add(Car1(app))
        # add(Car2(app))
        # add(Car3(app))
        # add(Car4(app))
        # add(Car5(app))
        # add(Car6(app))
        
        #add(City1(app, pos=(0, 0, 0)))
        
        if self.app.map == 1:
            add(City1(app, pos=(0, 0, 0)))

            self.moving_car1 = MovingCar1(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car2 = MovingCar2(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car3 = MovingCar3(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car4 = MovingCar4(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car5 = MovingCar5(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car6 = MovingCar6(app, pos=self.app.camera.position, scale=(2, 2, 2))


            add(self.moving_car1)
            add(self.moving_car2)
            add(self.moving_car3)
            add(self.moving_car4)
            add(self.moving_car5)
            add(self.moving_car6)
        

        # self.moving_cube = MovingCube(app, pos=(0, 100, 8), scale=(3, 3, 3), tex_id=1)
        # add(self.moving_cube)
        
        
        
        if self.app.map ==2:
            self.moving_car1 = MovingCar1(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car2 = MovingCar2(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car3 = MovingCar3(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car4 = MovingCar4(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car5 = MovingCar5(app, pos=self.app.camera.position, scale=(2, 2, 2))
            self.moving_car6 = MovingCar6(app, pos=self.app.camera.position, scale=(2, 2, 2))


            add(self.moving_car1)
            add(self.moving_car2)
            add(self.moving_car3)
            add(self.moving_car4)
            add(self.moving_car5)
            add(self.moving_car6)
            
            
            add(City4_1(app, pos=(0, 0, 0)))

            add(City4_2(app, pos=(0, 0, 0)))#hospital
            add(City4_2(app, pos=(-8*126, 0, 252)))
            add(City4_2(app, pos=(-20*126, 0, -126)))
            add(City4_2(app, pos=(-4*126, 0, 4*-126)))

            #Factory
            add(City4_3(app, pos=(0, 0, 0)))
            add(City4_4(app, pos=(0, 0, 0)))
            add(City4_5(app, pos=(0, 0, 0)))
            add(City4_6(app, pos=(0, 0, 0)))
            add(City4_7(app, pos=(0, 0, 0)))
            add(City4_8(app, pos=(0, 0, 0)))
            add(City4_9(app, pos=(0, 0, 0)))
            add(City4_10(app, pos=(0, 0, 0)))
            add(City4_11(app, pos=(0, 0, 0)))
            add(City4_12(app, pos=(0, 0, 0)))
            add(City4_13(app, pos=(0, 0, 0)))
            add(City4_14(app, pos=(0, 0, 0)))
            add(City4_15(app, pos=(0, 0, 0)))
            add(City4_16(app, pos=(0, 0, 0)))
            add(City4_17(app, pos=(0, 0, 0)))
            add(City4_18(app, pos=(0, 0, 0)))
            add(City4_19(app, pos=(0, 0, 0)))
            add(City4_20(app, pos=(0, 0, 0)))
            add(City4_23(app, pos=(0, 0, 0)))
            add(City4_22(app, pos=(0, 0, 0)))
            add(City4_23(app, pos=(0, 0, 0)))
            add(City4_24(app, pos=(0, 0, 0)))
            add(City4_25(app, pos=(0, 0, 0)))
            add(City4_26(app, pos=(0, 0, 0)))
            add(City4_27(app, pos=(0, 0, 0)))
            add(City4_28(app, pos=(0, 0, 0)))
            add(City4_29(app, pos=(0, 0, 0)))
            add(City4_30(app, pos=(0, 0, 0)))
            add(City4_31(app, pos=(0, 0, 0)))
            add(City4_32(app, pos=(0, 0, 0)))
            add(City4_33(app, pos=(0, 0, 0)))
            add(City4_34(app, pos=(0, 0, 0)))
            add(City4_35(app, pos=(0, 0, 0)))
            add(City4_36(app, pos=(0, 0, 0)))
            add(City4_37(app, pos=(0, 0, 0)))
            add(City4_38(app, pos=(0, 0, 0)))
            add(City4_39(app, pos=(0, 0, 0)))
            add(City4_40(app, pos=(0, 0, 0)))
            add(City4_41(app, pos=(0, 0, 0)))
            add(City4_42(app, pos=(0, 0, 0)))
            add(City4_43(app, pos=(0, 0, 0)))
            add(City4_44(app, pos=(0, 0, 0)))
            add(City4_45(app, pos=(0, 0, 0)))
            add(City4_46(app, pos=(0, 0, 0)))
            add(City4_47(app, pos=(0, 0, 0)))
            add(City4_48(app, pos=(0, 0, 0)))
            add(City4_49(app, pos=(0, 0, 0)))
            add(City4_50(app, pos=(0, 0, 0)))

            add(City4_51(app, pos=(0, 0, 0)))#city_cancha_edificio
            add(City4_52(app, pos=(0, 0, 0)))
            add(City4_53(app, pos=(0, 0, 0)))
            add(City4_54(app, pos=(0, 0, 0)))
            add(City4_55(app, pos=(0, 0, 0)))
            add(City4_56(app, pos=(0, 0, 0)))
            add(City4_57(app, pos=(0, 0, 0)))
            add(City4_58(app, pos=(0, 0, 0)))
            add(City4_59(app, pos=(0, 0, 0)))
            add(City4_60(app, pos=(0, 0, 0)))
            add(City4_61(app, pos=(0, 0, 0)))
            add(City4_62(app, pos=(0, 0, 0)))
            add(City4_63(app, pos=(0, 0, 0)))
            add(City4_51(app, pos=(6*126, 0, 0)))#city_cancha_edificio2
            add(City4_52(app, pos=(6*126, 0, 0)))
            add(City4_53(app, pos=(6*126, 0, 0)))
            add(City4_54(app, pos=(6*126, 0, 0)))
            add(City4_55(app, pos=(6*126, 0, 0)))
            add(City4_56(app, pos=(6*126, 0, 0)))
            add(City4_57(app, pos=(6*126, 0, 0)))
            add(City4_58(app, pos=(6*126, 0, 0)))
            add(City4_59(app, pos=(6*126, 0, 0)))
            add(City4_60(app, pos=(6*126, 0, 0)))
            add(City4_61(app, pos=(6*126, 0, 0)))
            add(City4_62(app, pos=(6*126, 0, 0)))
            add(City4_63(app, pos=(6*126, 0, 0)))
            add(City4_51(app, pos=(12*-126, 0, -126)))#city_cancha_edificio3
            add(City4_52(app, pos=(12*-126, 0, -126)))
            add(City4_53(app, pos=(12*-126, 0, -126)))
            add(City4_54(app, pos=(12*-126, 0, -126)))
            add(City4_55(app, pos=(12*-126, 0, -126)))
            add(City4_56(app, pos=(12*-126, 0, -126)))
            add(City4_57(app, pos=(12*-126, 0, -126)))
            add(City4_58(app, pos=(12*-126, 0, -126)))
            add(City4_59(app, pos=(12*-126, 0, -126)))
            add(City4_60(app, pos=(12*-126, 0, -126)))
            add(City4_61(app, pos=(12*-126, 0, -126)))
            add(City4_62(app, pos=(12*-126, 0, -126)))
            add(City4_63(app, pos=(12*-126, 0, -126)))
            
            add(City4_51(app, pos=(4*-126, 0, 4*126)))#city_cancha_edificio4
            add(City4_52(app, pos=(4*-126, 0, 4*126)))
            add(City4_53(app, pos=(4*-126, 0, 4*126)))
            add(City4_54(app, pos=(4*-126, 0, 4*126)))
            add(City4_55(app, pos=(4*-126, 0, 4*126)))
            add(City4_56(app, pos=(4*-126, 0, 4*126)))
            add(City4_57(app, pos=(4*-126, 0, 4*126)))
            add(City4_58(app, pos=(4*-126, 0, 4*126)))
            add(City4_59(app, pos=(4*-126, 0, 4*126)))
            add(City4_60(app, pos=(4*-126, 0, 4*126)))
            add(City4_61(app, pos=(4*-126, 0, 4*126)))
            add(City4_62(app, pos=(4*-126, 0, 4*126)))
            add(City4_63(app, pos=(4*-126, 0, 4*126)))

            add(City4_51(app, pos=(2*-126, 0, 2*-126)))#city_cancha_edificio5
            add(City4_52(app, pos=(2*-126, 0, 2*-126)))
            add(City4_53(app, pos=(2*-126, 0, 2*-126)))
            add(City4_54(app, pos=(2*-126, 0, 2*-126)))
            add(City4_55(app, pos=(2*-126, 0, 2*-126)))
            add(City4_56(app, pos=(2*-126, 0, 2*-126)))
            add(City4_57(app, pos=(2*-126, 0, 2*-126)))
            add(City4_58(app, pos=(2*-126, 0, 2*-126)))
            add(City4_59(app, pos=(2*-126, 0, 2*-126)))
            add(City4_60(app, pos=(2*-126, 0, 2*-126)))
            add(City4_61(app, pos=(2*-126, 0, 2*-126)))
            add(City4_62(app, pos=(2*-126, 0, 2*-126)))
            add(City4_63(app, pos=(2*-126, 0, 2*-126)))

            add(City4_51(app, pos=(12*-126, 0, 4*126)))#city_cancha_edificio6
            add(City4_52(app, pos=(12*-126, 0, 4*126)))
            add(City4_53(app, pos=(12*-126, 0, 4*126)))
            add(City4_54(app, pos=(12*-126, 0, 4*126)))
            add(City4_55(app, pos=(12*-126, 0, 4*126)))
            add(City4_56(app, pos=(12*-126, 0, 4*126)))
            add(City4_57(app, pos=(12*-126, 0, 4*126)))
            add(City4_58(app, pos=(12*-126, 0, 4*126)))
            add(City4_59(app, pos=(12*-126, 0, 4*126)))
            add(City4_60(app, pos=(12*-126, 0, 4*126)))
            add(City4_61(app, pos=(12*-126, 0, 4*126)))
            add(City4_62(app, pos=(12*-126, 0, 4*126)))
            add(City4_63(app, pos=(12*-126, 0, 4*126)))

            add(City4_51(app, pos=(6*126, 0, 4*126)))#city_cancha_edificio6
            add(City4_52(app, pos=(6*126, 0, 4*126)))
            add(City4_53(app, pos=(6*126, 0, 4*126)))
            add(City4_54(app, pos=(6*126, 0, 4*126)))
            add(City4_55(app, pos=(6*126, 0, 4*126)))
            add(City4_56(app, pos=(6*126, 0, 4*126)))
            add(City4_57(app, pos=(6*126, 0, 4*126)))
            add(City4_58(app, pos=(6*126, 0, 4*126)))
            add(City4_59(app, pos=(6*126, 0, 4*126)))
            add(City4_60(app, pos=(6*126, 0, 4*126)))
            add(City4_61(app, pos=(6*126, 0, 4*126)))
            add(City4_62(app, pos=(6*126, 0, 4*126)))
            add(City4_63(app, pos=(6*126, 0, 4*126)))

            add(City4_51(app, pos=(8*-126, 0, 2*-126)))#city_cancha_edificio7
            add(City4_52(app, pos=(8*-126, 0, 2*-126)))
            add(City4_53(app, pos=(8*-126, 0, 2*-126)))
            add(City4_54(app, pos=(8*-126, 0, 2*-126)))
            add(City4_55(app, pos=(8*-126, 0, 2*-126)))
            add(City4_56(app, pos=(8*-126, 0, 2*-126)))
            add(City4_57(app, pos=(8*-126, 0, 2*-126)))
            add(City4_58(app, pos=(8*-126, 0, 2*-126)))
            add(City4_59(app, pos=(8*-126, 0, 2*-126)))
            add(City4_60(app, pos=(8*-126, 0, 2*-126)))
            add(City4_61(app, pos=(8*-126, 0, 2*-126)))
            add(City4_62(app, pos=(8*-126, 0, 2*-126)))
            add(City4_63(app, pos=(8*-126, 0, 2*-126)))

            add(City4_84(app, pos=(0, 0, 0))) #cancha
            add(City4_84(app, pos=(-1890, 0, 0)))

            add(City4_85(app, pos=(0, 0, 0)))#lavanderia
            add(City4_86(app, pos=(0, 0, 0)))
            add(City4_87(app, pos=(0, 0, 0)))
            add(City4_88(app, pos=(0, 0, 0)))

            add(City4_86(app, pos=(9*126, 0, 3*126)))#lavanderia2

            add(City4_89(app, pos=(0, 0, 0))) #Tieda_armas
            add(City4_90(app, pos=(0, 0, 0)))
            add(City4_91(app, pos=(0, 0, 0)))
            add(City4_92(app, pos=(0, 0, 0)))
            add(City4_93(app, pos=(0, 0, 0)))

            add(City4_89(app, pos=(-189, 0, 252))) #Tieda_armas2
            add(City4_90(app, pos=(-189, 0, 252)))
            add(City4_91(app, pos=(-189, 0, 252)))
            add(City4_92(app, pos=(-189, 0, 252)))
            add(City4_93(app, pos=(-189, 0, 252)))
            add(City4_94(app, pos=(-189, 0, 252)))

            add(City4_89(app, pos=(12*126, 0, 252))) #Tieda_armas3
            add(City4_90(app, pos=(12*126, 0, 252)))
            add(City4_91(app, pos=(12*126, 0, 252)))
            add(City4_92(app, pos=(12*126, 0, 252)))
            add(City4_93(app, pos=(12*126, 0, 252)))
            add(City4_94(app, pos=(12*126, 0, 252)))

            add(City4_94(app, pos=(0, 0, 0)))
            add(City4_95(app, pos=(0, 0, 0)))
            add(City4_96(app, pos=(0, 0, 0)))
            add(City4_97(app, pos=(0, 0, 0)))
            add(City4_98(app, pos=(0, 0, 0)))
            add(City4_99(app, pos=(0, 0, 0)))
            add(City4_100(app, pos=(0, 0, 0)))
            add(City4_101(app, pos=(0, 0, 0)))
            add(City4_102(app, pos=(0, 0, 0)))
            add(City4_103(app, pos=(0, 0, 0)))
            add(City4_104(app, pos=(0, 0, 0)))
            add(City4_105(app, pos=(0, 0, 0)))

            add(City4_106(app, pos=(0, 0, 0)))#liquor
            add(City4_107(app, pos=(0, 0, 0)))
            add(City4_108(app, pos=(0, 0, 0)))
            add(City4_109(app, pos=(0, 0, 0)))
            add(City4_110(app, pos=(0, -40, 0)))

            add(City4_106(app, pos=(7*126, 0, 4*-126)))#liquor2
            add(City4_108(app, pos=(7*126, 0, 4*-126)))
            add(City4_109(app, pos=(7*126, 0, 4*-126)))
            add(City4_110(app, pos=(7*126, -40, 4*-126)))

            add(City4_106(app, pos=(4*-126, 0, 4*-126)))#liquor3
            add(City4_108(app, pos=(4*-126, 0, 4*-126)))
            add(City4_109(app, pos=(4*-126, 0, 4*-126)))
            add(City4_110(app, pos=(4*-126, -40, 4*-126)))

            add(City4_111(app, pos=(0, 0, 0)))
            add(City4_112(app, pos=(0, 0, 0)))
            add(City4_113(app, pos=(0, -40, 0)))
            add(City4_114(app, pos=(0, -40, 0)))
            add(City4_115(app, pos=(0, 0, 0)))

            add(City4_116(app, pos=(0, 0, 0))) #paramount
            add(City4_117(app, pos=(0, 0, 0)))
            add(City4_118(app, pos=(0, 0, 0)))
            add(City4_119(app, pos=(0, 0, 0)))
            add(City4_120(app, pos=(0, 0, 0)))
            add(City4_121(app, pos=(0, 0, 0)))
            add(City4_122(app, pos=(0, 0, 0)))
            add(City4_123(app, pos=(0, 0, 0)))

            add(City4_116(app, pos=(2*-126, 0, 4*-126))) #paramount2
            add(City4_117(app, pos=(2*-126, 0, 4*-126)))
            add(City4_118(app, pos=(2*-126, 0, 4*-126)))
            add(City4_119(app, pos=(2*-126, 0, 4*-126)))
            add(City4_120(app, pos=(2*-126, 0, 4*-126)))
            add(City4_121(app, pos=(2*-126, 0, 4*-126)))
            add(City4_122(app, pos=(2*-126, 0, 4*-126)))
            add(City4_123(app, pos=(2*-126, 0, 4*-126)))
            add(City4_124(app, pos=(2*-126, 0, 4*-126)))

            add(City4_116(app, pos=(3*126, 0, 4*-126))) #paramount3
            add(City4_117(app, pos=(3*126, 0, 4*-126)))
            add(City4_118(app, pos=(3*126, 0, 4*-126)))
            add(City4_119(app, pos=(3*126, 0, 4*-126)))
            add(City4_120(app, pos=(3*126, 0, 4*-126)))
            add(City4_121(app, pos=(3*126, 0, 4*-126)))
            add(City4_122(app, pos=(3*126, 0, 4*-126)))
            add(City4_123(app, pos=(3*126, 0, 4*-126)))
            add(City4_124(app, pos=(3*126, 0, 4*-126)))

            add(City4_116(app, pos=(6*-126, 0, 2*126))) #paramount4
            add(City4_117(app, pos=(6*-126, 0, 2*126)))
            add(City4_118(app, pos=(6*-126, 0, 2*126)))
            add(City4_119(app, pos=(6*-126, 0, 2*126)))
            add(City4_120(app, pos=(6*-126, 0, 2*126)))
            add(City4_121(app, pos=(6*-126, 0, 2*126)))
            add(City4_122(app, pos=(6*-126, 0, 2*126)))
            add(City4_123(app, pos=(6*-126, 0, 2*126)))
            add(City4_124(app, pos=(6*-126, 0, 2*126)))

            add(City4_116(app, pos=(5*126, 0, 2*126))) #paramount5
            add(City4_117(app, pos=(5*126, 0, 2*126)))
            add(City4_118(app, pos=(5*126, 0, 2*126)))
            add(City4_119(app, pos=(5*126, 0, 2*126)))
            add(City4_120(app, pos=(5*126, 0, 2*126)))
            add(City4_121(app, pos=(5*126, 0, 2*126)))
            add(City4_122(app, pos=(5*126, 0, 2*126)))
            add(City4_123(app, pos=(5*126, 0, 2*126)))
            add(City4_124(app, pos=(5*126, 0, 2*126)))

            add(City4_124(app, pos=(0, 0, 0)))
            add(City4_125(app, pos=(0, 0, 0)))
            add(City4_126(app, pos=(0, 0, 0)))
            add(City4_127(app, pos=(0, 0, 0)))
            add(City4_128(app, pos=(0, 0, 0)))
            add(City4_129(app, pos=(0, 0, 0)))
            add(City4_130(app, pos=(0, 0, 0)))
            add(City4_131(app, pos=(0, 0, 0)))
            add(City4_132(app, pos=(0, 0, 0)))
            add(City4_133(app, pos=(0, 0, 0)))
            add(City4_134(app, pos=(0, -25, 0)))
            add(City4_135(app, pos=(0, -25, 0)))
            add(City4_136(app, pos=(0, -25, 0)))
            add(City4_137(app, pos=(0, -25, 0)))
            add(City4_138(app, pos=(0, -25, 0)))
            add(City4_139(app, pos=(0, -25, 0)))
            add(City4_140(app, pos=(0, -25, 0)))
            add(City4_141(app, pos=(0, -25, 0)))
            add(City4_142(app, pos=(0, -25, 0)))
            add(City4_143(app, pos=(0, -25, 0)))
            add(City4_144(app, pos=(0, -25, 0)))
            add(City4_145(app, pos=(0, -25, 0)))

            add(City4_146(app, pos=(0, 0, 0)))#chino
            add(City4_147(app, pos=(0, 0, 0)))
            add(City4_148(app, pos=(0, 0, 0)))
            add(City4_149(app, pos=(0, 0, 0)))
            add(City4_150(app, pos=(0, 0, 0)))

            add(City4_146(app, pos=(8*126, 0, -126)))#chino2
            add(City4_147(app, pos=(8*126, 0, -126)))
            add(City4_148(app, pos=(8*126, 0, -126)))

            add(City4_146(app, pos=(4*126, 0, -126*4)))#chino3
            add(City4_147(app, pos=(4*126, 0, -126*4)))
            add(City4_148(app, pos=(4*126, 0, -126*4)))

            add(City4_146(app, pos=(10*126, 0, -126*4)))#chino4
            add(City4_147(app, pos=(10*126, 0, -126*4)))
            add(City4_148(app, pos=(10*126, 0, -126*4)))

            add(City4_146(app, pos=(20*126, 0, 126)))#chino5
            add(City4_147(app, pos=(20*126, 0, 126)))
            add(City4_148(app, pos=(20*126, 0, 126)))

            add(City4_146(app, pos=(19*126, 0, 252)))#chino5
            add(City4_147(app, pos=(19*126, 0, 252)))
            add(City4_148(app, pos=(19*126, 0, 252)))

            add(City4_146(app, pos=(-256, 0, 4*-126)))#chino6
            add(City4_147(app, pos=(-256, 0, 4*-126)))
            add(City4_148(app, pos=(-256, 0, 4*-126)))

            add(City4_151(app, pos=(882, 0, -126)))#pisos
            add(City4_151(app, pos=(1008, 0, -126)))
            add(City4_151(app, pos=(1260, 0, -126)))
            add(City4_151(app, pos=(756, 0, -252)))
            add(City4_151(app, pos=(882, 0, -252)))
            add(City4_151(app, pos=(1008, 0, -252)))
            add(City4_151(app, pos=(1260, 0, -252)))
            add(City4_151(app, pos=(1260, 0, -504)))
            add(City4_151(app, pos=(1638, 0, -504)))
            add(City4_151(app, pos=(1260, 0, -630)))
            add(City4_151(app, pos=(1260, 0, -756)))
            add(City4_151(app, pos=(1638, 0, -756)))

            add(City4_151(app, pos=(0, 0, 0)))#piso doble
            add(City4_152(app, pos=(0, 0, 0)))
            add(City4_153(app, pos=(0, 0, 0)))
            add(City4_154(app, pos=(0, 0, 0)))
            add(City4_155(app, pos=(0, 0, 0)))
            add(City4_156(app, pos=(0, 0, 0)))
            add(City4_157(app, pos=(0, 0, 0)))
            add(City4_158(app, pos=(0, 0, 0)))
            add(City4_159(app, pos=(0, 0, 0)))
            add(City4_160(app, pos=(0, 0, 0)))
            add(City4_161(app, pos=(0, 0, 0)))
            add(City4_162(app, pos=(0, 0, 0)))
            add(City4_163(app, pos=(0, 0, 0)))
            add(City4_164(app, pos=(0, 0, 0)))

            add(City4_152(app, pos=(8*126, 0, -252)))#piso doble2
            add(City4_153(app, pos=(8*126, 0, -252)))
            add(City4_154(app, pos=(8*126, 0, -252)))
            add(City4_155(app, pos=(8*126, 0, -252)))
            add(City4_156(app, pos=(8*126, 0, -252)))
            add(City4_157(app, pos=(8*126, 0, -252)))
            add(City4_158(app, pos=(8*126, 0, -252)))
            add(City4_159(app, pos=(8*126, 0, -252)))
            add(City4_160(app, pos=(8*126, 0, -252)))
            add(City4_161(app, pos=(8*126, 0, -252)))
            add(City4_162(app, pos=(8*126, 0, -252)))
            add(City4_163(app, pos=(8*126, 0, -252)))
            add(City4_164(app, pos=(8*126, 0, -252)))

            add(City4_152(app, pos=(4*126, 0, 252)))#piso doble2
            add(City4_153(app, pos=(4*126, 0, 252)))
            add(City4_154(app, pos=(4*126, 0, 252)))
            add(City4_155(app, pos=(4*126, 0, 252)))
            add(City4_156(app, pos=(4*126, 0, 252)))
            add(City4_157(app, pos=(4*126, 0, 252)))
            add(City4_158(app, pos=(4*126, 0, 252)))
            add(City4_159(app, pos=(4*126, 0, 252)))
            add(City4_160(app, pos=(4*126, 0, 252)))
            add(City4_161(app, pos=(4*126, 0, 252)))
            add(City4_162(app, pos=(4*126, 0, 252)))
            add(City4_163(app, pos=(4*126, 0, 252)))
            add(City4_164(app, pos=(4*126, 0, 252)))

            add(City4_152(app, pos=(16*126, 0, 252)))#piso doble3
            add(City4_153(app, pos=(16*126, 0, 252)))
            add(City4_155(app, pos=(16*126, 0, 252)))
            add(City4_156(app, pos=(16*126, 0, 252)))

            add(City4_152(app, pos=(252, 0, 6*-126)))#piso doble4
            add(City4_153(app, pos=(252, 0, 6*-126)))
            add(City4_155(app, pos=(252, 0, 6*-126)))
            add(City4_156(app, pos=(252, 0, 6*-126)))

            add(City4_152(app, pos=(12*126, 0, 6*-126)))#piso doble4
            add(City4_153(app, pos=(12*126, 0, 6*-126)))
            add(City4_155(app, pos=(12*126, 0, 6*-126)))
            add(City4_156(app, pos=(12*126, 0, 6*-126)))

            add(City4_152(app, pos=(8*126, 0, 6*-126)))#piso doble5
            add(City4_153(app, pos=(8*126, 0, 6*-126)))
            add(City4_154(app, pos=(8*126, 0, 6*-126)))
            add(City4_155(app, pos=(8*126, 0, 6*-126)))
            add(City4_156(app, pos=(8*126, 0, 6*-126)))
            add(City4_157(app, pos=(8*126, 0, 6*-126)))
            add(City4_158(app, pos=(8*126, 0, 6*-126)))
            add(City4_159(app, pos=(8*126, 0, 6*-126)))
            add(City4_160(app, pos=(8*126, 0, 6*-126)))
            add(City4_161(app, pos=(8*126, 0, 6*-126)))
            add(City4_162(app, pos=(8*126, 0, 6*-126)))
            add(City4_163(app, pos=(8*126, 0, 6*-126)))
            add(City4_164(app, pos=(8*126, 0, 6*-126)))

            add(City4_152(app, pos=(23*126, 0, 0)))#piso doble6
            add(City4_153(app, pos=(23*126, 0, 0)))
            add(City4_154(app, pos=(23*126, 0, 0)))
            add(City4_155(app, pos=(23*126, 0, 0)))
            add(City4_156(app, pos=(23*126, 0, 0)))
            add(City4_157(app, pos=(23*126, 0, 0)))
            add(City4_158(app, pos=(23*126, 0, 0)))
            add(City4_159(app, pos=(23*126, 0, 0)))
            add(City4_160(app, pos=(23*126, 0, 0)))
            add(City4_161(app, pos=(23*126, 0, 0)))
            add(City4_162(app, pos=(23*126, 0, 0)))
            add(City4_163(app, pos=(23*126, 0, 0)))
            add(City4_164(app, pos=(23*126, 0, 0)))

            add(City4_165(app, pos=(0, 0, 0)))#lammpost
            add(City4_166(app, pos=(0, 0, 0)))
            add(City4_167(app, pos=(0, 0, 0)))
            add(City4_168(app, pos=(0, 0, 0)))

            add(City4_165(app, pos=(2*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(2*-126, 0, 0)))
            add(City4_167(app, pos=(2*-126, 0, 0)))
            add(City4_168(app, pos=(2*-126, 0, 0)))

            add(City4_165(app, pos=(4*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(4*-126, 0, 0)))
            add(City4_167(app, pos=(4*-126, 0, 0)))
            add(City4_168(app, pos=(4*-126, 0, 0)))

            add(City4_165(app, pos=(6*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(6*-126, 0, 0)))
            add(City4_167(app, pos=(6*-126, 0, 0)))
            add(City4_168(app, pos=(6*-126, 0, 0)))

            add(City4_165(app, pos=(8*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(8*-126, 0, 0)))
            add(City4_167(app, pos=(8*-126, 0, 0)))
            add(City4_168(app, pos=(8*-126, 0, 0)))

            add(City4_165(app, pos=(10*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(10*-126, 0, 0)))
            add(City4_167(app, pos=(10*-126, 0, 0)))
            add(City4_168(app, pos=(10*-126, 0, 0)))

            add(City4_165(app, pos=(12*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(12*-126, 0, 0)))
            add(City4_167(app, pos=(12*-126, 0, 0)))
            add(City4_168(app, pos=(12*-126, 0, 0)))

            add(City4_165(app, pos=(14*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(14*-126, 0, 0)))
            add(City4_167(app, pos=(14*-126, 0, 0)))
            add(City4_168(app, pos=(14*-126, 0, 0)))

            add(City4_165(app, pos=(16*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(16*-126, 0, 0)))
            add(City4_167(app, pos=(16*-126, 0, 0)))
            add(City4_168(app, pos=(16*-126, 0, 0)))

            add(City4_165(app, pos=(18*-126, 0, 0)))#lammpost
            add(City4_166(app, pos=(18*-126, 0, 0)))
            add(City4_167(app, pos=(18*-126, 0, 0)))
            add(City4_168(app, pos=(18*-126, 0, 0)))

            add(City4_165(app, pos=(6*-126, 0, 4*-126)))#lammpost
            add(City4_166(app, pos=(6*-126, 0, 4*-126)))
            add(City4_167(app, pos=(6*-126, 0, 4*-126)))
            add(City4_168(app, pos=(6*-126, 0, 4*-126)))

            add(City4_165(app, pos=(8*-126, 0, 4*-126)))#lammpost
            add(City4_166(app, pos=(8*-126, 0, 4*-126)))
            add(City4_167(app, pos=(8*-126, 0, 4*-126)))
            add(City4_168(app, pos=(8*-126, 0, 4*-126)))

            add(City4_165(app, pos=(10*-126, 0, 4*-126)))#lammpost
            add(City4_166(app, pos=(10*-126, 0, 4*-126)))
            add(City4_167(app, pos=(10*-126, 0, 4*-126)))
            add(City4_168(app, pos=(10*-126, 0, 4*-126)))

            add(City4_165(app, pos=(12*-126, 0, 4*-126)))#lammpost
            add(City4_166(app, pos=(12*-126, 0, 4*-126)))
            add(City4_167(app, pos=(12*-126, 0, 4*-126)))
            add(City4_168(app, pos=(12*-126, 0, 4*-126)))

            add(City4_165(app, pos=(14*-126, 0, 4*-126)))#lammpost
            add(City4_166(app, pos=(14*-126, 0, 4*-126)))
            add(City4_167(app, pos=(14*-126, 0, 4*-126)))
            add(City4_168(app, pos=(14*-126, 0, 4*-126)))

            add(City4_165(app, pos=(16*-126, 0, 4*-126)))#lammpost
            add(City4_166(app, pos=(16*-126, 0, 4*-126)))
            add(City4_167(app, pos=(16*-126, 0, 4*-126)))
            add(City4_168(app, pos=(16*-126, 0, 4*-126)))

            add(City4_165(app, pos=(18*-126, 0, 4*-126)))#lammpost
            add(City4_166(app, pos=(18*-126, 0, 4*-126)))
            
        if self.app.map == 3:
            add(City3(app, pos=(0, 0, 0)))
            self.RadioCube= MovingCube(app,pos=(self.app.camera.position[0] + 5, self.app.camera.position[1]-2, self.app.camera.position[2] + 4) )
            self.moving_car1 = MovingCar1(app, pos=self.app.camera.position)
            self.moving_car2 = MovingCar2(app, pos=self.app.camera.position)
            self.moving_car3 = MovingCar3(app, pos=self.app.camera.position)
            self.moving_car4 = MovingCar4(app, pos=self.app.camera.position)
            self.moving_car5 = MovingCar5(app, pos=self.app.camera.position)
            self.moving_car6 = MovingCar6(app, pos=self.app.camera.position)
            
            add(self.moving_car1)
            add(self.moving_car2)
            add(self.moving_car3)
            add(self.moving_car4)
            add(self.moving_car5)
            add(self.moving_car6)

            add(self.RadioCube)


    def update(self):
        
        keys = pg.key.get_pressed()

        pg.mouse.set_pos((self.app.HALF_WIDTH, self.app.HALF_HEIGHT))

        if self.app.map == 1 or self.app.map == 2:
        
            new_car_pos = glm.vec3(self.app.camera.position) + self.camera_offset
            self.moving_car1.pos = new_car_pos
            self.moving_car2.pos = new_car_pos
            self.moving_car3.pos = new_car_pos
            self.moving_car4.pos = new_car_pos
            self.moving_car5.pos = new_car_pos
            self.moving_car6.pos = new_car_pos 
    
            # self.moving_car1.rot.y = self.app.camera.yaw * -0.01
            # self.moving_car2.rot.y = self.app.camera.yaw * -0.01
            # self.moving_car3.rot.y = self.app.camera.yaw * -0.01
            # self.moving_car4.rot.y = self.app.camera.yaw * -0.01
            # self.moving_car5.rot.y = self.app.camera.yaw * -0.01
            # self.moving_car6.rot.y = self.app.camera.yaw * -0.01 
            
            if keys[pg.K_a]:
                self.moving_car1.rot.y += 0.1 
                self.moving_car2.rot.y += 0.1 
                self.moving_car3.rot.y += 0.1    
                self.moving_car4.rot.y += 0.1    
                self.moving_car5.rot.y += 0.1    
                self.moving_car6.rot.y += 0.1
            # KEY A PRESSED
            
            if keys[pg.K_d]:
                self.moving_car1.rot.y -= 0.1 
                self.moving_car2.rot.y -= 0.1 
                self.moving_car3.rot.y -= 0.1    
                self.moving_car4.rot.y -= 0.1    
                self.moving_car5.rot.y -= 0.1    
                self.moving_car6.rot.y -= 0.1     
            
        else:
            self.moving_car1.pos = (self.app.camera.position[0], self.app.camera.position[1] - 21, self.app.camera.position[2]) 
            self.moving_car2.pos = (self.app.camera.position[0], self.app.camera.position[1] - 21, self.app.camera.position[2]) 
            self.moving_car3.pos = (self.app.camera.position[0], self.app.camera.position[1] - 21, self.app.camera.position[2]) 
            self.moving_car4.pos = (self.app.camera.position[0], self.app.camera.position[1] - 21, self.app.camera.position[2]) 
            self.moving_car5.pos = (self.app.camera.position[0], self.app.camera.position[1] - 21, self.app.camera.position[2]) 
            self.moving_car6.pos = (self.app.camera.position[0], self.app.camera.position[1] - 21, self.app.camera.position[2]) 

            self.RadioCube.pos= (self.app.camera.position[0] + 10, self.app.camera.position[1]-8, self.app.camera.position[2] + 6) 
            
         
 

        # self.moving_car1.rot.y = self.app.time
        # self.moving_car2.rot.y = self.app.time
        # self.moving_car3.rot.y = self.app.time
        # self.moving_car4.rot.y = self.app.time
        # self.moving_car5.rot.y = self.app.time
        # self.moving_car6.rot.y = self.app.time

        # self.moving_cube.rot.y = self.app.time