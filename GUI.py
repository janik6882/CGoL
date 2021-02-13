import pygame
from pygame.locals import *

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

clicked = False


class button():  # Buttons erstellen
    button_color = (25, 190, 225)  # Farbcode RGB
    hover_color = (75, 225, 255)  # wenn man mit Maus drüber fährt
    click_color = (50, 150, 225)  # wenn clicked
    text_color = (255, 255, 255)
    width = 100
    height = 40

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        global clicked
        action = False

        pos = pygame.mouse.get_pos()  # Mausposition

        button_rect = Rect(self.x, self.y, self.width, self.height)  # Rechteck des Buttons; zum Gucken, ob die Maus rüberfährt

        if button_rect.collidepoint(pos):  # Maus auf Button?
            if pygame.mouse.get_pressed()[0] == 1:  # Maus gedrückt?
                clicked = True
                pygame.draw.rect(screen, self.click_color, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked is True:  # Wenn Maus gedrückt und losgelassen wird dann action true setzen und Aktion beginnen
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, button_rect)  # Wenn Maus nur drauf ist ohne gedrückt
        else:
            pygame.draw.rect(screen, self.button_color, button_rect)  # Wenn Maus nicht auf Button

        # Schattierung
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # Text
        text_img = font.render(self.text, True, self.text_color)  # Text wird von pygame in ein img konvertiert
        text_len = text_img.get_width()  # wie lang der Text in der Mitte der Button (damit Text zentriert)
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 5))  # self.blit = Funtkion zum Anzeigen von Texten/Img
        return action


# Buttons:
Play = button(20, 100, "Play")
Pause = button(20, 150, "Pause")
Save = button(325, 200, "Save")
Load = button(325, 250, "Load")
Rules = button(325, 150, "Rules")
Forms = button(325, 100, "Forms")  # Formen einfuegen
Manual = button(20, 200, "Manual")  # Manuell Zellen färben
Auto = button(20, 250, "Auto")  # Automatisch

run = True
while run:
    # screen.fill(hg) #Farbe des Bildschirms einstellen
    if Play.draw_button():
        print("Play")
    if Pause.draw_button():
        print("Pause")
    if Save.draw_button():
        print("Save")
    if Load.draw_button():
        print("Load")
    if Rules.draw_button():
        print("Rules")
    if Forms.draw_button():
        print("Forms")
    if Manual.draw_button():
        print("Manual")
    if Auto.draw_button():
        print("Auto")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()


#   while True:
#      if Play.draw_button():
#         print("Play")


# __main__()

# def fuer window size einstellen (options) und dann: def windowsize(width, height) und die werte als input vorher festgelegt
