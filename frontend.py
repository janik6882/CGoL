from pygame import *
import pygame
from pygame.locals import *
import time
from backend import game
import sys
import math


class display():
    def __init__(self, windowX, windowY, nodes=[]):
        # TODO: add docu
        self.windowX = windowX
        self.windowY = windowY
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (173, 173, 173)
        board_sizeX = self.windowX//10
        board_sizeY = self.windowY//10
        self.game = game(nodes=nodes, boardX=board_sizeX, boardY=board_sizeY)
        self.display = pygame.display.set_mode((self.windowX, self.windowY))

    def clear_board(self):
        self.display.fill(self.white)
        self.draw_grid()

    def draw_grid(self):
        for x in range(0, self.windowX, 10):
            start_x = x
            start_y = 0
            end_x = x
            end_y = self.windowY
            start = (start_x, start_y)
            end = (end_x, end_y)
            pygame.draw.line(self.display, self.grey, start, end, width=1)
        for y in range(0, self.windowY, 10):
            start_x = 0
            start_y = y
            end_x = self.windowX
            end_y = y
            start = (start_x, start_y)
            end = (end_x, end_y)
            pygame.draw.line(self.display, self.grey, start, end, width=1)

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

    def manipulate_point(self, posX, posY):
        # TODO: Dokumentation hinzufuegen
        nodeX = posX//10
        nodeY = posY//10
        exist = self.game.manipulate_point(nodeX, nodeY)
        if exist:
            pygame.draw.rect(self.display, self.black, pygame.Rect(nodeY*10, nodeX*10, 10, 10))
        else:
            pygame.draw.rect(self.display, self.white, pygame.Rect(nodeY*10, nodeX*10, 10, 10))

    def wait_keypress(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    pos_x = pos[1]
                    pos_y = pos[0]
                    self.manipulate_point(pos_x, pos_y)
                    # self.game.add_point(nodeX, nodeY)
                    self.update_board()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        return "f"
                    if event.key == pygame.K_e:
                        self.game.export_current()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def mainloop(self):
        while True:
            points = self.game.get_points()
            self.show_board(points)

            # time.sleep(0.05)
            ev = self.wait_keypress()
            self.game.next_board()
            self.check_close()


def main():
    test = Main(1000, 1000)
    test.clear_board()
    test.update_board()
    time.sleep(2)

def debug():
    glider_top_left = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 1], [2, 5], [3, 5], [4, 1], [4, 4]]
    test = display(1000, 1000)
    test.mainloop()



if __name__ == '__main__':
    debug()
