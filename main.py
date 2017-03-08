import pygame
import colors
import constants

# create a window for the game
gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Slither')

gameExit = False


# x position on the screen
lead_x = 300
lead_x_change = 0
# y position on the screen
lead_y = 300
lead_y_change = 0

# how many pixels to move per frame (i.e speed)
movement_delta = 5

clock = pygame.time.Clock()


def change_direction(direction):
    print(direction)
    if direction == constants.Direction.UP:
        lead_x_change = 0
        lead_y_change = -movement_delta
    elif direction == constants.Direction.RIGHT:
        lead_x_change = movement_delta
        lead_y_change = 0
    elif direction == constants.Direction.DOWN:
        lead_x_change = 0
        lead_y_change = movement_delta
    elif direction == constants.Direction.LEFT:
        lead_x_change = -movement_delta
        lead_y_change = 0


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_direction(constants.Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                change_direction(constants.Direction.RIGHT)
            elif event.key == pygame.K_DOWN:
                change_direction(constants.Direction.DOWN)
            elif event.key == pygame.K_UP:
                change_direction(constants.Direction.UP)

    # if lead_x >= 800 or lead_x <= 0 or lead_y >= 600 or lead_y <= 0:
    #     lead_x_change =
    #     lead_y_change = 0
    lead_x += lead_x_change
    lead_y += lead_y_change
    gameDisplay.fill(colors.white)
    pygame.draw.rect(gameDisplay, colors.black, [lead_x, lead_y, 10, 10])
    pygame.display.update()
    clock.tick(60)

# un-initialize pygame
pygame.quit()

# exit python
quit()
