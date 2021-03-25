from tkinter import *

class display:

    def open_menu(self):
        """Öffnet ein TKinter Menü.
        Kommentar: Erstelt ein TKInter Menü und öffnet dieses
        Input: Name der Instanz
        Output: Kein Output
        Besonders: Keine Besonderheiten
        """
        self.master = Tk()

        self.master.geometry("200x100")
        self.master.resizable(0, 0)

        self.master.title("CgoL")

        self.title_label = Label(self.master, text="Spielmenü")
        self.title_label.grid(row=0, column=0, sticky='ew')

        self.save_button = Button(self.master, text="Speichern",
                                  command=lambda: self.save_file(self.game.get_points(), False))
        self.save_button.grid(row=1, column=0, sticky='ew')

        self.load_button = Button(self.master, text="Laden", command=lambda: self.open_saved_board())
        self.load_button.grid(row=1, column=1, sticky='ew')

        self.import_button = Button(self.master, text="Objekte laden", command=lambda: self.import_premade())
        self.import_button.grid(row=2, column=0, sticky="ew")

        self.manual_button = Button(self.master, text="Anleitung")
        self.manual_button.grid(row=2, column=1, sticky='ew')

        self.quit_button = Button(self.master, text="Quit", command= lambda: self.spiel_verlassen())
        self.quit_button.grid(row=3, column=0, sticky='ew')

        self.master.columnconfigure(0, weight=5, uniform="commi")
        self.master.columnconfigure(1, weight=5, uniform="commi")
        self.master.mainloop()

a = display()
a.open_menu()
