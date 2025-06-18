class StateMachine:
    def __init__(self):
        self.state_classes ={}
        self.states = {}
        self.current_state = None

        self.current_state_name = None

    def register_state_class(self, name, state_cls):
        self.state_classes[name] = state_cls

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name, **kwargs):
        print(f"[StateMachine] Switching to: {name}")
        if self.current_state and hasattr(self.current_state, 'exit'):
            self.current_state.exit()

        if name not in self.states and name in self.state_classes:
            self.states[name] = self.state_classes[name](self)

        self.current_state = self.states[name]
        self.current_state_name = name
        if hasattr(self.current_state, 'enter'):
            self.current_state.enter(**kwargs)

    def update(self):
        if self.current_state and hasattr(self.current_state, 'update'):
            self.current_state.update()

    def handle_input(self, input_event):
        print(f"[StateMachine] handle_input received: {input_event}")
        if self.current_state and hasattr(self.current_state, 'handle_input'):
            self.current_state.handle_input(input_event)

# Import game state classes
from GameStates.gameRunning import GameRunning
from GameStates.mainMenu import MainMenu
from GameStates.gameWin import GameWin
from GameStates.pauseMenu import PauseMenu

# Helper function to register all states
def register_all_states(state_machine):
    state_machine.register_state_class("game_running", GameRunning)
    state_machine.register_state_class("main_menu", MainMenu)
    state_machine.register_state_class("game_win", GameWin)
    state_machine.register_state_class("pause", lambda sm, **kwargs: PauseMenu(sm, **kwargs))
    