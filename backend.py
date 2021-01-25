# Vorerst Datei fuer alles Backend stuff.
class game():
    def __init__(self, nodes=[], boardY=30, boardX=30):
        self.nodes = nodes
        self.boardX = boardX
        self.boardY = boardY

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
        Kommentar: Fuegt Punkt hinzu, wenn nicht vorhanden, entfernt wenn vorhanden
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
        matrix = game.gen_matrix(self.boardX, self.boardY)
        for node in self.nodes:
            matrix[node[1]][node[0]] = 1
        return matrix

    @classmethod
    def gen_matrix(self, x, y):
        """
        Kommentar: generiert eine Matrix anhand einer vorgegeben größe
        Input: Name der Instanz, x--breite als int, y--höhe als int
        Output: Leere Matrix
        Besonders: Schnellste methode, eine Liste zu erzeugen
        """
        matrix = [[0]*x]*y
        return matrix


def debug():
    test = game()
    x = game.gen_matrix(10, 10)
    for reihe in x:
        print (reihe)


if __name__ == '__main__':
    debug()
