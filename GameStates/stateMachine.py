class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        self.states[name] = state

    def set_state(self, name, **kwargs):
        print(f"[StateMachine] Switching to: {name}")
        if self.current_state and hasattr(self.current_state, 'exit'):
            self.current_state.exit()

        self.current_state = self.states[name]
        if hasattr(self.current_state, 'enter'):
            self.current_state.enter(**kwargs)

    def update(self):
        if self.current_state and hasattr(self.current_state, 'update'):
            self.current_state.update()

    def handle_input(self, input_event):
        print(f"[StateMachine] handle_input received: {input_event}")
        if self.current_state and hasattr(self.current_state, 'handle_input'):
            self.current_state.handle_input(input_event)
