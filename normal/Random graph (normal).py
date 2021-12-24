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
first_x = 0
x = first_x
x_space = 0.07
min_y = 0
max_y = screen_height
first_y = screen_height / 2
y = first_y
scroll_value = 60
lines = []


def init_lines():
    global lines
    lines = []


def generate_axis():
    global x, y
    x += x_space
    y = y + random.randint(-random.randint(0, 5), random.randint(0, 5))


def draw():
    global lines
    for _ in range(30000):
        start_pos = [x, y]
        generate_axis()
        end_pos = [x, y]
        lines.append(start_pos)
        lines.append(end_pos)


init_lines()
draw()


while run:
    clock.tick(fps)
    screen.fill(background_color)

    for i in range(len(lines)):
        if i + 1 != len(lines):
            pygame.draw.line(screen, line_color, lines[i], lines[i + 1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = first_x
                y = first_y
                init_lines()
                draw()
            elif event.button == 2:
                init_lines()
            elif event.button == 3:
                y = lines[-1][1]
                x = lines[-1][0]
                draw()
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
                init_lines()

    pygame.display.update()
