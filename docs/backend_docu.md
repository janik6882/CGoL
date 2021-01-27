# Hier wird in kürze die Dokumentation bzw. Planung für das Backend erstehen. Sollten ideen aufkommen, teilt diese bitte über die Issues.
## Planung:
### Klassen:
|Name der Klasse|Zweck der Klasse|
|:-------------:|:--------------:|
|game|erzeugt eine Klasse, mit welcher das CGoL generiert werden kann|
### Variablen:
|Name der Variable|Aufbau bzw. Syntax der Variable|Funktion der Variable|
|:---------------:|:-----------------------------:|:-------------------:|
|self|Objekt|Instanz der Klasse|
|nodes|[[x koordinate als int, y koordinate als int]]|Speichert die Punkte innerhalb der Klasse und kann diese Ausgeben|
|boardX|Breite der Simulation als int|Speichert die Breite der Simulation intern|
|boardY|Höhe der Simulation als int|Speichert die Höhe der Simulation intern|
### Funktionen:
|Name der Funktion|Funktionsweise der Funktion|Input der Funktion|Output der Funktion|implementiert|weiteres|
|:---------------:|:-------------------------:|:----------------:|:-----------------:|:-----------:|:------:|
|init|initialisiert die Funktion |self--name der Instanz<br />optional:<br />nodes--liste der Punkte<br />boardY--y höhe des Bretts<br />boardX--breite des Bretts|Kein Output|:white_check_mark:|
|add_point()| fügt punkt hinzu| x und y koordinate jeweils einzeln|gibt die aktualisierte Knotenliste zurück|:white_check_mark:|
|remove_point()|entfernt einen Punkt| self --name der Instanz<br /> x--x koordinate des Punktes<br />y--y-Koordinate des Punktes|gibt die aktualisierte Knotenliste zurück|:white_check_mark:|
|manipulate_point()|fuegt einen Punkt hinzu, wenn keiner vorhanden ist bzw. fügt einen hinzu wenn der Punkt nicht existiert|self --name der Instanz<br /> x--x koordinate des Punktes<br />y--y-Koordinate des Punktes|gibt die aktualisierte Knotenliste zurück|:white_check_mark:|
|get_points()|gibt die Punkte in Form einer Verschachtelten Liste zurück| self--name der Instanz|[[x-Koordinate als int, y-Koordinate als int], [x-Koordinate als int, y-Koordinate als int]]|:white_check_mark:|
|get_matrix()|gibt die aktuelle Matrix in Form einer Matrix zurück|self--Name der Instanz<br />|z.B. (Punkt bei (0, 0) und (0, 1)):[[0, 1, 0], [0, 1, 0], [0, 0, 0]]|:white_check_mark:|
|get_num_neighbours()|gibt die anzahl der Nachbarn einer Zelle aus|self--Name der Instanz<br />Zelle([x, y])|Anzahl der Nachbarn als Int|:white_check_mark:|nutzt get_list_intersection()|
|check_regeln()|überprüft, ob an einer Stelle in der nächsten generation eine Zelle vorhanden sein soll|Name der Instanz<br />Zelle([x, y])|Boolean, ob Zelle vorhanden sein soll|:white_check_mark:|nutzt get_num_neighbours()|
|next_board()|generiert das nächste Bord, aktualisiert self.nodes zur neuen Knotenliste|Name der Instanz|
#### Klassenmethoden
|__gen_matrix()|generiert muliplikativ eine leere Matrix|self--name der Klasse<br />x--breite der Matrix<br />y--Höhe der Matrix| z.B. 3*3 Matrix: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]|:white_check_mark:|zum internen gebrauch vorgesehen, deshalb privat|
|get_list_intersection()|findet die überschneidungen zweier Listen|Name der Klasse<br />listA--Erste Liste<br />listB--Zweite Liste| Gibt eine Liste mit überschneidungen beider Listen zurück|:white_check_mark:||
