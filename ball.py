import turtle
import time

class Ball:
    def __init__(self, speed = 5):
        self._ball = turtle.Turtle()
        self._ball.speed(0)
        self._ball.shape("square")
        self._ball.color("white")
        self._ball.penup()
        self._ball.goto(0, 0)
        self._dx = speed
        self._dy = speed
        self._start_time = time.time()
        self._speedups_done = 0

    def move(self):
        new_x = self._ball.xcor() + self._dx
        new_y = self._ball.ycor() + self._dy
        self._ball.setx(new_x)
        self._ball.sety(new_y)
        self.maybe_speed_up()

    def bounce_y(self):
        self._dy *= -1

    def bounce_x(self):
        self._dx *= -1

    def reset_position(self):
        self._ball.goto(0, 0)
        self.reset_speed_timer()

    def reset_speed_timer(self):
        self._start_time = time.time()
        self._speedups_done = 0

    def ycor(self):
        return self._ball.ycor()
    
    def xcor(self):
        return self._ball.xcor()
    
    def setx(self, x):
        self._ball.setx(x)

    def sety(self, y):
        self._ball.sety(y)

    def turtle(self):
        return self._ball
    
    def maybe_speed_up(self):
        current_time = time.time()
        elapsed = current_time - self._start_time
        print(f"[DEBUG] Elapsed: {elapsed:.2f} sec, Speedups done: {self._speedups_done}")
        if elapsed >= (self._speedups_done + 1) * 5:
            self._dx *= 1.3
            self._dy *= 1.3
            self._speedups_done += 1
            print(f"[SPEED UP] New dx: {self._dx:.2f}, dy: {self._dy:.2f}")