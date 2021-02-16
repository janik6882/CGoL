# -*- coding: utf-8 -*-
"""Docstring beenden."""
import time
import json
import os
from typing import List
# Vorerst Datei fuer alles Backend stuff.


class Game():
    """Game Klasse, für Backend benutzt."""

    def __init__(self, nodes=None, board_x=30, board_y=30, premade=None) -> None:  # noqa: E501
        """Init Methode.

        Kommentar: Standard init Methode
        Input: Name der Instanz, optional: nodes--(siehe docs), boardX--Breite
               der Simulation, boardY--höhe der Simulation
        Output: Kein Output
        Besonders: Standard init, nichts Besonderes
        """
        nodes = nodes or list()
        premade = premade or dict()
        self.nodes = nodes
        self.board_x = board_x
        self.board_y = board_y
        if premade:
            self.premade = premade
        else:
            self.premade = {}
            self.premade = self.import_premade()

    def get_num_neighbours(self, x_koord: int, y_koord: int) -> int:
        """Gibt die Anzahl der Nachbarn zurück.

        Kommentar: gibt die Anzahl der Nachbarn als int aus
        Input: Name der Instanz, x-Koordinate, y-Koordinate
        Output: Int mit anzahl der Nachbarn
        Besonders: keine Besonderheiten
        """
        nachbar_zellen = [[x_koord-1, y_koord-1], [x_koord-1, y_koord],
                          [x_koord-1, y_koord+1], [x_koord, y_koord-1],
                          [x_koord, y_koord+1], [x_koord+1, y_koord-1],
                          [x_koord+1, y_koord], [x_koord+1, y_koord+1]]
        # setzen der Nachbarn zur länge der Überschneidung von nachbar_zellen
        #  und self.nodes (Knotenliste)
        num_nachbarn = len(Game.get_list_intersection(nachbar_zellen, self.nodes))  # noqa: E501
        return num_nachbarn

    def check_regeln(self, x_koord: int, y_koord: int) -> bool:
        """Überprüft die Regeln des CGoL.

        Kommentar: gibt aus, ob an der Position von Zelle eine Zelle erstellt
                    wird in der nächsten Iteration
        Input: Name der Instanz, x-Koordinate, y-Koordinate
        Output: False, wenn keine Zelle, True wenn Zelle in der nächsten
                Iteration
        Besonders: nutzt get_num_neighbours()
        """
        zelle = [x_koord, y_koord]
        num_nachbarn = self.get_num_neighbours(x_koord, y_koord)
        if zelle in self.nodes:
            return bool(num_nachbarn in [2, 3])
        else:
            return bool(num_nachbarn == 3)

    def next_board(self) -> list:
        """Erzeugt das nächste Bord und gibt dieses zurück.

        Kommentar:erzeugt das neue board und ersetzt das Aktuelle mit dem neuen
        Input: name der Instanz
        Output: aktualisierte Knotenliste
        Besonders: nutzt check_regeln
        """
        new_board = []
        nachbarn: List[List[int]] = list()
        nodes = self.nodes
        for node in nodes:  # loop durch alle elemente von self.nodes
            x_koord = node[0]  # setzt x zur x-koordinate von node
            y_koord = node[1]  # setzt y zur y-koordinate von node
            nachbar_zellen = [[x_koord-1, y_koord-1], [x_koord-1, y_koord],
                              [x_koord-1, y_koord+1], [x_koord, y_koord-1],
                              [x_koord, y_koord+1], [x_koord+1, y_koord-1],
                              [x_koord+1, y_koord], [x_koord+1, y_koord+1]]
            for zelle in nachbar_zellen:  # loop durch alle nachbar_zellen
                if zelle not in nachbarn + nodes:  # wenn zelle nicht nodes und
                    # nachbarn
                    nachbarn.append(zelle)
            if self.check_regeln(node[0], node[1]):
                new_board.append(node)
        for nachbar in nachbarn:  # loop durch nachbarn
            if self.check_regeln(nachbar[0], nachbar[1]):
                new_board.append(nachbar)
        self.nodes = new_board  # ersetzen der Knotenliste mit der neuen Liste
        return new_board

    def get_points(self) -> list:
        """Gibt die Knotenliste zurück.

        Kommentar: gibt die aktuelle Knotenliste aus
        Input: Name der Instanz
        Output: Knotenliste self.node
        Besonders: Rückgabe mittels return
        """
        return self.nodes

    def add_point(self, x_koord: int, y_koord: int) -> list:
        """Fügt einen Punkt zur Knotenliste hinzu.

        Kommentar: Fuegt einen Punkt zur Knotenliste self.nodes hinzu
        Input: name der Instanz, x-Koordinate als int, y-Koordinate als int
        Output: Aktualisierte Knotenliste self.nodes
        Besonders: Weitere Optimierung der Laufzeit
        """
        # TODO: Verhalten besprechen, wenn punkt bereits in Knotenliste
        # OPTIMIZE: Laufzeit optimieren (add, append oder operator?)
        self.nodes.append([x_koord, y_koord])
        return self.nodes

    def remove_point(self, x_koord, y_koord):
        """Entfernt einen Punkt aus der Knotenliste.

        Kommentar: Entfernt einen Punkt aus der Knotenliste
        Input: Name der Instanz, x-Koordinate als int, y-Koordinate als int
        Output: Aktualisierte Knotenliste self.nodes
        Besonders: Falls Punkt nicht in Knotenliste erfolgt Error
        """
        # OPTIMIZE: Laufzeit?
        # DEBUG: Try except pruefen
        if [x_koord, y_koord] in self.nodes:
            self.nodes.remove([x_koord, y_koord])
            return self.nodes
        else:
            # Ausgabe besprechen
            return "error"

    def manipulate_point(self, x_koord: int, y_koord: int) -> bool:
        """Siehe Kommentar.

        Kommentar: Fuegt Punkt hinzu, wenn nicht vorhanden, entfernt wenn
                   vorhanden
        Input: Name der Instanz, x-Koordinate als int, y-Koordinate als int
        Output: Aktualisierte Knotenliste
        Besonders: Prueft ob Punkt in Knotenliste
        """
        if [x_koord, y_koord] in self.nodes:
            self.remove_point(x_koord, y_koord)
            res = False
        else:
            self.add_point(x_koord, y_koord)
            res = True
        return res

    def get_matrix(self) -> list:
        """Erzeugt einen Matrix aus der Knotenliste.

        Kommentar: gibt eine Matrix aus, welche alle Punkte beinhaltet
        Input: name der Instanz
        Output: Matrix mit allen Punkten, eine Reihe entspricht einer Liste
        Besonders: Keine Besonderheiten
        """
        matrix = Game.__gen_matrix(self.board_x, self.board_y)
        points = self.nodes
        for node in points:
            matrix[node[1]][node[0]] = 1
        return matrix

    def export_current(self) -> None:
        """Docsring."""  # TODO: add docu
        export = dict()
        export["boardX"] = self.board_x
        export["boardY"] = self.board_y
        export["nodes"] = self.nodes
        Game.daten_speichern(export, "out.json")
        return None

    def list_premade(self) -> list:
        """Listet alle vorgefertigten Objekte auf.

        Kommentar: listet alle vorgefertigten Objekte mit deren Namen auf
        Input: Name der Instanz
        Output: Liste mit allen Namen
        Besonders: Keine Besonderheiten
        """
        res = list()
        for name in list(self.premade.keys()):
            res.append(name)
        return res

    def import_premade(self, filename=None) -> dict:
        """Importiert vorgefertigte Elemente aus einer Datei.

        Kommentar: Importiert vorgefertigte Objekte aus einer Json datei
        Input: Name der Instanz, Optional: Dateiname
        Output: vorgefertigte Dateien, werden aber automatisch zu self.premade
                hinzugefuegt
        Besonders: Wenn kein Dateiname gegeben, wird die standard datei genutzt
        """
        if filename:
            data = Game.load_premade(filename)
        else:
            pth = os.path.join("premade", "premade.json")
            data = Game.load_premade(pth)
        self.premade = Game.merge_dict(self.premade, data)
        return data

    def add_premade(self, name: str, pos_x: int, pos_y: int) -> None:
        """Fügt ein vorgefertigtes Element zur Knotenliste hinzu.

        Kommentar: fuegt an einer gegebenen Position ein vorgefertigtes Objekt
                   anhand dessen Namen hinzu
        Input: Name der Instanz, Name des Objekts, x-Koordinate, y-Koordinate
        Output: Kein Output, Knoten werden an Knotenliste angehängt
        Besonders: Kein Output, anfügen an Knotenliste
        """
        to_add = self.premade[name]
        for point in to_add:
            point[0] += pos_x
            point[1] += pos_y
        self.nodes += to_add
        return None

    @classmethod
    def merge_dict(cls, dict1: dict, dict2: dict) -> dict:
        """Merge zweiter Dicts.

        Kommentar: kombiniert zwei Dictionaries, dict2 hat höhere Priorität
        Input: Name der Klasse, Dict1 und Dict2
        Output: Kombinitere Dictionaries
        Besonders: dict2 hat höhere Priorität (dict1 wird bei dopplung
                   überschrieben)
        """
        dict1.update(dict2)
        return dict1

    @classmethod
    def load_premade(cls, path: str) -> dict:
        """Lädt vorgefertigte Elemente aus einem Pfad.

        Kommentar: lädt eine json Datei aus einem Pfad
        Input: Name der Klasse, Pfad zur Datei
        Output: Daten der Datei
        Besonders: Keine Besonderheiten
        """
        data = json.load(open(path, "r"))
        return data

    @classmethod
    def get_list_intersection(cls, list_a: list, list_b: list) -> list:
        """Gibt die Überschneidung zweier Listen zurück.

        Kommentar: erzeugt die überschneidung zweier listen
        Input: Name der Klasse, erste Liste, zweite Liste
        Output: Überschneidung der Listen
        Besonders: Keine Besonderheiten
        """
        intersect = [item for item in list_a if item in list_b]
        return intersect

    @classmethod
    def __gen_matrix(cls, x_koord: int, y_koord: int) -> list:
        """Generiert eine Leere Matrix.

        Kommentar: generiert eine Matrix anhand einer vorgegeben Größe
        Input: Name der Instanz, x--breite als int, y--höhe als int
        Output: Leere Matrix
        Besonders: Schnellste Methode, eine Liste zu erzeugen
        """
        matrix = [[0 for place in range(x_koord)] for row in range(y_koord)]
        return matrix

    @classmethod
    def __get_dir(cls) -> list:
        """Gibt alle Top-Level Ordner zurück.

        Kommentar: Private Classmethod, die alle Top-Level Ordner auflistet
        Input: Name der Klasse (Game in dieser Klasse)
        Output: Alle Top-Level Ordner
        Besonders: Nutzt das OS modul (anfangs importiert)
        """
        top_dir = next(os.walk("."))[1]
        return top_dir

    @classmethod
    def __check_dir(cls, dir_name: str) -> None:
        """Überprüfung nach Ordner.

        Kommentar: Private Classmethod, die überprüft ob ein Ordner vorhanden
                   ist und diesen erstellt, falls nicht.
        Input: Name der Klasse, Name des Ordners
        Output: Keins
        Besonders: Nutzt das os modul, welches am Anfang importiert wird
        """
        if dir_name not in Game.__get_dir():
            command = "mkdir {dirName}"
            command = command.format(dirName=dir_name)
            os.system(command)
        return None

    @classmethod
    def daten_speichern(cls, data, filename: str) -> None:
        """Speichert gegebene Daten in eine Datei.

        Kommentar: Speichert Daten in eine Datei
        Input: Name der Klasse, Daten, Dateiname
        Output: Kein Output
        Besonders: Nutzt das pickle und os modul, Daten werden in saves Ordner
                   gespeichert
        """
        Game.__check_dir("saves")
        path = os.path.join("saves", filename)
        json.dump(data, open(path, "w"))
        return None

    @classmethod
    def daten_laden(cls, filename: str) -> dict:
        """Lädt Daten aus einer Datei.

        Kommentar: lädt daten aus einer Datei
        Input: Name der Klasse, Dateiname
        Output: Geladene Daten
        Besonders: Nutzt das pickle und os modul, Daten werden aus saves Ordner
                   geladen
        """
        Game.__check_dir("saves")
        path = os.path.join("saves", filename)
        daten = json.load(open(path, "r"))
        return daten


def debug():
    """Debug Funktion."""
    test_pulse = [[1, 0], [1, 1], [1, 2]]
    test_gleiter = [[1, 0], [2, 1], [0, 2], [1, 2], [2, 2]]
    test = Game(nodes=test_pulse, board_x=10, board_y=10)
    # test.add_premade("Toad", 0, 0)
    print(test.list_premade())
    matrix = test.get_matrix()
    for row in matrix:
        print(row)
    iterationen = 3
    for iteration in range(iterationen):
        time.sleep(2)
        print("")
        test.next_board()
        matrix = test.get_matrix()
        for row in matrix:
            print(row)


def check_save():
    """Testfunktion für das Speichern und Laden."""
    test_pulse = [[1, 0], [1, 1], [1, 2]]
    test_gleiter = [[1, 0], [2, 1], [0, 2], [1, 2], [2, 2]]
    test = Game(nodes=test_gleiter, board_x=10, board_y=10)
    matrix = test.get_points()
    Game.daten_speichern(matrix, "test.json")
    data = Game.daten_laden("test.json")
    print(data)


if __name__ == '__main__':
    debug()
