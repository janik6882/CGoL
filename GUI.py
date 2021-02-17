# pylint: disable=E1101
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import sys


# pygame.path.append("H:\documents\Informatik")
pygame.init()

width = 450  # input?
height = 1000

screen = pygame.display.set_mode((width, height))
pygame.display.init()
pygame.display.set_caption("Conways Game of Life Menu")  # Name des Tabs

# Schriftfont
font = pygame.font.SysFont('Constantia', 30)
# Farben
hg = (200, 200, 200)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


class button():
    """Docstring."""  # TODO: add docstring

    def __init__(self, x_koord, y_koord, text):
        """Docstring."""  # TODO: docstring hinzufügen
        self.clicked = False
        self.button_color = (25, 190, 225)
        self.hover_color = (75, 225, 255)
        self.click_color = (50, 150, 225)
        self.text_color = (255, 255, 255)
        self.width = 100
        self.height = 40
        self.x_koord = x_koord
        self.y_koord = y_koord
        self.text = text

    def draw_button(self):
        """Docstring."""   # TODO: add docstring
        action = False

        pos = pygame.mouse.get_pos()  # Mausposition

        button_rect = pygame.locals.Rect(self.x_koord, self.y_koord, self.width, self.height)

        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(screen, self.click_color, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked:
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, button_rect)
        else:
            pygame.draw.rect(screen, self.button_color, button_rect)

        # Schattierung
        pygame.draw.line(screen, white, (self.x_koord, self.y_koord), (self.x_koord + self.width, self.y_koord), 2)
        pygame.draw.line(screen, white, (self.x_koord, self.y_koord), (self.x_koord, self.y_koord + self.height), 2)
        pygame.draw.line(screen, black, (self.x_koord, self.y_koord + self.height), (self.x_koord + self.width, self.y_koord + self.height), 2)
        pygame.draw.line(screen, black, (self.x_koord + self.width, self.y_koord), (self.x_koord + self.width, self.y_koord + self.height), 2)

        # Text
        text_img = font.render(self.text, True, self.text_color)  # Text wird von pygame in ein img konvertiert
        text_len = text_img.get_width()  # wie lang der Text in der Mitte der Button (damit Text zentriert)
        screen.blit(text_img, (self.x_koord + int(self.width / 2) - int(text_len / 2), self.y_koord + 5))  # self.blit = Funtkion zum Anzeigen von Texten/Img
        return action


class Menu():
    def __init__(self):
        # Buttons:
        self.Play = button(20, 100, "Play")
        self.Pause = button(20, 150, "Pause")
        self.Save = button(325, 200, "Save")
        self.Load = button(325, 250, "Load")
        self.Rules = button(325, 150, "Rules")
        self.Forms = button(325, 100, "Forms")
        self.Manual = button(20, 200, "Manual")
        self.Auto = button(20, 250, "Auto")

    def mainloop(self):
        run = True
        while run:
            # screen.fill(hg) #Farbe des Bildschirms einstellen
            if self.Play.draw_button():
                print("Play")
            if self.Pause.draw_button():
                print("Pause")
            if self.Save.draw_button():
                print("Save")
            if self.Load.draw_button():
                print("Load")
            if self.Rules.draw_button():
                print("Rules")
            if self.Forms.draw_button():
                print("Forms")
            if self.Manual.draw_button():
                print("Manual")
            if self.Auto.draw_button():
                print("Auto")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


if __name__ == "__main__":
    test = Menu()
    test.mainloop()


#   while True:
#      if Play.draw_button():
#         print("Play")


# __main__()

# def fuer window size einstellen (options) und dann: def windowsize(width, height) und die werte als input vorher festgelegt
