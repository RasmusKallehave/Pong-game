from GameStates.mainMenu import MainMenu
from screen import GameScreen
from paddle import Paddle
from ball import Ball
from collision import CollisionHandler
from GameStates.gameState import GameState
from score import Score
from GameStates.gameWin import GameWin


class GameRunning:
    def __init__(self, state_machine):
        self.active = False
        self.state_machine = state_machine
        self.state = GameState()
        self.screen = GameScreen()
        self.initialized = False # track first-time setup
        self.score = None
        self.waiting_for_continue = False

    def bind_keys(self):
        turtle_screen = self.screen._screen
        turtle_screen.onkeypress(lambda: self.left_paddle.start_move_up(), "w")
        turtle_screen.onkeyrelease(lambda: self.left_paddle.stop_move_up(), "w")
        turtle_screen.onkeypress(lambda: self.left_paddle.start_move_down(), "s")
        turtle_screen.onkeyrelease(lambda: self.left_paddle.stop_move_down(), "s")
        turtle_screen.onkeypress(lambda: self.right_paddle.start_move_up(), "Up")
        turtle_screen.onkeyrelease(lambda: self.right_paddle.stop_move_up(), "Up")
        turtle_screen.onkeypress(lambda: self.right_paddle.start_move_down(), "Down")
        turtle_screen.onkeyrelease(lambda: self.right_paddle.stop_move_down(), "Down")

    def unbind_keys(self):
        turtle_screen = self.screen._screen
        for key in ["w", "s", "Up", "Down"]:
            turtle_screen.onkeypress(None, key)
            turtle_screen.onkeyrelease(None, key)

    def enter(self):
        if self.active:
            return
        self.active = True
        if not self.initialized:
            self.left_paddle = Paddle(-350)
            self.right_paddle = Paddle(350)
            self.ball = Ball()
            self.state.start_game()
            self.score = Score()
            self.initialized = True
        else:
            self.left_paddle._paddle.showturtle()
            self.right_paddle._paddle.showturtle()
            self.ball._ball.showturtle()
            self.score.pen.clear()
            self.score.draw()

        turtle_screen = self.screen._screen
        turtle_screen.listen()
        turtle_screen.onkeypress(lambda: self.continue_after_point(), "space")
        if not self.waiting_for_continue:
            self.bind_keys()

    def exit(self):
        turtle_screen = self.screen._screen
        for key in ["w", "s", "Up", "Down"]:
            turtle_screen.onkeypress(None, key)
            turtle_screen.onkeyrelease(None, key)
        turtle_screen.onkeypress(None, "space")
        if hasattr(self, "left_paddle"):
            self.left_paddle._paddle.hideturtle()
        if hasattr(self, "right_paddle"):
            self.right_paddle._paddle.hideturtle()
        if hasattr(self, "ball"):
            self.ball._ball.hideturtle()
        if hasattr(self, "score"):
            self.score.pen.clear()
        self.active = False

    def continue_after_point(self):
        if self.waiting_for_continue:
            self.waiting_for_continue = False
            self.left_paddle.enable_movement()
            self.right_paddle.enable_movement()
            self.bind_keys()

    def start_game(self):
        self.left_paddle = Paddle(-350)
        self.right_paddle = Paddle(350)
        self.ball = Ball()
        self.state.start_game()

    def quit_game(self):
        self.state.game_over()

    def update(self):
        if self.waiting_for_continue:
            self.screen.update()
            return

        if self.state.is_running():
            self.ball.move()
            CollisionHandler.handle_paddle_bounce(self.ball, self.left_paddle, self.right_paddle)

            if self.ball.ycor() > 290 or self.ball.ycor() < -290:
                self.ball.bounce_y()

            winner = None
            if self.ball.xcor() > 390:
                winner = self.score.increase_right()
                self.ball.reset_position()
                self.left_paddle.reset_position()
                self.right_paddle.reset_position()
                self.unbind_keys()
                self.left_paddle.disable_movement()
                self.right_paddle.disable_movement()
                self.waiting_for_continue = True
            elif self.ball.xcor() < -390:
                winner = self.score.increase_left()
                self.ball.reset_position()
                self.left_paddle.reset_position()
                self.right_paddle.reset_position()
                self.unbind_keys()
                self.left_paddle.disable_movement()
                self.right_paddle.disable_movement()
                self.waiting_for_continue = True

            if winner:
                if hasattr(self, "left_paddle"):
                    self.left_paddle._paddle.hideturtle()
                if hasattr(self, "right_paddle"):
                    self.right_paddle._paddle.hideturtle()
                if hasattr(self, "ball"):
                    self.ball._ball.hideturtle()
                if hasattr(self, "score"):
                    self.score.pen.clear()
                self.state_machine.states["game_win"] = GameWin(self.state_machine, winner)
                self.state_machine.set_state("game_win")
                del self.state_machine.states["game_running"]
                return

            self.screen.update()

    def handle_input(self, key):
        if key == "Escape":
            self.state_machine.set_state("pause", previous_state=self)