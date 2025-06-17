import turtle

class GameWin:
    def __init__(self, state_machine, winner):
        self.state_machine = state_machine
        self.winner = winner
        self.active = False
        self.pen = turtle.Turtle()

    def enter(self):
        if self.active:
            return
        self.active = True

        if "game_running" in self.state_machine.states:
            self.state_machine.states["game_running"].exit()

        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color("green")
        self.pen.goto(0, 0)
        message = f"Player {1 if self.winner == 'left' else 2} wins!\nPress 'r' to restart or \npress 'Escape' to quit game"
        self.pen.write(message, align="center", font=("Counrier", 36, "bold"))

        screen = turtle.Screen()
        screen.listen()
        screen.onkeypress(self.quit_game, "Escape")
        screen.onkeypress(self.restart_game, "r")

    def exit(self):
        self.active = False
        self.pen.clear()
        screen = turtle.Screen()
        screen.onkeypress(None, "Escape")
        screen.onkeypress(None, "r")

    def update(self):
        pass


    def quit_game(self):
        turtle.bye()

    def restart_game(self):
        from GameStates.gameRunning import GameRunning 
        new_game = GameRunning(self.state_machine)
        self.state_machine.states["game_running"] = new_game
        self.state_machine.set_state("game_running")
