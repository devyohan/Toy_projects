import turtle

wn = turtle.Screen()
wn.title("Pong game by Dev Yohan")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 2
ball.dy = -2

# A 막대기 위로 이동
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# A 막대기 아래로 이동
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# A 막대기 위로 이동
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# A 막대기 아래로 이동
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Key binding
wn.listen()

# A 플레이어 키
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# B 플레이어 키
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")

# 메인 게임 코드
while True:
    wn.update()

    # 공 움직이기
    ball.setx(ball.xcor() + ball.dx) # 오른쪽으로
    ball.sety(ball.ycor() + ball.dy) # 위로

    # 테두리 검사하기
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1