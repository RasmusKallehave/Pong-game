import turtle

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.message = turtle.Turtle()
        self.message.hideturtle()
        self.message.penup()
        self.message.color("white")
        self.message.goto(0, 0)
        self.active = False

    def enter(self):
        if self.active:
            return
        self.active = True
        self.message.write("Press SPACE to start", align="center", font=("courier", 24, "normal"))
        turtle.update()

    def exit(self):
        self.active = False
        self.hide()

    def hide(self):
        self.message.clear()

    def update(self):
        pass  # No continuous updates needed in the menu

    def handle_input(self, key):
        if key == "space":
            self.hide()
            self.game.state_machine.set_state("game_running")