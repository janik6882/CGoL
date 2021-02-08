# -*- coding: utf-8 -*-
import time
import json
import os
# Vorerst Datei fuer alles Backend stuff.


class game():
    def __init__(self, nodes=[], boardX=30, boardY=30):
        """
        Kommentar: Standard init Methode
        Input: Name der Instanz, optional: nodes--(siehe docs), boardX--Breite
               der Simulation, boardY--höhe der Simulation
        Output: Kein Output
        Besonders: Standard init, nichts Besonderes
        """
        self.nodes = nodes
        self.boardX = boardX
        self.boardY = boardY

    def get_num_neighbours(self, x, y):
        """
        Kommentar: gibt die Anzahl der Nachbarn als int aus
        Input: Name der Instanz, x-Koordinate, y-Koordinate
        Output: Int mit anzahl der Nachbarn
        Besonders: keine Besonderheiten
        """
        nachbarn = 0
        nachbar_zellen = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1],
                          [x+1, y-1], [x+1, y], [x+1, y+1]]
        # setzen der Nachbarn zur länge der Überschneidung von nachbar_zellen
        #  und self.nodes (Knotenliste)
        nachbarn = len(game.get_list_intersection(nachbar_zellen, self.nodes))
        return nachbarn

    def check_regeln(self, x, y):
        """
        Kommentar: gibt aus, ob an der Position von Zelle eine Zelle erstellt
                    wird in der nächsten Iteration
        Input: Name der Instanz, x-Koordinate, y-Koordinate
        Output: False, wenn keine Zelle, True wenn Zelle in der nächsten
                Iteration
        Besonders: nutzt get_num_neighbours()
        """
        zelle = [x, y]
        nachbarn = self.get_num_neighbours(x, y)  # anzahl Nachbarn der Zelle
        if zelle in self.nodes:
            if nachbarn in [2, 3]:  # wenn nachbarn gleich 2 oder 3
                return True
            else:
                return False
        else:
            if nachbarn == 3:
                return True
            else:
                return False

    def next_board(self):
        """
        Kommentar:erzeugt das neue board und ersetzt das Aktuelle mit dem neuen
        Input: name der Instanz
        Output: aktualisierte Knotenliste
        Besonders: nutzt check_regeln
        """
        new_board = []
        nachbarn = []
        nodes = self.nodes
        for node in nodes:  # loop durch alle elemente von self.nodes
            x = node[0]  # setzt x zur x-koordinate von node
            y = node[1]  # setzt y zur y-koordinate von node
            nachbar_zellen = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1],
                              [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
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

    def get_points(self):
        """
        Kommentar: gibt die aktuelle Knotenliste aus
        Input: Name der Instanz
        Output: Knotenliste self.node
        Besonders: Rückgabe mittels return
        """
        return self.nodes

    def add_point(self, x, y):
        """
        Kommentar: Fuegt einen Punkt zur Knotenliste self.nodes hinzu
        Input: name der Instanz, x-Koordinate als int, y-Koordinate als int
        Output: Aktualisierte Knotenliste self.nodes
        Besonders: Weitere Optimierung der Laufzeit
        """
        # TODO: Verhalten besprechen, wenn punkt bereits in Knotenliste
        # OPTIMIZE: Laufzeit optimieren (add, append oder operator?)
        self.nodes.append([x, y])
        return self.nodes

    def remove_point(self, x, y):
        """
        Kommentar: Entfernt einen Punkt aus der Knotenliste
        Input: Name der Instanz, x-Koordinate als int, y-Koordinate als int
        Output: Aktualisierte Knotenliste self.nodes
        Besonders: Falls Punkt nicht in Knotenliste erfolgt Error
        """
        # OPTIMIZE: Laufzeit?
        # DEBUG: Try except pruefen
        if [x, y] in self.nodes:
            self.nodes.remove([x, y])
            return self.nodes
        else:
            # Ausgabe besprechen
            return "error"

    def manipulate_point(self, x, y):
        """
        Kommentar: Fuegt Punkt hinzu, wenn nicht vorhanden, entfernt wenn
                   vorhanden
        Input: Name der Instanz, x-Koordinate als int, y-Koordinate als int
        Output: Aktualisierte Knotenliste
        Besonders: Prueft ob Punkt in Knotenliste
        """
        if [x, y] in self.nodes:
            out = self.remove_point(x, y)
        else:
            out = self.add_point(x, y)
        return out

    def get_matrix(self):
        """
        Kommentar: gibt eine Matrix aus, welche alle Punkte beinhaltet
        Input: name der Instanz
        Output: Matrix mit allen Punkten, eine Reihe entspricht einer Liste
        Besonders: Keine Besonderheiten
        """
        matrix = game.__gen_matrix(self.boardX, self.boardY)
        points = self.nodes
        for node in points:
            matrix[node[1]][node[0]] = 1
        return matrix

    def export_current(self):
        # TODO: add docu
        export = dict()
        export["boardX"] = self.boardX
        export["boardY"] = self.boardY
        export["nodes"] = self.nodes
        game.daten_speichern(export, "out.json")

    @classmethod
    def get_list_intersection(self, listA, listB):
        # TODO: Dokumentation hinzufuegen
        intersect = [item for item in listA if item in listB]
        return intersect

    @classmethod
    def __gen_matrix(self, x, y):
        """
        Kommentar: generiert eine Matrix anhand einer vorgegeben Größe
        Input: Name der Instanz, x--breite als int, y--höhe als int
        Output: Leere Matrix
        Besonders: Schnellste Methode, eine Liste zu erzeugen
        """
        matrix = [[0 for place in range(x)] for row in range(y)]
        return matrix

    @classmethod
    def __get_dir(self):
        """
        Kommentar: Private Classmethod, die alle Top-Level Ordner auflistet
        Input: Name der Klasse (game in dieser Klasse)
        Output: Alle Top-Level Ordner
        Besonders: Nutzt das OS modul (anfangs importiert)
        """
        top_dir = next(os.walk("."))[1]
        return top_dir

    @classmethod
    def __check_dir(self, dir_name):
        """
        Kommentar: Private Classmethod, die überprüft ob ein Ordner vorhanden
                   ist und diesen erstellt, falls nicht.
        Input: Name der Klasse, Name des Ordners
        Output: Keins
        Besonders: Nutzt das os modul, welches am Anfang importiert wird
        """
        if dir_name not in game.__get_dir():
            command = "mkdir {dirName}"
            command = command.format(dirName=dir_name)
            os.system(command)

    @classmethod
    def daten_speichern(self, data, filename):
        """
        Kommentar: Speichert Daten in eine Datei
        Input: Name der Klasse, Daten, Dateiname
        Output: Kein Output
        Besonders: Nutzt das pickle und os modul, Daten werden in saves Ordner
                   gespeichert
        """
        game.__check_dir("saves")
        path = os.path.join("saves", filename)
        json.dump(data, open(path, "w"))

    @classmethod
    def daten_laden(self, filename):
        """
        Kommentar: lädt daten aus einer Datei
        Input: Name der Klasse, Dateiname
        Output: Geladene Daten
        Besonders: Nutzt das pickle und os modul, Daten werden aus saves Ordner
                   geladen
        """
        game.__check_dir("saves")
        path = os.path.join("saves", filename)
        daten = json.load(open(path, "r"))
        return daten


def debug():
    test_pulse = [[1, 0], [1, 1], [1, 2]]
    test_gleiter = [[1, 0], [2, 1], [0, 2], [1, 2], [2, 2]]
    test = game(nodes=test_gleiter, boardX=10, boardY=10)
    m = test.get_matrix()
    for row in m:
        print (row)
    iterationen = 3
    for i in range(iterationen):
        time.sleep(2)
        print ("")
        test.next_board()
        m = test.get_matrix()
        for row in m:
            print (row)

def check_save():
    test_pulse = [[1, 0], [1, 1], [1, 2]]
    test_gleiter = [[1, 0], [2, 1], [0, 2], [1, 2], [2, 2]]
    test = game(nodes=test_gleiter, boardX=10, boardY=10)
    m = test.get_points()
    game.daten_speichern(m, "test.json")
    x = game.daten_laden("test.json")
    print(x)



if __name__ == '__main__':
    # debug()
    check_save()
