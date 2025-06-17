import turtle

class GameScreen:
    def __init__(self, width = 800, height = 600, bg_color = "black", title = "Pong"):
        self._screen = turtle.Screen()
        self._screen.title(title)
        self._screen.bgcolor(bg_color)
        self._screen.setup(width = width, height = height)
        self._screen.tracer(0)

    def update(self):
        self._screen.update()

    def listen(self):
        self._screen.listen()

    def on_key(self, key, callback):
        self._screen.onkeypress(callback, key)

    def on_keypress(self, key, callback):
        self._screen.onkeypress(callback, key)

    def on_keyrelease(self, key, callback):
        self._screen.onkeyrelease(callback, key)

    def focus(self):
        self._screen._canvas.focus_force()