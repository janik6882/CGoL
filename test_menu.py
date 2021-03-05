from tkinter import Button, Label, Tk
from frontend import Display


class Startfenster:
    def __init__(self, master):
        self.master = master
        master.title("Conways Game of Life")

        self.label = Label(master, text="Conways Game of Life")
        self.label.grid(row=0, column=0, columnspan=2, sticky='ew')

        self.play_button = Button(master, text="Play")
        self.play_button.grid(row=1, column=0, sticky='ew')

        self.pause_button = Button(master, text="Pause")
        self.pause_button.grid(row=2, column=0, sticky='ew')

        self.save_button = Button(master, text="Save", command=lambda: Display.save_file())
        self.save_button.grid(row=3, column=0, sticky='ew')

        self.load_button = Button(master, text="Load", command=lambda: Display.open_file())
        self.load_button.grid(row=4, column=0, sticky='ew')

        self.rules_button = Button(master, text="Rules")
        self.rules_button.grid(row=1, column=1, sticky='ew')

        self.forms_button = Button(master, text="Forms")
        self.forms_button.grid(row=2, column=1, sticky='ew')

        self.manual_button = Button(master, text="Manual")
        self.manual_button.grid(row=3, column=1, sticky='ew')

        self.auto_button = Button(master, text="Auto")
        self.auto_button.grid(row=4, column=1, sticky='ew')

        master.columnconfigure(0, weight=1, uniform="commi")
        master.columnconfigure(1, weight=1, uniform="commi")
        master.rowconfigure(1, weight=1, uniform="commi")
        master.rowconfigure(2, weight=1, uniform="commi")
        master.rowconfigure(3, weight=1, uniform="commi")
        master.rowconfigure(4, weight=1, uniform="commi")


def main():
    root = Tk()
    root.geometry("250x250")

    fenster = Startfenster(root)

    root.mainloop()


if __name__ == '__main__':
    main()
