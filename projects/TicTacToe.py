import sys, pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255 ,0)
RED = (255, 0, 0)
h = 140
w = 140

def DrawText(display, font, txt, color):
    pygame.draw.rect(DISPLAY, WHITE, (0, 421, 420, 29))
    text = font.render(txt, True, color)
    display.blit(text, dest=(10, 430))


def GetBoxAccordingToCoords(coords, m_x, m_y):
    for i in range(0, 9):
        x, y = coords[i]
        if m_x > x and m_x < (x + w) and m_y > y and m_y < (y + h):
            return i
    return -1

def checkWin(colored_boxes, color_index):
    boxes = colored_boxes[color_index]
    # check vertical
    for x in range(0, 3):
        if 0+x in boxes and 3+x in boxes and 6+x in boxes:
            return True

    # check horizontal
    for x in range(0, 3, 3):
        if 0+x in boxes and 1+x in boxes and 2+x in boxes:
            return True

    # check daignols
    if 0 in boxes and 4 in boxes and 8 in boxes:
        return True

    if 2 in boxes and 4 in boxes and 6 in boxes:
        return True

    return False

coords = {}
r = 0 
c = 0
for i in range(0, 9):
    if(i % 3 == 0 and i != 0):
        r = r + 1
        c = 0
    x_i = c * 140
    y_i = r * 140
    c = c + 1
    coords[i] = (x_i, y_i)

pygame.init()
DISPLAY=pygame.display.set_mode((420,450),0,32)
pygame.display.set_caption('Tic-Tac-Toe Kartik') 
myfont = pygame.font.SysFont('Consolas', 12)
DISPLAY.fill(WHITE)


## Grid
pygame.draw.line(DISPLAY, BLUE, (140, 0), (140, 420))
pygame.draw.line(DISPLAY, BLUE, (280, 0), (280, 420))
pygame.draw.line(DISPLAY, BLUE, (0, 0), (420, 0))
pygame.draw.line(DISPLAY, BLUE, (0, 140), (420, 140))
pygame.draw.line(DISPLAY, BLUE, (0, 280), (420, 280))
pygame.draw.line(DISPLAY, BLUE, (0, 420), (420, 420))

color = GREEN
colored_boxes = {0:[], 1:[]}
DrawText(DISPLAY, myfont, "Player 1's chance!", RED)
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            box = GetBoxAccordingToCoords(coords, x, y)
            b_x, b_y = coords[box]
            color = GREEN if color is RED else RED
            color_index = 0 if color is RED else 1
            colored_boxes[color_index].append(box)
            pygame.draw.rect(DISPLAY, color, (b_x + 1, b_y + 1, w - 2, h - 2))
            if checkWin(colored_boxes, color_index):
                DrawText(DISPLAY, myfont, "Player {} won!".format(color_index + 1), color)
                break
            else:
                DrawText(DISPLAY, myfont, "Player {}'s chance!".format(1 if color_index == 1 else 2), GREEN if color == RED else RED)

    pygame.display.update()
