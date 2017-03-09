class Direction:
    def __init__(self):
        pass

    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class MovementHolder:
    def __init__(self, lead_x, lead_y, movement_delta):
        self.lead_x = lead_x
        self.lead_y = lead_y
        self.change_x = 0
        self.change_y = 0
        self.movement_delta = movement_delta


def change_direction(move_holder, direction):
    if direction == Direction.UP:
        move_holder.change_x = 0
        move_holder.change_y = -move_holder.movement_delta
    elif direction == Direction.RIGHT:
        move_holder.change_x = move_holder.movement_delta
        move_holder.change_y = 0
    elif direction == Direction.DOWN:
        move_holder.change_x = 0
        move_holder.change_y = move_holder.movement_delta
    elif direction == Direction.LEFT:
        move_holder.change_x = -move_holder.movement_delta
        move_holder.change_y = 0


def move(movement_holder):
    movement_holder.lead_x += movement_holder.change_x
    movement_holder.lead_y += movement_holder.change_y


def handle_edges(movement_holder, window_size):
    if movement_holder.lead_x >= window_size or movement_holder.lead_x <= 0:
