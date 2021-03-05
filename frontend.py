"""Projekt des Informatik LK."""
# pylint: disable=E1101
# pylint: disable=C0301
import sys
import pygame
# from pygame.locals import *
import json
from backend import Game
from tkinter.filedialog import asksaveasfilename, askopenfile
from tkinter import Button, Label, Tk


class Display:  # Zu Display ändern
    """Display Klasse.

    Klasse erstellt ein Pygame Display und ersellt eine Instanz von dem aus
    backend.py importiertem game.
    """

    def __init__(self, master, windowX: int, windowY: int, nodes=None):
        """Init Klasse.

        Kommentar: Konstrukter der Klasse display()
        Input: Name der Klasse, x-Größe des Bildschirms, y-Größe des
               Bildschirms, optional: knotenliste
        Output: Kein Output
        Besonders: Erstellt ein pygame display, erstellt eine Instanz der
                   game() klasse
        """

        self.master = master
        master.geometry("250x250")

        master.title("Conways Game of Life")

        self.label = Label(master, text="Start Menu")
        self.label.grid(row=0, column=0, columnspan=2, sticky='ew')

        self.play_button = Button(master, text="Play")
        self.play_button.grid(row=1, column=0, sticky='ew')

        self.pause_button = Button(master, text="Pause")
        self.pause_button.grid(row=2, column=0, sticky='ew')

        self.save_button = Button(master, text="Save", command=lambda: Display.save_file())
        self.save_button.grid(row=3, column=0, sticky='ew')

        self.load_button = Button(master, text="Load", command=lambda: Display.open_file())
        self.load_button.grid(row=4, column=0, sticky='ew')

        self.rules_button = Button(master, text="Rules")
        self.rules_button.grid(row=1, column=1, sticky='ew')

        self.forms_button = Button(master, text="Forms")
        self.forms_button.grid(row=2, column=1, sticky='ew')

        self.manual_button = Button(master, text="Manual")
        self.manual_button.grid(row=3, column=1, sticky='ew')

        self.auto_button = Button(master, text="Auto")
        self.auto_button.grid(row=4, column=1, sticky='ew')

        self.master.columnconfigure(0, weight=1, uniform="commi")
        self.master.columnconfigure(1, weight=1, uniform="commi")
        self.master.rowconfigure(1, weight=1, uniform="commi")
        self.master.rowconfigure(2, weight=1, uniform="commi")
        self.master.rowconfigure(3, weight=1, uniform="commi")
        self.master.rowconfigure(4, weight=1, uniform="commi")

        nodes = nodes or []
        self.window_x = windowX
        self.window_y = windowY
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (173, 173, 173)
        board_size_x = self.window_x // 10
        board_size_y = self.window_y // 10
        self.game = Game(nodes=nodes, board_x=board_size_x, board_y=board_size_y)  # noqa: E501
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
        for x_koord in range(0, self.window_x, 10):
            start_x = x_koord
            start_y = 0
            end_x = x_koord
            end_y = self.window_y
            start = (start_x, start_y)
            end = (end_x, end_y)
            pygame.draw.line(self.display, self.grey, start, end, width=1)
        for y_koord in range(0, self.window_y, 10):
            start_x = 0
            start_y = y_koord
            end_x = self.window_x
            end_y = y_koord
            start = (start_x, start_y)
            end = (end_x, end_y)
            pygame.draw.line(self.display, self.grey, start, end, width=1)

    def show_board(self, points: list):
        """Zeigt das Bord an.

        Kommentar: Erzeugt die Punkte auf dem Bord
        Input: Name der Instanz, punkte
        Output: Kein Output
        Besonders: Aktualisiert das Bord
        """
        self.clear_board()
        for point in points:
            x_koord = (point[0] * 10) + 1
            y_koord = (point[1] * 10) + 1
            pygame.draw.rect(self.display, self.black, pygame.Rect(y_koord, x_koord, 9, 9))  # noqa: E501
        Display.update_board()

    def manipulate_point(self, pos_x: int, pos_y: int):
        """Manipulierung eines Punktes.

        Kommentar: Manipuliert einen Punkt (hinzufuegen wenn keiner vorhanden,
                   entfernen wenn Punhkt vorhanden)
        Input: Name der Instanz, x-Position des Klicks, y-Position des Klicks
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        node_x = pos_x // 10
        node_y = pos_y // 10
        exist = self.game.manipulate_point(node_x, node_y)
        point_x = (node_x * 10) + 1
        point_y = (node_y * 10) + 1
        if exist:
            pygame.draw.rect(self.display, self.black, pygame.Rect(point_y, point_x, 9, 9))  # noqa: E501
        else:
            pygame.draw.rect(self.display, self.white, pygame.Rect(point_y, point_x, 9, 9))  # noqa: E501

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
                    Display.update_board()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        return "f"  # TODO: entfernen, dient nur debug zwecken
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
            Display.check_close()

    @classmethod
    def check_close(cls):
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

    @classmethod
    def update_board(cls):
        """Aktualisiert das Bord.

        Kommentar: Bord wird durch den Flip befehl aktualisiert
        Input: Name der Instanz
        Output: Keine Output
        Besonders: Keine Besonderheiten
        """
        pygame.display.flip()

    @classmethod
    def open_file(cls):
        """Lädt Daten aus einer Datei mit file browser.

        Kommentar: Lädt daten aus einer Datei
        Input: Name der Klasse
        Output: Geladene Daten
        Besonders: Nutzt tkinter lade-Modul, beliebiger Speicherort.
        """
        file = askopenfile(mode='r', filetypes=[('Json files', '*.json')])
        if file is not None:
            inhalt = file.read()
        return inhalt

    @classmethod
    def save_file(cls, inhalt):
        """Speichert gegebene Daten in eine Datei mit file browser.

        Kommentar: Speichert Daten in eine Datei
        Input: Name der Klasse, Daten
        Output: Kein Output
        Besonders: Nutzt tkinter speicher-Modul, beliebiger Dateiort.
        """
        filename = asksaveasfilename(
            filetypes=[('JSON files', '.json')], initialfile=''
        )
        if filename:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(inhalt, file)


def main():
    """Funktion zum testen."""
    glider_top_left = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 5], [3, 5],
                       [4, 1], [4, 4]]
    test = Display(1000, 1000, glider_top_left)
    print(test.game.list_premade())
    test.game.add_premade("Middle-weight spaceship", 5, 5)
    test.mainloop()


def debug():
    """Funktion zum Debugging."""
    root = Tk()
    fenster = Display(root, 0, 0)
    root.mainloop()


if __name__ == '__main__':
    debug()
    # main()
