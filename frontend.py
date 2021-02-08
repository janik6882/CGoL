import pygame
from backend import *
import time
import sys


class Main():
    def __init__(self, windowX, windowY, nodes=None):
        # TODO: add docu
        self.windowX = windowX
        self.windowY = windowY
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        board_sizeX = self.windowX//10
        board_sizeY = self.windowY//10
        self.game = game(nodes=nodes, boardX=board_sizeX, boardY=board_sizeY)

    def display_window(self):
        # TODO: add docu
        self.display = pygame.display.set_mode((self.windowX, self.windowY))

    def clear_board(self):
        self.display.fill(self.white)

    def update_board(self):
        pygame.display.flip()

    def show_board(self, points):
        self.clear_board()
        for point in points:
            x = point[0]
            y = point[1]
            pygame.draw.rect(self.display, self.black, pygame.Rect(y*10, x*10, 10, 10))
        self.update_board()

    def check_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def wait_keypress(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    nodeX = pos[1]//10
                    nodeY = pos[0]//10
                    pygame.draw.rect(self.display, self.black, pygame.Rect(nodeY*10, nodeX*10, 10, 10))
                    self.game.add_node(nodeX, nodeY)
                    self.update_board()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        return "f"
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def mainloop(self):
        while True:
            points = self.game.get_nodes()
            disp.show_board(points)
            # time.sleep(0.05)
            self.game.next_board()
            ev = self.wait_keypress()
            print (ev)
            self.check_close()


def main():
    test = Main(1000, 1000)
    test.display_window()
    test.clear_board()
    test.update_board()
    time.sleep(2)

def debug():
    glider_top_left = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 5], [3, 5], [4, 1], [4, 4]]
    disp = Main(1000, 1000, glider_top_left)
    disp.mainloop()



if __name__ == '__main__':
    debug()
