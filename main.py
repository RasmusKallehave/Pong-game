import turtle
from GameStates.stateMachine import StateMachine, register_all_states

# Set up screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Set up state machine and register all states
state_machine = StateMachine()
register_all_states(state_machine)

# Key bindings
screen.onkeypress(lambda: state_machine.set_state("game_running"), "space")
screen.listen()

# Start in main menu
state_machine.set_state("main_menu")

# Game loop
def game_loop():
    state_machine.update()
    screen.update()
    screen.ontimer(game_loop, 10)

game_loop()
turtle.mainloop()
