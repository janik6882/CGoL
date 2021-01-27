# Vorerst Datei fuer alles Backend stuff.
class game():
    def __init__(self, nodes=[], boardY=30, boardX=30):
        self.nodes = nodes
        self.boardX = boardX
        self.boardY = boardY

    def get_num_neighbours(self, zelle):
        """
        Kommentar: gibt die anzahl der Nachbarn als int aus
        Input: Name der Instanz, Zelle ([x, y]), optional: anz. der nachbarn
        Output: Int mit anzahl der Nachbarn
        Besonders: keine Besonderheiten
        """
        x, y = zelle[0], zelle[1]
        nachbarn = 0
        nachbar_zellen = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1],
                          [x+1, y-1], [x+1, y], [x+1, y+1]]
        nachbarn = len(game.get_list_intersection(nachbar_zellen, self.nodes))
        return nachbarn

    def check_regeln(self, zelle):
        """
        Kommentar: gibt aus, ob an der position von zelle eine Zelle erstellt
                    wird in der nächsten Iteration
        Input: Name der Instanz, Zelle ([x-koordinate, y-koordinate])
        Output: False, wenn keine Zelle, True wenn Zelle in der nächsten
                Iteration
        Besonders: nutzt get_num_neighbours()
        """
        nachbarn = self.get_num_neighbours(zelle)
        if zelle in self.nodes:
            if nachbarn < 2 or nachbarn > 3:
                return False
            else:
                return True
        else:
            if nachbarn == 3:
                return True
            else:
                return False

    def next_board(self):
        """
        Kommentar:erzeugt das neue board und ersetzt das aktuelle mit dem neuen
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
                if zelle not in nachbarn and zelle not in nodes:
                    nachbarn.append(zelle)
            if self.check_regeln(node):
                new_board.append(node)
        for f in nachbarn:
            if self.check_regeln(f):
                new_board.append(f)
        self.nodes = new_board
        return new_board

    def get_points(self):
        """
        Kommentar: gibt die aktuelle knotenliste aus
        Input: Name der Instanz
        Output: Knotenliste self.node
        Besonders: Rückgabe mittels return
        """
        return self.nodes

    def add_point(self, x, y):
        """
        Kommentar: Fuegt einen Punkt zur knotenliste self.nodes hinzu
        Input: name der instanze, x-koordinate als int, y-koordinate als int
        Output: Aktualisierte knotenliste self.nodes
        Besonders: Weitere Optimierung der Laufzeit
        """
        # TODO: Verhalten besprechen, wenn punkt bereits in Knotenliste
        # OPTIMIZE: Laufzeit optimieren (add, append oder operator?)
        self.nodes.append([x, y])
        return self.nodes

    def remove_point(self, x, y):
        """
        Kommentar: Entfernt einen Punkt aus der Knotenliste
        Input: Name der Instanz, x-koordinate als int, y-koordinate als int
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
        Input: Name der Instanz, x-koordinate als int, y-koordinate als int
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
        Kommentar: gibt eine Matrix aus, welche alle punkte beeinhaltet
        Input: name der Instanz
        Output: Matrix mit allen punkten, eine Reihe entspricht einer Liste
        Besonders: Keine Besonderheiten
        """
        matrix = game.__gen_matrix(self.boardX, self.boardY)
        points = self.nodes
        for node in points:
            matrix[node[1]][node[0]] = 1
        return matrix

    @classmethod
    def get_list_intersection(self, listA, listB):
        intersect = [item for item in listA if item in listB]
        return intersect

    @classmethod
    def __gen_matrix(self, x, y):
        """
        Kommentar: generiert eine Matrix anhand einer vorgegeben größe
        Input: Name der Instanz, x--breite als int, y--höhe als int
        Output: Leere Matrix
        Besonders: Schnellste methode, eine Liste zu erzeugen
        """
        matrix = [[0 for place in range(x)] for row in range(y)]
        return matrix


def debug():
    test_nodes = [[1, 0], [1, 1], [1, 2]]
    test = game(nodes=test_nodes, boardX=10, boardY=10)
    m = test.get_matrix()
    for i in m:
        print (i)
    test.next_board()
    print ("")
    m = test.get_matrix()
    for i in m:
        print (i)


if __name__ == '__main__':
    debug()
