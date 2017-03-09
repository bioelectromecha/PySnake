import pygame
import colors
import movement
import gamestate
import random

# the game window size in pixels
window_size = 800
# the pixel size of each block on the screen
block_size = 10
# how many frames per second the game should draw
frames_per_second = 60
# how many pixels to advance per frame
distance_per_frame = 5
# game over screen wait time
game_over_wait = 1

# initialize pygame
pygame.init()
# create a window for the game
gameDisplay = pygame.display.set_mode((window_size, window_size))
# set the label for the window
pygame.display.set_caption('Slither')

# set to clock to control the fps
clock = pygame.time.Clock()


def message_to_screen(msg, color, font):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_size / 2, window_size / 2])


rand_apple_x = random.randrange(0, window_size - block_size)
rand_apple_y = -random.randrange(0, window_size - block_size)


def game_loop():

    # holds the game state (i.e game over or quit or play)
    game_state = gamestate.GameState()
    # the font with which to print out stuff to the user
    font = pygame.font.SysFont(None, 25)
    # init the initial location and movement params
    move_holder = movement.MovementHolder(window_size / 2, window_size / 2, distance_per_frame)

    # main game loop
    while not game_state.game_exit:

        while game_state.game_over:
            handle_game_over(game_state, font)

        # keypress event handling and logic
        handle_movement_events(game_state, move_holder)
        # update position
        movement.move(move_holder)
        # check for movement beyond edges
        if (not game_state.game_exit) and movement.is_beyond_edges(move_holder, window_size):
            game_state.set_game_over()

        # draw stuff on screen
        draw(move_holder)

        pygame.draw.rect(gameDisplay, colors.black, [move_holder.lead_x, move_holder.lead_y, block_size, block_size])

    # un-initialize pygame
    pygame.quit()

    # exit python
    quit()


def handle_game_over(game_state, font):
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


def handle_movement_events(game_state, move_holder):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.set_game_exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement.change_direction(move_holder, movement.Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                movement.change_direction(move_holder, movement.Direction.RIGHT)
            elif event.key == pygame.K_DOWN:
                movement.change_direction(move_holder, movement.Direction.DOWN)
            elif event.key == pygame.K_UP:
                movement.change_direction(move_holder, movement.Direction.UP)


def draw(move_holder):
    gameDisplay.fill(colors.white)
    pygame.draw.rect(gameDisplay, colors.blue, [rand_apple_x, rand_apple_y, block_size, block_size])
    pygame.draw.rect(gameDisplay, colors.black, [move_holder.lead_x, move_holder.lead_y, block_size, block_size])
    pygame.display.update()
    clock.tick(frames_per_second)

# run the game
game_loop()
