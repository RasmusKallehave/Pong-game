import turtle

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

    def move(self):
        new_x = self._ball.xcor() + self._dx
        new_y = self._ball.ycor() + self._dy
        self._ball.setx(new_x)
        self._ball.sety(new_y)

    def bounce_y(self):
        self._dy *= -1

    def bounce_x(self):
        self._dx *= -1

    def reset_position(self):
        self._ball.goto(0, 0)

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
    
