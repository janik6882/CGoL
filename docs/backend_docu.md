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
|Name der Funktion|Funktionsweise der Funktion|Input der Funktion|Output der Funktion|
|:---------------:|:-------------------------:|:----------------:|:-----------------:|
|init|initialisiert die Funktion |self--name der Instanz<br />optional:<br />nodes--liste der Punkte<br />boardX--X höhe des Bretts<br />boardX--breite des Bretts|Kein Output|
|add_point()| fügt punkt hinzu| x und y koordinate jeweils einzeln| True oder False|
|remove_point()|
|manipulate_point()|
|get_points()|
|get_matrix()|
