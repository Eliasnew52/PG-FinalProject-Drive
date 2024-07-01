import glm
import pygame as pg
from SoundEngine import AudioEngine

FOV = 60  # deg
NEAR = 1
FAR = 10000
SPEED = .1
SENSITIVITY = 0.1



class RayCast_Camera:
    def __init__(self, app, position=(613, 64, -467), yaw=-360, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        #movement parameters
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch

        self.x = 0
        self.z = 0
        self.Limits_x = glm.vec2(7500, 40)
        self.Limits_z =glm.vec2(-30, -7500) 

        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()
        
        self.Engine = False
        self.Radio = False  
        
    def get_position(self):
        return self.position
    
    def get_ray_from_mouse(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        ndc_x = (2.0 * mouse_x) / self.app.WIN_SIZE[0] - 1.0
        ndc_y = 1.0 - (2.0 * mouse_y) / self.app.WIN_SIZE[1]
    
        ray_ndc = glm.vec4(ndc_x, ndc_y, -1.0, 1.0)
        ray_clip = glm.vec4(ray_ndc.x, ray_ndc.y, -1.0, 1.0)
        ray_eye = glm.inverse(self.m_proj) * ray_clip
        ray_eye = glm.vec4(ray_eye.x, ray_eye.y, -1.0, 0.0)
        ray_world = glm.inverse(self.m_view) * ray_eye
        ray_world = glm.vec3(ray_world.x, ray_world.y, ray_world.z)
        ray_world = glm.normalize(ray_world)
    
        return ray_world

    
    def ray_intersects_aabb(self, ray_origin, ray_direction, aabb_min, aabb_max):
        t_min = (aabb_min - ray_origin) / ray_direction
        t_max = (aabb_max - ray_origin) / ray_direction
        t1 = glm.min(t_min, t_max)
        t2 = glm.max(t_min, t_max)
        t_near = glm.max(glm.max(t1.x, t1.y), t1.z)
        t_far = glm.min(glm.min(t2.x, t2.y), t2.z)
        return t_far >= t_near

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def get_dynamic_aabbs_max(self):
        aabbs_max = []
        for obj in self.app.scene.objects:
        # Agrega el AABB máximo para cada objeto
            aabbs_max.append(glm.vec3(obj.pos[0] + 1, obj.pos[1] + 1, obj.pos[2] + 1))
        return aabbs_max

    def get_dynamic_aabbs_min(self):
        aabbs_min = []
        for obj in self.app.scene.objects:
        # Agrega el AABB mínimo para cada objeto
            aabbs_min.append(glm.vec3(obj.pos[0] - 1, obj.pos[1] - 1, obj.pos[2] - 1))
        return aabbs_min

            
    
    def update(self):
        keys = pg.key.get_pressed()
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()
        ray_origin = self.position
        ray_direction = self.get_ray_from_mouse()
        aabb_max = self.get_dynamic_aabbs_max()
        aabb_min = self.get_dynamic_aabbs_min()

        #Logica del Raycast - Actualmente Config para MAnipular Musica con cualquier interseccion
        #Para la Radio es el indice[6] de los aabbs
        
        intersected = False
        idle_channel = None
        
        for i in range(len(aabb_min)):
            if self.ray_intersects_aabb(ray_origin, ray_direction, aabb_min[i], aabb_max[i]):
                intersected = True
                break
        
        #Engine Startup
        if intersected and keys[pg.K_e] == 1 and not self.Engine:
            idle_channel = AudioEngine.EngineStartup()
            self.Engine = True


        #Engine Stop
        elif intersected and keys[pg.K_q] == 1 and self.Engine:
            AudioEngine.StopEngineIdle(idle_channel)
            self.Engine = False


    def pls_rotate(self, yaw_offset, pitch_offset):
        self.yaw += yaw_offset
        self.pitch += pitch_offset
        self.update_camera_vectors()

    def move(self):
        
        # velocity = SPEED * self.app.delta_time
        # keys = pg.key.get_pressed()
        
        # # Forward and Back Buttons
        # # KEY W PRESSED
        # if keys[pg.K_w]:
        #     self.position += self.forward * velocity
        # # KEY S PRESSED
        # if keys[pg.K_s]:
        #     self.position -= self.forward * velocity

        #Right and Left Buttons
        # KEY D PRESSED
        # if keys[pg.K_d]:
        #     self.position += self.right * velocity
        # # KEY A PRESSED
        # if keys[pg.K_a]:
        #     self.position -= self.right * velocity
        
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.z = self.position[2] + self.forward[2] * velocity
            self.x = self.position[0] + self.forward[0] * velocity
        
            if self.Limits_z[0] > self.z > self.Limits_z[1] and self.Limits_x[0] > self.x > self.Limits_x[1] :
                self.position[2] = self.z
                self.position[0] = self.x
        if keys[pg.K_s]:
            self.z = self.position[2] - self.forward[2] * velocity
            self.x = self.position[0] - self.forward[0] * velocity
        
            if self.Limits_z[1] < self.z < self.Limits_z[0] and self.Limits_x[1] < self.x < self.Limits_x[0] :
                self.position[2] = self.z
                self.position[0] = self.x
        # if keys[pg.K_a]:
        #     self.x = self.position[0] - self.right[0] * velocity
        #     self.z = self.position[2] - self.right[2] * velocity
        
        #     if self.Limits_x[1] < self.x < self.Limits_x[0] and self.Limits_z[1] < self.z < self.Limits_z[0] :
        #         self.position[0] = self.x
        #         self.position[2] = self.z
        # if keys[pg.K_d]:
        #     self.x = self.position[0] + self.right[0] * velocity
        #     self.z = self.position[2] + self.right[2] * velocity
        
        #     if self.Limits_x[0] > self.x > self.Limits_x[1] and self.Limits_z[0] > self.z > self.Limits_z[1] :
        #         self.position[0] = self.x
        #         self.position[2] = self.z
        if keys[pg.K_g]:
            print(self.position)
        
       

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
