import os
import pygame
import sys
from menu_system.button import Button
from programs.test_window import GraphicsEngine

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pygame.init()

info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Menu")

# Construye la ruta de la imagen de fondo
BG_PATH = os.path.join(BASE_DIR, 'assets', 'main_menu_bg3.png')
BG = pygame.image.load(BG_PATH)

BG = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))


def get_font(size):  # Returns Press-Start-2P in the desired size
    font_path = os.path.join(BASE_DIR, 'assets', 'social.otf')
    return pygame.font.Font(font_path, size)

def play():
    app = GraphicsEngine()
    app.Run()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

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

        PLAY_BUTTON = Button(image=None, pos=(SCREEN.get_width()/2, SCREEN.get_height()/2 + 150 ), 
                            text_input="PLAY", font=get_font(100), base_color="White", hovering_color="Pink")

        gear_img_path = os.path.join(BASE_DIR, 'assets', 'gear2.png')
        OPTIONS_BUTTON = Button(image=pygame.image.load(gear_img_path), pos=(SCREEN.get_width() - 70, SCREEN.get_height() - 70), 
                            text_input="", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=None, pos=(120, SCREEN.get_height() - 70), 
                            text_input="QUIT", font=get_font(75), base_color="White", hovering_color="Red")

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
