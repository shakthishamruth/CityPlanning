import pygame
import random

pygame.init()

# window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('City-planning')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

c = True

if c:
    x = 10
    # x = int(input('Cube size(max = 100):'))
    x = x * 5
    c = False

matrix = []
for i in range(int((500 / x) ** 2)):  # A for loop for row entries
    a = []
    for j in range(int((500 / x) ** 2)):  # A for loop for column entries
        a.append(int(0))
    matrix.append(a)

# Algorithm to generate city
residential = 35
while not residential == 0:
    for i in range(1, 10):  # A for loop for row entries
        for j in range(1, 10):  # A for loop for column entries
            pick_num_i = 0
            pick_num_j = 0
            if not matrix[i - pick_num_i][j - pick_num_j] == 1:
                matrix[i - pick_num_i][j - pick_num_j] = 1
                residential -= 1


# funcs
def drawGrid(n):
    blockSize = n  # Set the size of the grid block
    for i in range(0, WINDOW_WIDTH, blockSize):
        for j in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(i, j, blockSize, blockSize)
            pygame.draw.rect(SCREEN, (0, 0, 0), rect, 2)


def fillGrid(n):
    global matrix, blockSize
    a = 0
    b = 0
    blockSize = n - 2  # Set the size of the grid block
    for i in range(0, WINDOW_WIDTH, blockSize + 2):
        for j in range(0, WINDOW_HEIGHT, blockSize + 2):
            if (matrix[a][b] == 1):  # green
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (0, 255, 0), rect)
            elif matrix[a][b] >= 35 and matrix[a][b] <= 56:  # blue
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (0, 0, 255), rect)
            elif matrix[a][b] >= 56 and matrix[a][b] <= 70:  # yellow
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (255, 241, 31), rect)
            elif matrix[a][b] == 0:
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (255, 255, 255), rect)
            a = a + 1
            b = b + 1


running = True

# main loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not c:
        fillGrid(x)
        drawGrid(x)
    pygame.display.update()

# end
