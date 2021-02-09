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
|get_num_neighbours()|gibt die anzahl der Nachbarn einer Zelle aus|self--Name der Instanz<br />Zelle([x, y])|Anzahl der Nachbarn als Int|:white_check_mark:|nutzt get_list_intersection()|
|check_regeln()|überprüft, ob an einer Stelle in der nächsten generation eine Zelle vorhanden sein soll|Name der Instanz<br />Zelle([x, y])|Boolean, ob Zelle vorhanden sein soll|:white_check_mark:|nutzt get_num_neighbours()|
|next_board()|generiert das nächste Bord, aktualisiert self.nodes zur neuen Knotenliste|Name der Instanz|
|get_points()|gibt die Punkte in Form einer Verschachtelten Liste zurück| self--name der Instanz|[[x-Koordinate als int, y-Koordinate als int], [x-Koordinate als int, y-Koordinate als int]]|:white_check_mark:|
|add_point()| fügt punkt hinzu| x und y koordinate jeweils einzeln|gibt die aktualisierte Knotenliste zurück|:white_check_mark:|
|remove_point()|entfernt einen Punkt| self --name der Instanz<br /> x--x koordinate des Punktes<br />y--y-Koordinate des Punktes|gibt die aktualisierte Knotenliste zurück|:white_check_mark:|
|manipulate_point()|fuegt einen Punkt hinzu, wenn keiner vorhanden ist bzw. fügt einen hinzu wenn der Punkt nicht existiert|self --name der Instanz<br /> x--x koordinate des Punktes<br />y--y-Koordinate des Punktes|True wenn punkt hinzugefuugt, False wenn entfernt|:white_check_mark:|
|get_matrix()|gibt die aktuelle Matrix in Form einer Matrix zurück|self--Name der Instanz<br />|z.B. (Punkt bei (0, 0) und (0, 1)):[[0, 1, 0], [0, 1, 0], [0, 0, 0]]|:white_check_mark:|
|manipulate_point|Manipuliert einen Punkt, entfernt wenn vorhanden, fügt hinzu wenn nicht|self--Name der Instanz,<br />x--X-Koordinate des Punktes,<br />Y--Y-Koordinate des Punktes| True wenn Punkt hinzugefuegt, False wenn entfernt|:white_check_mark:|   |
|export_current|exportiert den aktuellen Spielstand mittels daten_speichern|self--Name der Instanz|Kein Output|:white_check_mark:|   |
|list_premade|gibt alle vorgefertigte Objekte als Liste aus|self--Name der Instanz|Liste mit allen Objekten|:white_check_mark:|   |
|import_premade|importiert vorgefertigte Objekte|self--Nam der Instanz,<br />Optional:filename--Wenn gegeben, Dateiname zur Datei|inhalt der Json Datei|:white_check_mark:|aktualisiert self.premade mit den importierten Objekten|
|add_premade|Fuegt ein Vorgefertiges Objekt an einer angegebenen Stelle ein|self--Name der Instanz,<br />posX--X-Koordinate,<br />posY--Y-Koordinate|Kein Output|:white_check_mark:|posX/posY sinnt ist der Punkt links oben am Objekt|
#### Klassenmethoden
|merge_dict|kombiniert zwei Dictionaries zu einem|self--Name der Klasse,<br />dict1--Ertses Dictionary,<br />dict2--Zweites Dictionary|kombinierte Dictionary|:white_check_mark:|dict2 hat Priorität|
|load_premade|lädt vorgefertigte Objekte aus einer Json datei|self--Name der Klasse,<br />path--Pfad zur Datei|Daten als Dictionary|:white_check_mark:|   |
|__gen_matrix()|generiert muliplikativ eine leere Matrix|self--name der Klasse<br />x--breite der Matrix<br />y--Höhe der Matrix| z.B. 3*3 Matrix: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]|:white_check_mark:|zum internen gebrauch vorgesehen, deshalb privat|
|get_list_intersection()|findet die überschneidungen zweier Listen|Name der Klasse<br />listA--Erste Liste<br />listB--Zweite Liste| Gibt eine Liste mit überschneidungen beider Listen zurück|:white_check_mark:||
|__get_dir|Listet alle Top Level Ordner auf|self--Name der Klasse|Top Level Ordner als Liste|:white_check_mark|Nutzt das os Modul|
|__check_dir|überprüft, ob ein ordner vorhanden ist, wenn nicht erstellt es diesen|self--Name der Klasse,<br />dir_name--Name des Ordners|Kein Output|:white_check_mark:|Nutzt das os Modul und führt einen Befehl aus|
|daten_speichern|Speichert die Spieldaten in den saves ordner|self--Name der Instanz,<br />Daten--Daten, die zu speichern sind,<br />Filename--Name der Datei|Kein Output|:white_check_mark:|   |
|daten_laden|Importiert die Spieldaten aus einer Json Datei|self--Name der Klasse,<br />filename--Dateiname|Daten der angegebenen Datei|:white_check_mark|   |
