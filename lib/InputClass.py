import pygame


class Input:
    """Klasse für ein Input Feld"""

    def __init__(self, x, y, width, hight, screen, text='', mode=''):
        """Init Methode für Input Klasse

        Kommentar: Standard Init Methode
        Input: Name der Instanz, x, y, breite, höhe, display optional: text, modus
        Output: Kein Direktes Output
        Besonders: Keine Besonderheiten
        """
        self.x = x
        self.y = y
        self.hight = hight
        self.width = width
        self.origin_width = width
        self.rect = pygame.Rect(self.x, self.y, width, hight)
        self.font = pygame.font.Font(None, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('midnightblue')
        self.color = self.color_inactive
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.active = False
        self.screen = screen
        self.mode = mode
        self.update()

    def change_state(self):
        """Verändert status und Farbe

        Kommentar: Verändert den Status von active auf das invertierte
        Input: Name der Instanz
        Output: Gibt return der Mainloop zurück
        Besonders: Keine Besonderheiten
        """
        self.active = not self.active
        self.color = self.color_active if self.active else self.color_inactive
        self.update()
        if self.active:
            return self.mainloop()

    def change_text(self, text):
        """Verändert den text zum Input und aktualisiert den Text."""
        self.text = text
        self.update()

    def update(self):
        """Aktualisiert das Input Fenster und dessen Inhalt."""
        self.text_surface = self.font.render(self.text, True, self.color)
        width = max(self.origin_width, self.text_surface.get_width() + 10)
        pygame.draw.rect(self.screen, pygame.Color('white'),
                         pygame.Rect(self.x, self.y, max(width, self.width + 10), self.hight + 10))
        if width + 10 + self.x < self.screen.get_size()[0]:
            self.rect.width = width
            self.width = self.rect.width
        else:
            self.change_text(self.text[:-1])
        self.draw()

    def draw(self):
        """Zeichnet die Box für das Input-Feld."""
        self.screen.blit(self.text_surface, (self.x + 5, self.y + 5))
        pygame.draw.rect(self.screen, self.color, self.rect, 2)
        pygame.display.flip()

    def mainloop(self):
        while self.active:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.change_text(self.text[:-1])
                    elif event.key == pygame.K_ESCAPE:
                        self.change_text('')
                        self.change_state()
                    elif event.key == pygame.K_RETURN:
                        self.change_state()
                        return True
                    else:
                        if event.unicode.isnumeric() or self.mode != 'int':
                            self.change_text(self.text + event.unicode)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pos_x = pos[1]
                    pos_y = pos[0]
                    if self.rect.collidepoint(pos_y, pos_x) == False:
                        self.change_state()
