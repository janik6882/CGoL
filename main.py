"""Main Datei für das Projekt."""
import multiprocessing
import subprocess
import json
import ast
from frontend import Display
# import pygame
# queue = multiprocessing.Queue()

# manager = multiprocessing.Manager()
# return_dict = manager.dict()

def menu_proc():
    """Öffnet den GUI.py prozess.

    Einstellungen werden in menu.json gespeichert
    """
    res = subprocess.check_output("python GUI.py")
    # global return_dict
    data = res.decode("utf-8")
    data = ast.literal_eval(data)
    res_data = dict()
    res_data["res"] = data
    json.dump(res_data, open("menu.json", "w"))


def open_menu():
    global choice
    """Ruft die menu_proc() methode mit Multiprocessing auf.

    Kommentar: Öffnet das menü über Multiprocessing
    Input: Kein Input
    Output: Aktuell kein Output
    Besonders: Arbeitet mit Multiprocessing, bei Tests immer zu testen!!
    """
    # manager = multiprocessing.Manager()
    # return_dict = manager.dict()
    jobs = []
    proc = multiprocessing.Process(target=menu_proc)
    jobs.append(proc)
    proc.start()
    choice = json.load(open("menu.json"))
    # print(return_dict.values())

    # command = proc.get()
    # return command


def main():
    """Doctstring."""  # TODO: docu beenden
    global choice
    glider_top_left = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 5], [3, 5],
    [4, 1], [4, 4]]
    # proc.join()
    open_menu()
    test = Display(1000, 1000, glider_top_left)
    test.game.add_premade("Middle-weight spaceship", 5, 5)
    print(test.game.list_premade())
    while True:
        points = test.game.get_points()
        test.show_board(points)
        key = test.wait_keypress()
        if key == "m":
            print(open_menu())
            choice = json.load(open("menu.json", "r"))
            print(choice)
        test.game.next_board()
        print(x)
        print("test")
        Display.check_close()
    # test.mainloop()


'''def mainloop():
    """Mainloop, läuft bis beendet.

    Kommentar: Mainloop, läuft bis programm beendet wird
    Input: Name der Instanz
    Output: Kein Output
    Besonders: Keine Besonderheiten
    """
    while True:
        # points = test.game.get_points()
        test.show_board(points)
        key = test.wait_keypress()
        if key == "m":
            open_menu()
        command = proc.get()
        print(command)
        test.game.next_board()
        Display.check_close()
        '''




# Programm wird aus unerklärlichen Gründen doppelt ausgeführt.
if __name__ == "__main__":
    main()
