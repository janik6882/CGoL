import tkinter as tk
from tkinter import Tk
from frontend import Display


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Conways Game of Life")

        self.label = tk.Label(master, text="Conways Game of Life")
        self.label.pack()

        self.play_button = tk.Button(master, text="Play")
        self.play_button.pack()

        self.pause_button = tk.Button(master, text="Pause")
        self.pause_button.pack()

        self.save_button = tk.Button(master, text="Save", command=lambda: Display.save_file())
        self.save_button.pack()

        self.load_button = tk.Button(master, text="Load", command=lambda: Display.open_file())
        self.load_button.pack()

        self.rules_button = tk.Button(master, text="Rules")
        self.rules_button.pack()

        self.forms_button = tk.Button(master, text="Forms")
        self.forms_button.pack()

        self.manual_button = tk.Button(master, text="Manual")
        self.manual_button.pack()

        self.auto_button = tk.Button(master, text="Auto")
        self.auto_button.pack()


def main():
    root = tk.Tk()
    root.geometry("500x500")
    my_gui = MyFirstGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
