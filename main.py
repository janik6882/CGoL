"""Main Datei für das Projekt."""
import multiprocessing
import subprocess
from frontend import Display


def menu_proc():
    """Doctstring."""  # TODO: add docstring
    subprocess.call("python GUI.py")


def main():
    """Doctstring."""  # TODO: docu beenden
    glider_top_left = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 5], [3, 5],
                       [4, 1], [4, 4]]
    proc = multiprocessing.Process(target=menu_proc)
    proc.start()
    # proc.join()
    test = Display(1000, 1000, glider_top_left)
    print(test.game.list_premade())
    test.game.add_premade("Middle-weight spaceship", 5, 5)
    test.mainloop()


# Programm wird aus unerklärlichen Gründen doppelt ausgeführt.
if __name__ == "__main__":
    main()
