import turtle

class PauseMenu:
    def __init__(self, state_machine, **kwargs):
        self.state_machine = state_machine
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.options = ["Resume", "Exit"]
        self.selected = 0
        self.active = False
        self.previous_state = kwargs.get("previous_state")

    def enter(self):
        if self.active:
            return
        self.active = True
        self._draw_menu()
        screen = turtle.Screen()
        screen.listen()
        screen.onkeypress(self._select_up, "Up")
        screen.onkeypress(self._select_down, "Down")
        screen.onkeypress(self._confirm, "Return")

    def exit(self):
        self.active = False
        self.pen.clear()
        screen = turtle.Screen()
        screen.onkeypress(None, "Up")
        screen.onkeypress(None, "Down")
        screen.onkeypress(None, "Return")

    def update(self):
        pass  # Nothing to update during pause

    def _draw_menu(self):
        self.pen.clear()
        self.pen.goto(0, 40)
        self.pen.color("yellow")
        self.pen.write("Game Paused", align="center", font=("Courier", 32, "bold"))
        for index, option in enumerate(self.options):
            self.pen.goto(0, -index * 40)
            style = ("Courier", 24, "bold")
            if index == self.selected:
                self.pen.write(f"> {option} <", align="center", font=style)
            else:
                self.pen.write(option, align="center", font=style)

    def _select_up(self):
        self.selected = (self.selected - 1) % len(self.options)
        self._draw_menu()

    def _select_down(self):
        self.selected = (self.selected + 1) % len(self.options)
        self._draw_menu()

    def _confirm(self):
        if self.options[self.selected] == "Resume":
            print("[PauseMenu] Resuming...")
            self.state_machine.set_state("game_running")
        elif self.options[self.selected] == "Exit":
            print("[PauseMenu] Exiting...")
            turtle.bye()