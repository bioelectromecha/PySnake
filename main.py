import pygame
import colors
import movement
import math

# the game window size in pixels
window_size = 800
# the pixel size of each block on the screen
block_size = 10
# how many frames per second the game should draw
frames_per_second = 60
# how many pixels to advance per frame
distance_per_frame = 5

# create a window for the game
gameDisplay = pygame.display.set_mode((window_size, window_size))
# set the label for the window
pygame.display.set_caption('Slither')
# init the initial location and movement params
move_holder = movement.MovementHolder(math.floor(window_size/2), math.floor(window_size/2), distance_per_frame)
# set to clock to control the fps
clock = pygame.time.Clock()

# the loop closes the window when this gets set to True
gameExit = False

# main game loop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement.change_direction(move_holder, movement.Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                movement.change_direction(move_holder, movement.Direction.RIGHT)
            elif event.key == pygame.K_DOWN:
                movement.change_direction(move_holder, movement.Direction.DOWN)
            elif event.key == pygame.K_UP:
                movement.change_direction(move_holder, movement.Direction.UP)

    # if lead_x >= 800 or lead_x <= 0 or lead_y >= 600 or lead_y <= 0:
    #     lead_x_change =
    #     lead_y_change = 0

    movement.move(move_holder)
    gameDisplay.fill(colors.white)
    pygame.draw.rect(gameDisplay, colors.black, [move_holder.lead_x, move_holder.lead_y, block_size, block_size])
    pygame.display.update()
    clock.tick(frames_per_second)

# un-initialize pygame
pygame.quit()

# exit python
quit()
