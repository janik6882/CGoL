from tkinter import *


def anleitung():
    tkFenster = Tk()
    fensterBreite = tkFenster.winfo_reqwidth()
    fensterHoehe = tkFenster.winfo_reqheight()
    positionRechts = int(tkFenster.winfo_screenwidth() / 2 - fensterBreite / 2)
    positionUnten = int(tkFenster.winfo_screenheight() / 2 - fensterHoehe / 0.75)
    tkFenster.focus_force()
    tkFenster.title('Bedienungsanleitung: Zum weiter spielen muss zuerst dieses Fenster geschlossen werden.')
    tkFenster.geometry('1500x750')
    labelText = Label(master=tkFenster, text='Das Spielfeld ist in Zeilen und Spalten unterteilt und unendlich groß. '
                                             'Jedes Gitterquadrat definiert eine Zelle, welche einen von zwei '
                                             'Zuständen einnehmen kann: lebendig oder tot.\nEine Zelle lebt, '
                                             'wenn sie schwarz gefärbt ist. Sie ist tot, wenn sie weiß gefärbt '
                                             'ist. Die Nachfolgegenerationen sind durch Iterationen '
                                             'definiert.\n\n\nKürzel: \nEsc: Programm beenden\nM: Menü öffnen\nF: '
                                             'Nächste Iteration\n->: Nächste Form auswählen\n<-: Vorherige Form '
                                             'auswählen\nP: Modus Zelle/Spur/Radieren/Form platzieren\nLinksklick: '
                                             'Interaktion\nRechtsklick: Zelle zentrieren\n\nWeitere Anzeige:\n- '
                                             'Iterationsanzahl\n- Aktueller Modus\n- Aktuelle Form\n- Rotation der '
                                             'Form\n- Knopf zur automatischer Iteration\n\n\nRegeln:\n- Nachbarzellen '
                                             'sind alle Zellen ein Kästchen unmittelbar und auch diagonal daneben. '
                                             'Eine Zelle hat demenstprechend 8 Nachhbarzellen.\n- Wenn eine Zelle lebt und 2 '
                                             'oder 3 Nachbarn leben, bleibt die Zelle in der folgenden Iteration am '
                                             'Leben.\n- Eine lebende Zelle mit mehr als 3 lebenden Nachbarn stirbt in '
                                             'der nächsten Iteration an Überbevölkerung.\n- Eine lebende Zelle mit '
                                             'weniger als 2 lebenden Nachbarn stirb in der nächsten Iteration an '
                                             'Einsamkeit.\n- Eine tote Zelle mit genau 3 lebenden Nachbarn wird in der '
                                             'nächsten Iteration wiederbelebt.\n\n\nHinweis:\nSehr viele lebende '
                                             'Zellen sind sehr rechenaufwendig und dauern dementsprechend länger.',
                      fg='black', bg='white', font=('Arial',12))
    labelText.place(x=0, y=0, width=1500, height=750)
    mainloop()

if __name__ == "__main__":
    anleitung()
