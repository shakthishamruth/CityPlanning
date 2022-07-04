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
        a.append(int(random.randint(1, 101)))
    matrix.append(a)

running = True


# funcs
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
            if (matrix[a][b] <= 35):  # green
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (0, 255, 0), rect)
            elif matrix[a][b] >= 35 and matrix[a][b] <= 56:  # blue
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (0, 0, 255), rect)
            elif matrix[a][b] >= 56 and matrix[a][b] <= 70:  # yellow
                rect = pygame.Rect(i, j, blockSize, blockSize)
                pygame.draw.rect(SCREEN, (255, 241, 31), rect)
            b = b + 1
        a = a + 1


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
