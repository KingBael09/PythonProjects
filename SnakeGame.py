import pygame
import sys
import time
import random

pygame.init()  # Checking all modules in pygame

# Defining RGB values for variable(tuple)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Fixing Windowsize
dis_width = 600
dis_height = 400
# via pygame  module setting display size(windowsize)
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game LOL')  # Application name

clock = pygame.time.Clock()

snake_block = 10  # pixel size of snake and food
snake_speed = 10  # determined speed of movement

# setting up fonts
font_style = pygame.font.SysFont("calibiri", 25)
score_font = pygame.font.SysFont("calibiri", 35)


def Your_score(score):
    value = score_font.render(
        "Your Score: " + str(score), True, yellow)  # Scoreboard
    dis.blit(value, [225, 0])  # Coordinate of Score board on


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        # inilizing snake block coordinates and rendering


def message(msg, color):  # message function
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():  # main function
    # inilization
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    # random food spawn
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:  # lost game screen
            dis.fill(blue)
            message("You Lost! Press C To Play Again OR Esc to Quit ", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                        pygame.quit()  # same work as quit
                    if event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT:
                    sys.exit()  # quit gameWindow after lost

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.QUIT  # quit gameWindow while during the game
            if event.type == pygame.KEYDOWN:  # movement allotment
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True  # lose condition

        # changing position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)  # filling changed position

        # food spawning
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        # collapse function
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        # Maintaining Score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    sys.exit()


gameLoop()
