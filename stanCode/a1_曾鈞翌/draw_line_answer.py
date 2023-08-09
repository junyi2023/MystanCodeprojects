"""
File: draw_line
Name: 曾鈞翌
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()

# SIZE為空心圓圈半徑
SIZE = 5
# 計算點擊次數
click = 0
# 移除時須使用的共用變數
circle = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
# 執行畫圖程式
    onmouseclicked(check_click)


# 依據點擊次數，判斷執行動作
def check_click(mouse):
    global click
    click += 1
    if click % 2 == 1:
        create_circle(mouse)
    else:
        draw_line(mouse)


# 點擊奇數次畫空心圓
def create_circle(mouse):
    global circle
    circle = GOval(SIZE, SIZE)
    circle.filled = False
    circle.color = "black"
    window.add(circle, x=mouse.x - circle.width / 2, y=mouse.y - circle.width / 2)


# 點擊偶數次，移除圓圈畫線
def draw_line(mouse):
    global circle
    window.remove(circle)
    line = GLine(circle.x, circle.y, mouse.x, mouse.y)
    window.add(line)


if __name__ == "__main__":
    main()
