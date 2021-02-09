# Dokumentation für das Frontend
### Klassen:
|Name der Klasse|Zweck der Klasse|
|:-------------:|:--------------:|
|display|erstellt das Frontend für das CGoL|
### Variablen:
|Name der Variable|Aufbau bzw. Syntax der Variable|Funktion der Variable|
|:---------------:|:-----------------------------:|:-------------------:|
|self|Name der Instanz|Für Zugriff auf die Instanz|
|windowX|Int, Breite des Fensters|Wird intern für die Breite genutzt|
|windowY|Int, Höhe des Fensters|Wird intern für die Höhe genutzt|
|self.windowX|wie windowX|wie windowX|
|self.windowY|wie windowY|wie windowY|
|nodes|[[x, y], [x, y]]|Fungiert als Knotenliste|
|self.game|Instanz der Klasse game()|Fungiert als Konstrukter und zum Zugriff auf die Klasse|
|self.black|(0, 0, 0)|Zum einfacheren und zentralen Zugriff auf die Farbe Schwarz|
|self.white|(255, 255, 255)|wie self.black|
|self.grey|(173, 173, 173)|wie self.grey|
|self.display|Instanz der Klasse pygame.display|Für Zugriff und Konstruktion der Klasse|
### Methoden:
|Name der Funktion|Funktionsweise der Funktion|Input der Funktion|Output der Funktion|implementiert|weiteres|
|:---------------:|:-------------------------:|:----------------:|:-----------------:|:-----------:|:------:|
|init|erzeugt ein objekt der Klasse game, erstellt ein display der Klasse pygame.display|self--Name der Instanz,<br /> windowX--Höhe des Fensters,<br />windowY--Breite des Fensters,<br />nodes--Liste der anfangsknoten|Kein Output|:white_check_mark:|   |
|clear_board|Entfernt alle Punkte vom Bord und zeichnet ein Gitter|self--Name der Instanz|Kein Output|:white_check_mark:|nutzt draw_grid()|
|draw_grid|Zeichnet ein Gitter mit Abstand von 10 px|self--Name der Instanz|Kein Output|:white_check_mark:|greift auf self.windowX und self.windowY zu|
|update_board|aktualisiert das Bord mittels pygame.display.flip()|self--Name der Instanz|Kein Output|:white_check_mark:|   |
|show_board|zeichnet bei jedem Punkt ein 9*9 Rechteck|self--Name der Instanz,<br />Punkte als Knotenliste|Kein Output|:white_check_mark:|greift auf self.clear_board und self.update_board zu|
|check_close|überprüft, ob der Close Button oder Escape Taste gedrückt wurde, wenn Ja schließen mit sys.exit()|self--Name der Instanz|Kein Output|:white_check_mark:|nutzt das sys Modul|
|manipulate_point|Manipuliert einen Punkt, wenn Punkt vorhanden wird dieser Entfernt, wenn nicht wird ein PUnkt hinzugefuegt|self--Name der Instanz,<br />posX--X-Position des Mausklicks,<br />posY--y-Position des Mausklicks|Kein Output|:white_check_mark:|nutzt game.manipulate_point|
|wait_keypress|Wartet auf einen Tastendruck und führt den entsprechenden Befehl aus|<self--Name der Instanz|Kein Output (aktuell für Debug zwecke)|:white_check_mark:|nutzt diverse sys und pygame Befehle|
|mainloop|Mainloop des Programms, läuft bis zur Unterbrechung|self--Name der Instanz|Kein Output|:white_check_mark:|   |
