import turtle

class Score:
    def __init__(self):
        self.left_score = 0
        self.right_score = 0
        self.winning_score = 5
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.waiting_for_restart = False
        self.update_display()

    def update_display(self):
        self.pen.clear()
        score_text = f"Player 1: {self.left_score} Player 2: {self.right_score}"
        self.pen.write(score_text, align="center", font=("Courier", 24, "normal"))

    def increase_left(self):
        self.left_score += 1
        self.update_display()
        self.waiting_for_restart = True
        return self.check_winner()

    def increase_right(self):
        self.right_score += 1
        self.update_display()
        self.waiting_for_restart = True
        return self.check_winner()
    
    def check_winner(self):
        if self.left_score >= self.winning_score:
            return "left"
        elif self.right_score >= self.winning_score:
            return "right"
        return None
    
    def is_waiting(self):
        return self.waiting_for_restart

    def reset(self):
        self.left_score = 0
        self.right_score = 0
        self.waiting_for_restart = False
        self.update_display()