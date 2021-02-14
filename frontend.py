"""Docstring tba."""  # TODO: Add docustring
import sys
import pygame
# from pygame.locals import *
from backend import game


class Display():  # Zu Display ändern
    """Display Klasse.

    Klasse erstellt ein Pygame Display und ersellt eine Instanz von dem aus
    backend.py importiertem game.
    """

    def __init__(self, windowX, windowY, nodes=None):
        """Init Klasse.

        Kommentar: Konstrukter der Klasse display()
        Input: Name der Klasse, x-Größe des Bildschirms, y-Größe des
               Bildschirms, optional: knotenliste
        Output: Kein Output
        Besonders: Erstellt ein pygame display, erstellt eine Instanz der
                   game() klasse
        """
        nodes = nodes or []
        self.window_x = windowX
        self.window_y = windowY
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (173, 173, 173)
        board_size_x = self.window_x//10
        board_size_y = self.window_y//10
        self.game = game(nodes=nodes, boardX=board_size_x, boardY=board_size_y)
        self.display = pygame.display.set_mode((self.window_x, self.window_y))

    def clear_board(self):
        """Entfernt alle Objekte vom Bord.

        Kommentar: leert das Bord und erzeugt ein Gitter
        Input: Name der Instanz
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        self.display.fill(self.white)
        self.draw_grid()

    def draw_grid(self):
        """Zeichnet ein Gitter.

        Kommentar: erzeugt ein Gitter auf der GUI
        Input: Name der Instanz
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        for x in range(0, self.window_x, 10):  # Snake Case beenden
            start_x = x
            start_y = 0
            end_x = x
            end_y = self.window_y
            start = (start_x, start_y)
            end = (end_x, end_y)
            pygame.draw.line(self.display, self.grey, start, end, width=1)
        for y in range(0, self.window_y, 10):  # Snake Case beenden
            start_x = 0
            start_y = y
            end_x = self.window_x
            end_y = y
            start = (start_x, start_y)
            end = (end_x, end_y)
            pygame.draw.line(self.display, self.grey, start, end, width=1)

    def update_board(self):  # R0201 beheben?
        """Aktualisiert das Bord.

        Kommentar: Bord wird durch den Flip befehl aktualisiert
        Input: Name der Instanz
        Output: Keine Output
        Besonders: Keine Besonderheiten
        """
        pygame.display.flip()

    def show_board(self, points):
        """Zeigt das Bord an.

        Kommentar: Erzeugt die Punkte auf dem Bord
        Input: Name der Instanz, punkte
        Output: Kein Output
        Besonders: Aktualisiert das Bord
        """
        self.clear_board()
        for point in points:
            x = (point[0]*10)+1
            y = (point[1]*10)+1
            pygame.draw.rect(self.display, self.black, pygame.Rect(y, x, 9, 9))
        self.update_board()

    def check_close(self):  # R0201 beheben?
        """Prüft, ob Close Button aktiviert wurde.

        Kommentar: Überprüft, ob der Close button aktiviert wurde
        Input: Name der Instanz
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def manipulate_point(self, posX, posY):
        """Manipulierung eines Punktes.

        Kommentar: Manipuliert einen Punkt (hinzufuegen wenn keiner vorhanden,
                   entfernen wenn Punhkt vorhanden)
        Input: Name der Instanz, x-Position des Klicks, y-Position des Klicks
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        nodeX = posX//10
        nodeY = posY//10
        exist = self.game.manipulate_point(nodeX, nodeY)
        point_x = (nodeX*10)+1
        point_y = (nodeY*10)+1
        if exist:
            pygame.draw.rect(self.display, self.black, pygame.Rect(point_y, point_x, 9, 9))
        else:
            pygame.draw.rect(self.display, self.white, pygame.Rect(point_y, point_x, 9, 9))

    def wait_keypress(self):
        """Wartet auf einen Tastendruck.

        Kommentar: wartet auf einen Tastendruck und führt entsprechende Befehle
                   aus
        Input: Name der Instanz
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pos_x = pos[1]
                    pos_y = pos[0]
                    self.manipulate_point(pos_x, pos_y)
                    # self.game.add_point(nodeX, nodeY)
                    self.update_board()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        return "f"
                    if event.key == pygame.K_e:
                        self.game.export_current()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def mainloop(self):
        """Mainloop, läuft bis beendet.

        Kommentar: Mainloop, läuft bis programm beendet wird
        Input: Name der Instanz
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        while True:
            points = self.game.get_points()
            self.show_board(points)
            self.wait_keypress()
            self.game.next_board()
            self.check_close()


def main():
    """Funktion zum testen."""
    glider_top_left = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 5], [3, 5], [4, 1], [4, 4]]
    test = Display(1000, 1000, [])
    print(test.game.list_premade())
    test.game.add_premade("Middle-weight spaceship", 5, 5)
    test.mainloop()


def debug():
    """Funktion zum Debugging."""
    glider_top_left = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 5], [3, 5], [4, 1], [4, 4]]
    test = Display(1000, 1000, glider_top_left)
    test.mainloop()


if __name__ == '__main__':
    # debug()
    main()
