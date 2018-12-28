import turtle

wn = turtle.Screen()
wn.title("Pong game by Dev Yohan")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# 메인 게임 코드
while True:
    wn.update()