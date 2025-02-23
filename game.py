import pgzrun
import random

TITLE = "Arkanoid"
WIDTH = 800
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 450

DEFAULT_BALL_X = 30
DEFAULT_BALL_Y = 300
BALL_X_SPEED_WHEN_MOVING = 3
BALL_Y_SPEED_WHEN_MOVING = 3

ball = Actor("ballblue.png")
ball.x = DEFAULT_BALL_X
ball.y = DEFAULT_BALL_Y
ball_x_speed = 0
ball_y_speed = 0

bar = Actor("element_blue_rectangle_glossy.png")
bar.x = 120
bar.y = 100
bars_list = []

def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(8):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bars_list.append(bar)
        bar_x += 70

coloured_box_list = ["element_blue_rectangle_glossy.png", "element_green_rectangle_glossy.png","element_red_rectangle_glossy.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50

def draw():
    screen.blit("background.png", (0,0))
    paddle.draw()
    ball.draw()
    

    for bar in bars_list:
        bar.draw()
    

def update():
    global ball_x_speed, ball_y_speed
    if keyboard.q:
        ball_x_speed = 0
        ball_y_speed = 0
    if keyboard.w:
        ball_x_speed = BALL_X_SPEED_WHEN_MOVING
        ball_y_speed = BALL_Y_SPEED_WHEN_MOVING
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5
    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
            rand = random.randint(0,1)
            if rand:
                ball_x_speed *= -1
    if paddle.colliderect(ball):
        ball_y_speed *= -1
        rand = random.randint(0,1)
        if rand:
            ball_x_speed *= -1
    if (ball.y > paddle.y): # paddle didn't catch ball
        reset_bar()

def reset_bar():
    global ball_x_speed, ball_y_speed
    ball_x_speed = 0
    ball_y_speed = 0
    ball.x = DEFAULT_BALL_X
    ball.y = DEFAULT_BALL_Y

def update_ball():
    # ball.x -= 1 # moves the ball left
    # ball.y -= 1 # moves the ball up
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <= 0):
        ball_x_speed *= -1
    if (ball.y >= HEIGHT) or (ball.y <= 0):
        ball_y_speed *= -1

pgzrun.go()
