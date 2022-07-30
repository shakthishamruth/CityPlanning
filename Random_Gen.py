import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('City-planning')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

c = True

if c:
    l = int(input('square size(max = 500):'))
    c = False

matrix = []
for i in range(int((500 / l) ** 2)):  # A for loop for row entries
    a = []
    for j in range(int((500 / l) ** 2)):  # A for loop for column entries
        a.append(int(random.randint(1, 101)))
    matrix.append(a)

running = True


def drawGrid(n):
    blockSize = n  # Set the size of the grid block
    for i in range(0, WINDOW_WIDTH, blockSize):
        for j in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(i, j, blockSize, blockSize)
            pygame.draw.rect(SCREEN, (0, 0, 0), rect, 2)


def fillGrid(n):
    global matrix
    a = 0
    b = 0
    blockSize = n - 2  # Set the size of the grid block
    for i in range(0, WINDOW_WIDTH, blockSize + 2):
        for j in range(0, WINDOW_HEIGHT, blockSize + 2):
            if (matrix[a][b] <= 35):
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (0, 255, 0), rect)
            elif matrix[a][b] >= 35 and matrix[a][b] <= 56:
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (0, 0, 255), rect)
            elif matrix[a][b] >= 56 and matrix[a][b] <= 70:
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (255, 241, 31), rect)
            a = a + 1
            b = b + 1


while running:
    screen.fill((255, 255, 255))
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not c:
        fillGrid(l)
        drawGrid(l)
    pygame.display.update()
