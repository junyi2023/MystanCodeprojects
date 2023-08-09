"""
File: bouncing_ball
Name: 曾鈞翌
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
# 創建視窗，並預先畫出球
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
click = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    # 視窗出現浮球
    # 執行彈跳球程式
    onmouseclicked(check_click)


def check_click(mouse):
    global click
    click += 1
    if click == 1:
        bouncing_ball()


# 彈跳球程式
def bouncing_ball():
    global click
    vy = 0
    # 執行3次
    for i in range(3):
        # 不斷執行，直到球跳出視窗
        while True:
            if ball.x+SIZE < window.width:
                vy += GRAVITY
            if ball.x + SIZE < window.width:
                vy += GRAVITY
                ball.move(dx=VX, dy=vy)
                pause(DELAY)
                if ball.y + SIZE >= window.height:
                    # 避免球掉出視窗
                    ball.y = window.height - SIZE
                    vy = -vy * REDUCE
                    # 確保回彈瞬間速度往上
                    ball.move(dx=VX, dy=vy)
                    pause(DELAY)
            else:
                break
        # 球回原點
        ball.x = START_X
        ball.y = START_Y
    # 歸零計算
    click = 0


if __name__ == "__main__":
    main()
