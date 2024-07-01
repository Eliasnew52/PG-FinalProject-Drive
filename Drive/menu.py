import pygame, sys
from button import Button
import os

from main import GraphicsEngine


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pygame.init()

pygame.display.set_caption("Menu")

BG_PATH = os.path.join(BASE_DIR, 'assets', 'bg.jpg')
BG = pygame.image.load(BG_PATH)

info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

def get_font(size): # Returns Press-Start-2P in the desired size
   return pygame.font.Font("assets/social.otf", size)


def Run(map):
    app = GraphicsEngine(map)
    app.run()

def play():
    while True:
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        BG_PATH = os.path.join(BASE_DIR, 'assets', 'bck.png')
        BG = pygame.image.load(BG_PATH)

        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        

        SCREEN.blit(BG,(0,0))
        
        VICE = Button(image=pygame.image.load("assets/vice.jpg"), pos=(SCREEN.get_width()/2 - 400, SCREEN.get_height()/2 - 50), 
                            text_input="", font=get_font(200), base_color="White", hovering_color="Pink")
        LIBERTY = Button(image=pygame.image.load("assets/liberty.jpg"), pos=(SCREEN.get_width()/2, SCREEN.get_height()/2 - 50), 
                            text_input="", font=get_font(200), base_color="White", hovering_color="Pink")
        SA = Button(image=pygame.image.load("assets/sa.jpg"), pos=(SCREEN.get_width()/2 + 400, SCREEN.get_height()/2 - 50), 
                            text_input="", font=get_font(200), base_color="White", hovering_color="Pink")
                

        PLAY_BUTTON = Button(image=None, pos=(SCREEN.get_width()/2, SCREEN.get_height() - 800 ), 
                            text_input="SELECT A MAP", font=get_font(100), base_color="White", hovering_color="Pink")

        QUIT_BUTTON = Button(image=None, pos=(120, SCREEN.get_height() - 70), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Red")

        for button in [PLAY_BUTTON, QUIT_BUTTON, VICE, LIBERTY, SA]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if VICE.checkForInput(MENU_MOUSE_POS):
                    Run(1)
                if LIBERTY.checkForInput(MENU_MOUSE_POS):
                    Run(2)
                if SA.checkForInput(MENU_MOUSE_POS):
                    Run(3)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                    sys.exit()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        BG_PATH = os.path.join(BASE_DIR, 'assets', 'credits.jpeg')
        BG = pygame.image.load(BG_PATH)

        BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))

        SCREEN.blit(BG,(0,0))
        
        tinoco_text = get_font(45).render("Eliezer Tinoco", True, "White")
        tinoco_opt = tinoco_text.get_rect(center=(  SCREEN.get_width()/2 - 600,   SCREEN.get_height()/2 + 200))
        tinoco_user_text = get_font(20).render("EliezerT", True, "Black")
        tinoco_user_text_opt = tinoco_user_text.get_rect(center=(  SCREEN.get_width()/2 - 600,   SCREEN.get_height()/2 + 240))

        ernesto_text = get_font(45).render("Ernesto Vargas", True, "White")
        ernesto_opt = ernesto_text.get_rect(center=(  SCREEN.get_width()/2 - 200,   SCREEN.get_height()/2 + 200))
        ernesto_user_text = get_font(20).render("xSarscov", True, "Pink")
        ernesto_user_text_opt = ernesto_user_text.get_rect(center=(  SCREEN.get_width()/2 - 200,   SCREEN.get_height()/2 + 240))
        
        
        elias_text = get_font(45).render("Elías Castillo", True, "White")
        elias_opt = elias_text.get_rect(center=(  SCREEN.get_width()/2 + 200,   SCREEN.get_height()/2 + 200))
        
        elias_user_text = get_font(20).render("Eliasnew52", True, "Pink")
        elias_user_text_opt = elias_user_text.get_rect(center=(  SCREEN.get_width()/2 + 200,   SCREEN.get_height()/2 + 240))
        
        enghell_text = get_font(45).render("Enghell Zelaya", True, "White")
        enghell_opt = enghell_text.get_rect(center=(  SCREEN.get_width()/2 + 600,   SCREEN.get_height()/2 + 200))
        
        enghell_user_text = get_font(20).render("Enghell27", True, "Black")
        enghell_user_text_opt = enghell_user_text.get_rect(center=(  SCREEN.get_width()/2 + 600,   SCREEN.get_height()/2 + 240))
        
        SCREEN.blit(tinoco_text, tinoco_opt)
        SCREEN.blit(ernesto_text, ernesto_opt)
        SCREEN.blit(elias_text, elias_opt)
        SCREEN.blit(enghell_text, enghell_opt)
        
        SCREEN.blit(tinoco_user_text, tinoco_user_text_opt)
        SCREEN.blit(ernesto_user_text, ernesto_user_text_opt)
        SCREEN.blit(elias_user_text, elias_user_text_opt)
        SCREEN.blit(enghell_user_text, enghell_user_text_opt)

        OPTIONS_BACK = Button(image=None, pos=(SCREEN.get_width() - 70, SCREEN.get_height() - 30), 
                            text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Red")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(SCREEN.get_width()/2, SCREEN.get_height()/2 + 100), 
                            text_input="PLAY", font=get_font(70), base_color="White", hovering_color="#DE3163")

        OPTIONS_BUTTON = Button(image=None, pos=(SCREEN.get_width() - 150, SCREEN.get_height() - 40), 
                            text_input="CREDITS", font=get_font(75), base_color="White", hovering_color="Pink")
        QUIT_BUTTON = Button(image=None, pos=(90, SCREEN.get_height() - 40), 
                            text_input="QUIT", font=get_font(75), base_color="White", hovering_color="Red")
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

        pygame.display.update()

main_menu()
