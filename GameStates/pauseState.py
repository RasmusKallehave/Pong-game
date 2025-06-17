import turtle
class PauseState:
    def __init__(self, state_machine, previous_state_instance):
        self.state_machine = state_machine
        self.previous_state = previous_state_instance
        self.message = turtle.Turtle()
        self.message.hideturtle()
        self.message.penup()
        self.message.color("white")
        self.message.goto(0, 0)
        self.selection = 0  # 0 = Resume, 1 = Exit
        self.options = ["Resume", "Exit"]
        self.active = False

    def enter(self):
        if self.active:
            return
        self.active = True
        self.draw_menu()
        screen = turtle.Screen()
        screen.listen()
        screen.onkeypress(lambda: self.state_machine.handle_input("Up"), "Up")
        screen.onkeypress(lambda: self.state_machine.handle_input("Down"), "Down")
        screen.onkeypress(lambda: self.state_machine.handle_input("Return"), "Return")
        turtle.update()

    def draw_menu(self):
        self.message.clear()
        for i, option in enumerate(self.options):
            self.message.goto(0, 40 - i * 40)
            prefix = "> " if i == self.selection else "  "
            self.message.write(prefix + option, align="center", font=("Courier", 24, "normal"))

    def update(self):
        pass  # No updates during pause

    def handle_input(self, key):
        print(f"[PauseState] handle_input received: {key}")
        if key == "Up":
            self.selection = (self.selection - 1) % len(self.options)
            self.draw_menu()
            turtle.update()
        elif key == "Down":
            self.selection = (self.selection + 1) % len(self.options)
            self.draw_menu()
            turtle.update()
        elif key == "Return":
            if self.selection == 0:
                self.message.clear()
                print("[PauseState] Resuming game...")
                self.state_machine.current_state = self.previous_state
                self.previous_state.enter()
            elif self.selection == 1:
                turtle.bye()
    def exit(self):
        screen = turtle.Screen()
        for key in ["Up", "Down", "Return"]:
            screen.onkeypress(None, key)
        self.active = False