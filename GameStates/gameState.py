class GameState:
    MAIN_MENU = "main_menu"
    GAME_RUNNING = "game_running"
    GAME_OVER = "game_over"

    def __init__(self):
        self.state = GameState.MAIN_MENU

    def is_menu(self):
        return self.state == GameState.MAIN_MENU

    def is_running(self):
        return self.state == GameState.GAME_RUNNING

    def is_over(self):
        return self.state == GameState.GAME_OVER

    def start_game(self):
        self.state = GameState.GAME_RUNNING

    def show_menu(self):
        self.state = GameState.MAIN_MENU

    def game_over(self):
        self.state = GameState.GAME_OVER