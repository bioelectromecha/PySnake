class GameState:
    def __init__(self):
        pass
    # show the game over screen?
    game_over = False
    # exit the game?
    game_exit = False

    def set_game_over(self):
        self.game_over = True
        self.game_exit = False

    def set_game_exit(self):
        self.game_over = False
        self.game_exit = True
