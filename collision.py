class CollisionHandler:
    def check_paddle_collision(ball, paddle):
        ball_turtle = ball.turtle()
        paddle_turtle = paddle.get_turtle()

        # Check proximity on x and y axis
        x_distance = abs(ball_turtle.xcor() - paddle_turtle.xcor())
        y_distance = abs(ball_turtle.ycor() - paddle_turtle.ycor())

        return x_distance < 20 and y_distance < 50

    def handle_paddle_bounce(ball, left_paddle, right_paddle):
        if CollisionHandler.check_paddle_collision(ball, right_paddle) and ball.xcor() > 0:
            ball.setx(right_paddle.get_turtle().xcor() - 20)
            ball.bounce_x()

        if CollisionHandler.check_paddle_collision(ball, left_paddle) and ball.xcor() < 0:
            ball.setx(left_paddle.get_turtle().xcor() + 20)
            ball.bounce_x()