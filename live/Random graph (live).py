import pygame
import random


fps = 90
background_color = (0, 0, 0)
line_color = (0, 110, 255)
window_caption = 'Project - X'

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_size = screen.get_size()
screen_width = screen_size[0]
screen_height = screen_size[1]
pygame.display.set_caption(window_caption)


run = True
clock = pygame.time.Clock()
lines = []
first_x = 0
x = first_x
x_space = 0.07
min_y = 0
max_y = screen_height
first_y = screen_height / 2
y = first_y
scroll_value = 60


def generate_axis():
    global x, y
    x += x_space
    y = y + random.randint(-random.randint(0, 5), random.randint(0, 5))


def draw():
    global lines
    for _ in range(7):
        pos = [x, y]
        generate_axis()
        lines.append(pos)


def reset():
    global x, y, lines
    x = first_x
    y = first_y
    lines = []
    draw()


draw()
while run:
    clock.tick(fps)
    screen.fill(background_color)

    y = lines[-1][1]
    x = lines[-1][0]
    draw()

    for i in range(len(lines)):
        if i + 1 != len(lines):
            pygame.draw.line(screen, line_color, lines[i], lines[i + 1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                reset()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                for i in range(len(lines)):
                    lines[i][1] -= scroll_value
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                for i in range(len(lines)):
                    lines[i][1] += scroll_value
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                for i in range(len(lines)):
                    lines[i][0] += scroll_value
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                for i in range(len(lines)):
                    lines[i][0] -= scroll_value
            if event.key == pygame.K_SPACE:
                reset()
            if event.key == pygame.K_RETURN:
                reset()

    pygame.display.update()
