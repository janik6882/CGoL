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
|Name der Funktion|Funktionsweise der Funktion|Input der Funktion|Output der Funktion|implementiert|
|:---------------:|:-------------------------:|:----------------:|:-----------------:|:-----------:|
|init|initialisiert die Funktion |self--name der Instanz<br />optional:<br />nodes--liste der Punkte<br />boardY--y höhe des Bretts<br />boardX--breite des Bretts|Kein Output|<ul><li>[x] implementiert</li></ul>|
|add_point()| fügt punkt hinzu| x und y koordinate jeweils einzeln|keins|<ul><li>[x] implementiert</li></ul>|
|remove_point()|entfernt einen Punkt| self --name der Instanz<br /> x--x koordinate des Punktes<br />y--y-Koordinate des Punktes|keines|<ul><li>[x] implementiert</li></ul>|
|manipulate_point()|fuegt einen Punkt hinzu, wenn keiner vorhanden ist bzw. fügt einen hinzu wenn der Punkt nicht existiert|self --name der Instanz<br /> x--x koordinate des Punktes<br />y--y-Koordinate des Punktes|keines|<ul><li>[x] implementiert</li></ul>|
|get_points()|gibt die Punkte in Form einer Verschachtelten Liste zurück| self--name der Instanz|[[x-Koordinate als int, y-Koordinate als int], [x-Koordinate als int, y-Koordinate als int]]|<ul><li>[x] implementiert</li></ul>|
|get_matrix()|gibt die aktuelle Matrix in Form einer Matrix zurück| z.B. (Punkt bei (0, 0) und (0, 1)):[[0, 1, 0], [0, 1, 0], [0, 0, 0]]| |<ul><li> [ ] </li></ul>|
