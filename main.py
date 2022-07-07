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
    x = 5
    # x = int(input('Cube size(max = 100):'))
    x = x * 5
    c = False

matrix = []
for i in range(int((500 / x) ** 2)):  # A for loop for row entries
    a = []
    for j in range(int((500 / x) ** 2)):  # A for loop for column entries
        a.append(int(0))
    matrix.append(a)

matrix[int(random.randint(10, 12))][int(random.randint(10, 12))] = 1
matrix[int(random.randint(8, 9))][int(random.randint(8, 9))] = 1

residential = 70 - 2  # 70%50*2
commercial = 42  # 70%30*2
industrial_block = 2
industrial = 28 - 2  # 70%20*2
geni = 3
genj = 3
geni_c = 1
genj_c = 1
geni_i = 0
genj_i = 0

done = False


# Func to generate city


def gen_residential():
    global residential, geni, genj
    if not residential == 0:
        # A for loop for row entries
        # A for loop for column entries
        pick_num_i = int(random.randint(-1, 1))
        pick_num_j = int(random.randint(-1, 1))
        if matrix[geni][genj] == 1:
            if matrix[int(geni - pick_num_i)][int(genj - pick_num_j)] == 0:
                matrix[int(geni - pick_num_i)][int(genj - pick_num_j)] = 1
                residential -= 1
        if not genj == 18:
            genj += 1
        else:
            if not geni == 18:
                geni += 1
                genj = 1
            else:
                geni = 1
                genj = 1


def gen_commercial():
    global residential, commercial, geni_c, genj_c, done

    if not commercial == 0 and residential >= 55:
        # A for loop for row entries
        # A for loop for column entries
        pick_num_i = int(random.randint(-1, 1))
        pick_num_j = int(random.randint(-1, 1))
        if matrix[geni_c][genj_c] == 1:
            if matrix[int(geni_c - pick_num_i)][int(genj_c - pick_num_j)] == 0:
                matrix[int(geni_c - pick_num_i)][int(genj_c - pick_num_j)] = 2
                commercial -= 1
        if not genj_c == 18:
            genj_c += 1
        else:
            if not geni_c == 18:
                geni_c += 1
                genj_c = 1
            else:
                geni_c = 1
                genj_c = 1
    elif not commercial == 0 and residential == 0:
        # A for loop for row entries
        # A for loop for column entries
        pick_num_i = int(random.randint(-1, 1))
        pick_num_j = int(random.randint(-1, 1))
        if matrix[geni_c][genj_c] == 2:
            if matrix[int(geni_c - pick_num_i)][int(genj_c - pick_num_j)] == 0:
                matrix[int(geni_c - pick_num_i)][int(genj_c - pick_num_j)] = 2
                commercial -= 1
        if not genj_c == 18:
            genj_c += 1
        else:
            if not geni_c == 18:
                geni_c += 1
                genj_c = 1
            else:
                geni_c = 1
                genj_c = 1


def gen_industrial():
    global industrial, geni_i, genj_i, done, industrial_block
    if not industrial == 0 and residential >= 65:
        # A for loop for row entries
        # A for loop for column entries
        pick_num_i = int(random.choice([-4, 4]))
        pick_num_j = int(random.choice([-4, 4]))
        if matrix[geni_i][genj_i] == 1 or matrix[geni_i][genj_i] == 2:
            if matrix[int(geni_i - pick_num_i)][int(genj_i - pick_num_j)] == 0:
                matrix[int(geni_i - pick_num_i)][int(genj_i - pick_num_j)] = 3
                industrial -= 1
        if not genj_i == 19:
            genj_i += 1
        else:
            if not geni_i == 19:
                geni_i += 1
                genj_i = 0
            else:
                geni_i = 0
                genj_i = 0
    elif not industrial == 0 and commercial == 0 and residential == 0:
        # A for loop for row entries
        # A for loop for column entries
        # Create 2 industrial units
        if not industrial_block == 0:
            y = random.randint(2, 17)
            if not matrix[0][y + 7] == 1 and not matrix[0][y + 7] == 2:
                matrix[0][y] = 4
                industrial_block -= 1
            elif not matrix[19][y + 7] == 1 and not matrix[19][y + 7] == 2:
                matrix[19][y] = 4
                industrial_block -= 1
            elif not matrix[y + 7][0] == 1 and not matrix[y + 7][0] == 2:
                matrix[y + 6][0] = 4
                industrial_block -= 1
            elif not matrix[y + 7][19] == 1 and not matrix[y + 7][19] == 2:
                matrix[y + 6][19] = 4
                industrial_block -= 1
        if industrial_block == 0:
            pick_num_i = int(random.randint(-1, 1))
            pick_num_j = int(random.randint(-1, 1))
            if matrix[geni_i][genj_i] == 4:
                if matrix[int(geni_i - pick_num_i)][int(genj_i - pick_num_j)] == 0:
                    matrix[int(geni_i - pick_num_i)][int(genj_i - pick_num_j)] = 4
                    industrial -= 1
            if not genj_i == 19:
                genj_i += 1
            else:
                if not geni_i == 19:
                    geni_i += 1
                    genj_i = 0
                else:
                    geni_i = 0
                    genj_i = 0
    if commercial == 0 and residential == 0 and industrial == 0 and not done:
        print("Done")
        done = True


# Funcs
def drawGrid(n):
    blockSize = n  # Set the size of the grid block
    for i in range(0, WINDOW_WIDTH, blockSize):
        for j in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(i, j, blockSize, blockSize)
            pygame.draw.rect(SCREEN, (0, 0, 0), rect, 2)


def fillGrid(n):
    global matrix, blocksize
    a = 0
    b = 0
    blocksize = n - 2  # Set the size of the grid block
    for i in range(0, WINDOW_WIDTH, blocksize + 2):
        for j in range(0, WINDOW_HEIGHT, blocksize + 2):
            if matrix[a][b] == 1:  # green residential
                rect = pygame.Rect(i, j, blocksize, blocksize)
                pygame.draw.rect(SCREEN, (0, 255, 0), rect)
            elif matrix[a][b] == 2:  # blue commercial
                rect = pygame.Rect(i, j, blocksize, blocksize)
                pygame.draw.rect(SCREEN, (0, 0, 255), rect)
            elif matrix[a][b] == 3:  # yellow industrial
                rect = pygame.Rect(i, j, blocksize, blocksize)
                pygame.draw.rect(SCREEN, (255, 241, 31), rect)
            elif matrix[a][b] == 4:  # yellow industrial block
                rect = pygame.Rect(i, j, blocksize, blocksize)
                pygame.draw.rect(SCREEN, (255, 241, 31), rect)
            b = b + 1
        b = 0
        a = a + 1


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
        gen_residential()
        gen_commercial()
        gen_industrial()
    pygame.display.update()

# end
