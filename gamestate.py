import random
import numpy


class Direction:
    def __init__(self):
        pass

    # these are what accounts for direction enums
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class GameState:
    def __init__(self, movement_delta, window_size, block_size, fps):
        self.lead = (window_size / 2, window_size / 2)
        self.change = (0, 0)
        self.movement_delta = movement_delta
        self.window_size = window_size
        self.block_size = block_size
        self.fps = fps
        self.apple = (random.randrange(0, window_size - block_size), random.randrange(0, window_size - block_size))
        self.snake_length = 1
        self.snake_list = []

    game_over = False
    # exit the game?
    game_exit = False

    def set_game_over(self):
        self.game_over = True
        self.game_exit = False

    def set_game_exit(self):
        self.game_over = False
        self.game_exit = True

    def change_direction(self, direction):
        if direction == Direction.UP:
            self.change = (0, -self.movement_delta)
        elif direction == Direction.RIGHT:
            self.change = (self.movement_delta, 0)
        elif direction == Direction.DOWN:
            self.change = (0, self.movement_delta)
        elif direction == Direction.LEFT:
            self.change = (-self.movement_delta, 0)

    def move(self):
        self.lead = tuple(numpy.add(self.lead, self.change))
        if len(self.snake_list) > self.snake_length:
            del self.snake_list[0]
        for segment in self.snake_list[:-1]:
            if segment == self.lead:
                self.set_game_over()

        self.snake_list.append(self.lead)

    def is_beyond_edges(self):
        if self.lead[0] >= self.window_size or self.lead[0] <= 0 \
                or self.lead[1] >= self.window_size or self.lead[1] <= 0:
            return True
        else:
            return False

    def detect_apple_collision(self):
        if (self.apple[0] + self.block_size >= self.lead[0] >= self.apple[0]
            or self.lead[0] + self.block_size >= self.apple[0] >= self.lead[0]) \
                and (self.apple[1] + self.block_size >= self.lead[1] >= self.apple[1]
                     or self.lead[1] + self.block_size >= self.apple[1] >= self.lead[1]):
            self.replace_apple()
            self.snake_length += 1

    def replace_apple(self):
        self.apple = (random.randrange(0, self.window_size - self.block_size),
                      random.randrange(0, self.window_size - self.block_size))

    def reset(self):
        self.lead = (self.window_size / 2, self.window_size / 2)
        self.snake_length = 1
        self.snake_list = []
        self.change = (0, 0)
        self.replace_apple()
        self.game_exit = False
        self.game_over = False
