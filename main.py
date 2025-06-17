import turtle
from GameStates.stateMachine import StateMachine
from GameStates.mainMenu import MainMenu
from GameStates.gameRunning import GameRunning

# Set up screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Set up state machine
state_machine = StateMachine()

# Create and add states
menu_state = MainMenu(game=None)  # Placeholder
game_state = GameRunning(state_machine)

# Inject game into menu now that it's created
menu_state.game = game_state
game_state.menu = menu_state

state_machine.add_state("main_menu", menu_state)
state_machine.add_state("game_running", game_state)

# Updated set_state method with exit call
def new_set_state(name):
    print(f"[StateMachine] Switching to: {name}")
    if name in state_machine.states:
        if state_machine.current_state and hasattr(state_machine.current_state, 'exit'):
            state_machine.current_state.exit()
        state_machine.current_state = state_machine.states[name]
        state_machine.current_state_name = name
        if hasattr(state_machine.current_state, 'enter'):
            state_machine.current_state.enter()

state_machine.set_state = new_set_state

screen.onkeypress(lambda: state_machine.set_state("game_running"), "space")
screen.listen()

state_machine.set_state("main_menu")

# Game loop
def game_loop():
    state_machine.update()
    screen.update()
    screen.ontimer(game_loop, 10)

game_loop()
turtle.mainloop()
