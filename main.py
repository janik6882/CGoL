"""Main Datei für das Projekt."""
import multiprocessing
import subprocess
import json
from frontend import Display
import pygame
import ast
# queue = multiprocessing.Queue()
res_data = dict()

# manager = multiprocessing.Manager()
# return_dict = manager.dict()

def menu_proc():
    global res_data
    """Doctstring."""  # TODO: add docstring
    res = subprocess.check_output("python GUI.py")
    # global return_dict
    data = res.decode("utf-8")
    data = ast.literal_eval(data)
    res_data["res"] = data
    json.dump(res_data, open("menu.json", "w"))
    # return_dict["res"] = data
    # print(res.decode("utf-8"))
    # print(res)


def open_menu():
    global res_data
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
    print(res_data)
    return("lol")
    # print(return_dict.values())

    # command = proc.get()
    # return command

def main():
    """Doctstring."""  # TODO: docu beenden
    global res_data
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
        print(res_data)
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
