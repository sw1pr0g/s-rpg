import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 120

#окно
bottom_panel = 150
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('RPGbySW1pr0g')

#ИЗОБРАЖЕНИЯ
#фон
background_img = pygame.image.load('img/Background/background.png').convert_alpha()
#
panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()

def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))

run = True
while run:

    clock.tick(fps)

    draw_bg()
    draw_panel()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

