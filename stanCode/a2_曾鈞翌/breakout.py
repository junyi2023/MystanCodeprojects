"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

這是一個用板子接球的小遊戲，
有些疑問，如果要判斷磚塊的顏色，
是需要導入simpleimage的套件去抓取顏色嗎?

如果
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
LIVE = "★"


def main():
    global NUM_LIVES, LIVE
    graphics = BreakoutGraphics()
    brick_num = graphics.brick_number()
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        switch = graphics.is_ball_moving()
        graphics.label.text = f"Score: {graphics.score} {LIVE * NUM_LIVES}"
        if NUM_LIVES > 0:
            while switch:
                graphics.ball.move(dx=vx, dy=vy)
                pause(FRAME_RATE)
                # 球掉下去就結束
                if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                    NUM_LIVES -= 1
                    graphics.reset_ball()
                    break
                # 假設消滅全部磚塊，獲勝結束
                if graphics.score == brick_num:
                    graphics.reset_ball()
                    graphics.label.text = f"恭喜完成作業，闖關成功"
                    break
                # 如果球撞到東西的話
                for i in range(2):
                    for j in range(2):
                        position = graphics.window.get_object_at(x=graphics.ball.x+i*2*graphics.window.width,
                                                                 y=graphics.ball.y+j*2*graphics.window.height)
                        if position is not None:
                            if position is graphics.paddle:
                                vy = -vy
                                graphics.ball.y = graphics.paddle.y
                                graphics.ball.move(dx=vx, dy=vy)
                            elif position is graphics.label:
                                continue
                            # 消除磚塊
                            else:
                                graphics.window.remove(position)
                                graphics.score += 1
                                graphics.label.text = f"Score: {graphics.score} {LIVE*NUM_LIVES}"
                                vy = - vy
                                graphics.ball.move(dx=vx, dy=vy)
                # 如果球碰到視窗的話
                if graphics.ball.x <= 0:
                    vx = -vx
                elif graphics.ball.x >= graphics.window.width - graphics.ball.width:
                    vx = -vx
                elif graphics.ball.y <= 0:
                    vy = -vy
        else:
            graphics.label.text = f"闖關失敗，再試一次吧"
            graphics.reset_ball()
            break


if __name__ == '__main__':
    main()
