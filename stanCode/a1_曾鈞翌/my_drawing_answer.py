"""
File: my_drawing
Name: 曾鈞翌
----------------------
TODO:
每天上班，最期待的就是回家啦
不過最近下班都要寫作業上課，只好畫畫抒發一下
背景的是海
是我小時候夢想房子的模樣
一走出門就能看到的遼闊的大海
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GLine
from campy.graphics.gwindow import GWindow

WINDOW_W = 800
WINDOW_H = 500


def main():
    """
    TODO:
    """
    # 背景是海
    window = GWindow(WINDOW_W, WINDOW_H, title="小時候的房子")
    for j in range(0, int(window.height*3.5/10), int(window.height/20)):
        for i in range(0, int(window.width*1.1), int(window.width/20)):
            sea = GOval(window.width*0.7/10, window.width*0.5/10, x=-window.width*0.7/10+i, y=0+1.2*j)
            sea.filled = True
            if j % 2*int(window.width/50) == 0:
                sea.fill_color = "ivory"
                sea.color = "ivory"
                window.add(sea)
            else:
                sea.fill_color = "blue"
                sea.color = "blue"
                window.add(sea)
    # 房子底部
    base = GRect(window.width*4/10, window.height*5/10, x=window.width*5.8/10, y=window.height*5/10)
    base.filled = True
    base.fill_color = "snow"
    base.color = "snow"
    window.add(base)
    # 房子煙囪
    chimney = GRect(window.width*0.5/10, window.height*3.5/10, x=window.width*8.8/10, y=window.height*0.5/10)
    chimney.filled = True
    chimney.fill_color = "gray"
    chimney.color = "gray"
    window.add(chimney)
    chimney1 = GRect(window.width*0.7/10, window.height*0.1/10, x=window.width*8.7/10, y=window.height*0.45/10)
    chimney1.filled = True
    chimney1.fill_color = "brown"
    chimney1.color = "brown"
    window.add(chimney1)
    # 房子屋頂
    roof = GPolygon()
    roof.add_vertex((window.width*5.8/10, window.height*5/10))
    roof.add_vertex((window.width*9.8/10, window.height*5/10))
    roof.add_vertex((window.width*7.8/10, window.height/10))
    roof.filled = True
    roof.fill_color = "sienna"
    roof.color = "sienna"
    window.add(roof)
    door1 = GRect(window.width/10, window.height*2/10, x=window.width*7.3/10, y=window.height*8/10)
    door1.filled = True
    door1.fill_color = "salmon"
    door2 = GOval(window.width*0.07/10, window.width*0.4/10, x=window.width*7.5/10, y=window.height*9/10)
    door2.filled = True
    door2.fill_color = "tomato"
    window.add(door1)
    window.add(door2)
    # 火柴人
    head = GOval(window.width/10, window.width/9, x=window.width*2/10, y=window.height*5/10)
    window.add(head)
    body = GLine(window.width*2.5/10, window.height*5/10+window.width/9, window.width*2.5/10, window.height*9/10)
    window.add(body)
    left_hand = GLine(window.width*1.7/10, window.height*5/10+window.width/9, window.width*2.5/10, window.height*7.8/10)
    window.add(left_hand)
    right_hand = GLine(window.width*3.3/10, window.height*5/10+window.width/9, window.width*2.5/10, window.height*7.8/10)
    window.add(right_hand)
    left_foot = GLine(window.width*2/10, window.height*0.99, window.width*2.5/10, window.height*9/10)
    window.add(left_foot)
    right_foot = GLine(window.width*3/10, window.height*0.99, window.width*2.5/10, window.height*9/10)
    window.add(right_foot)
    # 表情符號
    eye = GLabel("^ ^", x=window.width*2.15/10, y=window.height*6.3/10)
    eye.font = "-30-bold"
    window.add(eye)
    mouth = GLabel("o", x=window.width * 2.4 / 10, y=window.height * 6.6 / 10)
    mouth.font = "-25-bold"
    window.add(mouth)
    # 想說的話
    words = GLabel("放假啦！", x=window.width * 3.3 / 10, y=window.height * 6.6 / 10)
    words.font = "-35-bold"
    words.color = "tomato"
    window.add(words)


if __name__ == '__main__':
    main()
