import pygame, sys, os
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
#Fondo del menu
BG = pygame.image.load("assets/Background.png")
#Musica de fondo


music_path = os.path.join(os.path.dirname(__file__), 'Musica', 'Nightcall.mp3')
if os.path.exists(music_path):
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)
else:
    print(f"Error: No se encontró el archivo de música en {music_path}")

"""#Iconos del control de volumen
sonido_arriba = pygame.image.load('Menu(para_pg)/Musica/iconos/sube-el-volumen.png')
sonido_abajo = pygame.image.load('Menu(para_pg)/Musica/iconos/bajar-volumen.png')
sonido_mute = pygame.image.load('Menu(para_pg)/Musica/iconos/silenciar.png')
sonido_max = pygame.image.load('Menu(para_pg)/Musica/iconos/altoparlante.png')
#Funcion de control de volumen9
def Volumen():
    keys = pygame.key.get_pressed()  # Para el monitoreo del volumen

    # Baja volumen
    if keys[pygame.K_9] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
        # SCREEN.blit(sonido_abajo, (850, 25))
    elif keys[pygame.K_9] and pygame.mixer.music.get_volume() == 0.0:
        # SCREEN.blit(sonido_mute, (850, 25))

    # Sube volumen
    if keys[pygame.K_0] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        # SCREEN.blit(sonido_arriba, (850, 25))
    elif keys[pygame.K_0] and pygame.mixer.music.get_volume() == 1.0:
        # SCREEN.blit(sonido_max, (850, 25))

    # Desactivar sonido
    if keys[pygame.K_m]:
        pygame.mixer.music.set_volume(0.0)
        # SCREEN.blit(sonido_mute, (850, 25))

    # Reactivar sonido
    if keys[pygame.K_COMMA]:
        pygame.mixer.music.set_volume(1.0)
        # SCREEN.blit(sonido_max, (850, 25))"""

def get_font(size): # Returns Press-Start-2P in the desired size
   #Letras
   return pygame.font.Font("assets/font2.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("Animación.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(1220, 695), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
        #Volumen() 
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Configuración.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(1220, 695), 
                            text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        #Volumen() 
        pygame.display.update()
def MAP():
    while True:
        MAP_MOUSE_POS = pygame.mouse.get_pos()
        pygame.image.load("assets/Background.png")
        OPTIONS_MAP = Button(image=None, pos=(1220, 695), 
                             text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")
        OPTIONS_MAP.changeColor(MAP_MOUSE_POS)
        OPTIONS_MAP.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  OPTIONS_MAP.checkForInput(MAP_MOUSE_POS):
                    main_menu()
      
def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(150, 350), 
                            text_input="PLAY", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        MAP_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"),pos=(650,260),
                            text_input="MAPAS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(150, 466), 
                            text_input="OPTIONS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(150, 580), 
                            text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        #Volumen()    
        pygame.display.update()

main_menu()