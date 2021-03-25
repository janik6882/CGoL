from tkinter import Tk, Label, mainloop


def anleitung():
    tkFenster = Tk()
    tkFenster.focus_force()
    tkFenster.title('Bedienungsanleitung: Zum weiter spielen muss zuerst dieses Fenster geschlossen werden.')
    tkFenster.geometry('1500x750')
    labelText = Label(master=tkFenster, text='Das Spielfeld ist in Zeilen und Spalten unterteilt und unendlich groß. Jedes Gitterquadrat definiert eine Zelle, welche einen von zwei Zuständen einnehmen kann: lebendig oder tod.\nEine Zelle lebt, wenn sie schwarz ausgefüllt ist. Sie ist Tod, wenn sie weiß ausgefüllt ist. Die Nachfolgegenerationen sind durch Iterationen definiert.\n\n\nKürzel: \nEsc: Programm beenden\nM: Menü öffnen\nF: nächste Iteration\n->: nächste Form auswählen\n<-: vorherige Form auswählen\nP: Modus Zelle/Spur/Radieren/Form platzieren\nLinksklick: Interaktion\nRechtsklick: Zelle zentrieren\n\nWeitere Anzeige:\n- Iterationsanzahl\n- aktueller Modus\n- aktuelle Form\n- Rotation der Form\n- Knopf zur automatischer Iteration\n\n\nRegeln:\n- Nachbarzellen sind alle Zellen ein Kästchen unmittelbar und auch diagonal daneben. Sie hat demenstprechend 8 Nachhbarzellen\n- Wenn eine Zelle lebt und 2 oder 3 Nachbarn leben, bleibt die Zelle in der folgenden Iteration am Leben\n- Eine lebende Zelle mit mehr als 3 lebenden Nachbarn stirbt in der nächsten Iteration an Überbevölkerung\n- Eine lebende Zelle mit weniger als 2 lebenden Nachbarn stirb in der nächsten Iteration an Einsamkeit\n- Eine tote Zelle mit genau 3 lebenden Nachbarn wird in der nächsten Iteration wieder lebendig\n\n\nHinweis:\nSehr viele lebende Zellen sind sehr rechenaufwendig und dauern dementsprechend länger.', fg='black', bg='white', font=('Arial',12))
    labelText.place(x=0, y=0, width=1500, height=750)
    mainloop()

if __name__ == "__main__":
    anleitung()
