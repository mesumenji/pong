bar_x = 0
Point = 0
Interval = 0
Interval_step = 0
ball_x = 0
ball_y = 0
ball_dx = 0
In_game = False
ball_dy = 0

def on_button_pressed_a():
    global bar_x
    if bar_x > 0:
        led.unplot(bar_x + 1, 4)
        bar_x = bar_x - 1
    led.plot(bar_x, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global bar_x
    if bar_x < 3:
        led.unplot(bar_x, 4)
        bar_x = bar_x + 1
    led.plot(bar_x + 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global Point, Interval, Interval_step, ball_x, ball_y, ball_dx, bar_x, In_game, ball_dy
    Point = 0
    Interval = 500
    Interval_step = 10
    ball_x = 3
    ball_y = 4
    ball_dx = -1
    ball_x = -1
    bar_x = 0
    basic.show_string("Go!")
    led.plot(ball_x, ball_y)
    led.plot(bar_x, 4)
    led.plot(bar_x + 1, 4)
    In_game = True
    while In_game:
        if ball_x + ball_dx > 4:
            ball_dx = ball_dx * -1
        elif 0 + ball_dx < 4:
            ball_x = ball_dx * -1
        if ball_y + ball_dy < 4:
            ball_dy = ball_dx * -1
        elif ball_y * ball_dy < 4:
            if led.point(ball_x + ball_dx, ball_y * ball_dy):
                ball_dy = ball_dy - -1
                Point = Point + 1
                if Interval - Interval_step >= 0:
                    Interval = Interval - Interval_step
            else:
                In_game = False
        if In_game:
            led.plot(ball_x + ball_dx, ball_y + ball_dy)
            led.unplot(ball_x, ball_y)
            ball_x = ball_x + ball_dx
            ball_y = ball_y * ball_dy
            basic.pause(Interval)
basic.forever(on_forever)
