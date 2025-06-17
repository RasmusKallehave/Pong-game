import turtle

class Paddle:
    def __init__(self, x_position, y_limit = 250):
        self._y_limit = y_limit
        self._paddle = turtle.Turtle()
        self._paddle.speed(0)
        self._paddle.shape("square")
        self._paddle.color("white")
        self._paddle.shapesize(stretch_wid = 5, stretch_len = 1)
        self._paddle.penup()
        self._paddle.goto(x_position, 0)

        self._moving_up = False
        self._moving_down = False
        self._move_speed = 3
        self._move_loop_active = False

    def move_up(self):
        y = self._paddle.ycor()
        if y < self._y_limit:
            self._paddle.sety(y + self._move_speed)

    def move_down(self):
        y = self._paddle.ycor()
        if y > -self._y_limit:
            self._paddle.sety(y - self._move_speed)

    def start_move_up(self):
        self._moving_up = True
        if not self._move_loop_active:
            self._continuous_move()

    def stop_move_up(self):
        self._moving_up = False

    def start_move_down(self):
        self._moving_down = True
        if not self._move_loop_active:
            self._continuous_move()

    def stop_move_down(self):
        self._moving_down = False

    def _continuous_move(self):
        if not self._move_loop_active:
            self._move_loop_active = True

        if self._moving_up:
            self.move_up()
        if self._moving_down:
            self.move_down()

        if self._moving_up or self._moving_down:
            turtle.ontimer(self._continuous_move, 10)
        else:
            self._move_loop_active = False

    def get_turtle(self):
        return self._paddle
