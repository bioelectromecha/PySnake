import pygame
import colors
import gamestate

# holds the game state (i.e game over or quit or play)
game_state = gamestate.GameState(3, 600, 10, 60)

# to print something out : print "lala {} lulu {}".format(arg1, arg2)

# TODO make the apple collision detection and rejuvenation function etc
# initialize pygame
pygame.init()
# create a window for the game
gameDisplay = pygame.display.set_mode((game_state.window_size, game_state.window_size))
# set the label for the window
pygame.display.set_caption('Slither')

# set to clock to control the fps
clock = pygame.time.Clock()


def message_to_screen(msg, color, font):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [game_state.window_size / 2, game_state.window_size / 2])


def game_loop():

    # reset the state of the game
    game_state.reset()

    # main game loop
    while not game_state.game_exit:

        while game_state.game_over:
            handle_game_over()

        # keypress event handling and logic
        handle_movement_events()
        # update position
        game_state.move()
        # update apple if eaten
        game_state.detect_apple_collision()
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
    # the font with which to print out stuff to the user
    font = pygame.font.SysFont(None, 25)
    gameDisplay.fill(colors.white)
    message_to_screen("GAME OVER! Press C to play again or Q to quit", colors.red, font)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.set_game_exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_state.set_game_exit()
            elif event.key == pygame.K_c:
                game_loop()


def handle_movement_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.set_game_exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_state.set_game_exit()
            elif event.key == pygame.K_LEFT:
                game_state.change_direction(gamestate.Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                game_state.change_direction(gamestate.Direction.RIGHT)
            elif event.key == pygame.K_DOWN:
                game_state.change_direction(gamestate.Direction.DOWN)
            elif event.key == pygame.K_UP:
                game_state.change_direction(gamestate.Direction.UP)


def draw():
    gameDisplay.fill(colors.white)
    pygame.draw.rect(gameDisplay, colors.red,
                     [game_state.apple[0], game_state.apple[1], game_state.block_size, game_state.block_size])

    # draw the snake
    for pos in game_state.snake_list:
        pygame.draw.rect(gameDisplay, colors.green,
                         [pos[0], pos[1], game_state.block_size, game_state.block_size])

    pygame.display.update()
    clock.tick(game_state.fps)


# run the game
game_loop()
