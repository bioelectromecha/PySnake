import pygame
import colors
import gamestate
import time


# initialize pygame
pygame.init()
# create a window for the game

FRAMES_PER_SECOND = 30
SEGMENT_SIZE = 20
APPLE_SIZE = 30
WINDOW_SIZE = 600
PIXELS_PER_FRAME = 10
SNAKE_IMG = pygame.image.load('snake_head.png')
APPLE_IMG = pygame.image.load('snake_apple.png')
WINDOW_NAME = 'Slither'
WINDOW_ICON = pygame.image.load('snake_apple.png')
# the font with which to print out stuff to the user
FONT_HEADER = pygame.font.SysFont(None, 35)
FONT_SUB_HEADER = pygame.font.SysFont(None, 25)


# holds the game state (i.e game over or quit or play)
game_state = gamestate.GameState(PIXELS_PER_FRAME, WINDOW_SIZE, SEGMENT_SIZE, FRAMES_PER_SECOND, SNAKE_IMG, APPLE_SIZE)

# to print something out : print "lala {} lulu {}".format(arg1, arg2)

gameDisplay = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
# set the label for the window
pygame.display.set_caption(WINDOW_NAME)
# set the icon for the window
pygame.display.set_icon(WINDOW_ICON)
# set to clock to control the fps
clock = pygame.time.Clock()


def message_to_screen(msg, color, font, displace_y):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [game_state.window_size / 2 - screen_text.get_width()/2,
                                   game_state.window_size / 2 - screen_text.get_height()/2 + displace_y])


def game_loop():
    # reset the state of the game
    game_state.reset()

    # main game loop
    while not game_state.game_exit:

        while game_state.game_intro:
            handle_game_intro()

        while game_state.game_over:
            handle_game_over()

        # keypress event handling and logic
        handle_movement_events()
        # update position
        game_state.move()
        # update apple if eaten
        game_state.detect_apple_collision()
        # game over if snake crosses itself
        game_state.detect_self_collision()
        # check for movement beyond edges
        if (not game_state.game_exit) and game_state.is_beyond_edges():
            game_state.set_game_over()

        # draw stuff on screen
        draw()

    # un-initialize pygame
    pygame.quit()

    # exit python
    quit()


def handle_game_over():
    gameDisplay.fill(colors.white)
    message_to_screen("GAME OVER!", colors.red, FONT_HEADER, -25)
    message_to_screen("Press C to play again or Q to quit", colors.red, FONT_SUB_HEADER, 25)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.set_game_exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_state.set_game_exit()
            elif event.key == pygame.K_c:
                game_loop()


def handle_game_intro():
    gameDisplay.fill(colors.snake_green)
    font_header = pygame.font.SysFont(None, 50)
    font_subheader = pygame.font.SysFont(None, 25)
    message_to_screen("Hello!", colors.white, font_header, -25)
    message_to_screen("Eat apples to win!", colors.white, font_subheader, 25)
    pygame.display.update()
    time.sleep(2)
    game_state.game_intro = False


def handle_movement_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.set_game_exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_state.set_game_exit()
            elif event.key == pygame.K_LEFT:
                game_state.change_direction(gamestate.Direction.LEFT)
                game_state.head_image = change_head_img_direction(SNAKE_IMG, gamestate.Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                game_state.change_direction(gamestate.Direction.RIGHT)
                game_state.head_image = change_head_img_direction(SNAKE_IMG, gamestate.Direction.RIGHT)
            elif event.key == pygame.K_DOWN:
                game_state.change_direction(gamestate.Direction.DOWN)
                game_state.head_image = change_head_img_direction(SNAKE_IMG, gamestate.Direction.DOWN)
            elif event.key == pygame.K_UP:
                game_state.change_direction(gamestate.Direction.UP)
                game_state.head_image = change_head_img_direction(SNAKE_IMG, gamestate.Direction.UP)


def draw():
    gameDisplay.fill(colors.white)

    # draw the apple
    gameDisplay.blit(APPLE_IMG, [game_state.apple[0], game_state.apple[1]])

    # draw the snake
    for pos in game_state.snake_list[:-1]:
        pygame.draw.rect(gameDisplay, colors.snake_green,
                         [pos[0], pos[1], game_state.block_size, game_state.block_size])

    gameDisplay.blit(game_state.head_image, [game_state.snake_list[-1][0], game_state.snake_list[-1][1]])

    #show the score
    score = FONT_HEADER.render('score: '+str(game_state.snake_length-1), True, colors.red)
    gameDisplay.blit(score, [WINDOW_SIZE-score.get_width()*1.5, score.get_height()/2])

    pygame.display.update()
    clock.tick(game_state.fps)


def change_head_img_direction(img, direction):
    if direction == gamestate.Direction.UP:
        head = pygame.transform.rotate(img, 90)
    elif direction == gamestate.Direction.RIGHT:
        head = img
    elif direction == gamestate.Direction.DOWN:
        head = pygame.transform.rotate(img, 270)
    elif direction == gamestate.Direction.LEFT:
        head = pygame.transform.rotate(img, 180)
    return head


# run the game
game_loop()
