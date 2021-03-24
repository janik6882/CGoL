"""
Bedinungsanleitung:
Das Spielfeld ist in Zeilen und Spalten unterteilt und unendlich groß. Jedes Gitterquadrat definiert eine Zelle, welche einen von zwei Zuständen einnehmen kann: lebendig oder tod.
Eine Zelle lebt, wenn sie schwarz ausgefüllt ist. Sie ist Tod, wenn sie weiß ausgefüllt ist. Die Nachfolgegenerationen sind durch Iterationen definiert.

Kürzel: 
Esc: Programm beenden
M: Menü öffnen
F: nächste Iteration
->: nächste Form auswählen
<-: vorherige Form auswählen
P: Modus Zelle/Spur/Radieren/Form platzieren
Linksklick: Interaktion
Rechtsklick: Zelle <zentrieren

Weitere Anzeige:
- Iterationsanzahl
- aktueller Modus
- aktuelle Form
- Rotation der Form
- Knopf zur automatischer Iteration


Regeln:
- Nachbarzellen sind alle Zellen ein Kästchen unmittelbar und auch diagonal daneben. Sie hat demenstprechend 8 Nachhbarzellen
- Wenn eine Zelle lebt und 2 oder 3 Nachbarn leben, bleibt die Zelle in der folgenden Iteration am Leben
- Eine lebende Zelle mit mehr als 3 lebenden Nachbarn stirbt in der nächsten Iteration an Überbevölkerung
- Eine lebende Zelle mit weniger als 2 lebenden Nachbarn stirb in der nächsten Iteration an Einsamkeit
- Eine tote Zelle mit genau 3 lebenden Nachbarn wird in der nächsten Iteration wieder lebendig


Hinweis:
Sehr viele lebende Zellen sind sehr rechenaufwendig und dauern dementsprechend länger.
"""
