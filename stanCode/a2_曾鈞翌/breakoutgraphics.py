"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

這是一個用板子接球的小遊戲
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
SWITCH = False


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-self.ball.width)/2, y=(window_height-self.ball.height)/2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.action)
        onmousemoved(self.paddle_move)
        # Draw bricks
        self.brick_num = 0
        for i in range(0, brick_rows):
            if i < 2:
                color = "red"
            elif 2 <= i < 4:
                color = "orange"
            elif 4 <= i < 6:
                color = "yellow"
            elif 6 <= i < 8:
                color = "green"
            else:
                color = "skyblue"
            for j in range(0, brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.window.add(self.brick,
                                x=0+j*(self.brick.width+brick_spacing),
                                y=brick_offset+i*(self.brick.height+brick_spacing))
        # 記分板
        self.score = 0
        self.label = GLabel(f"Score: {self.score}")
        self.label.font = "-20-bold"
        self.window.add(self.label, x=0, y=self.label.height+BRICK_SPACING)

    @staticmethod
    def brick_number():
        global BRICK_COLS, BRICK_ROWS
        return BRICK_ROWS*BRICK_COLS

    # 移動板子
    def paddle_move(self, mouse):
        if mouse.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x < self.paddle.width:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x-self.paddle.width/2

    # 點擊，給予球速度變化
    def action(self, mouse):
        global SWITCH
        self.is_ball_moving()
        if SWITCH is False:
            self.set_ball_velocity()

    # 判斷球是否移動中(加速度=0)
    def is_ball_moving(self):
        global SWITCH
        if self.__dx != 0:
            SWITCH = True
        return SWITCH

    # 設定球速
    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # 重置球
    def reset_ball(self):
        global SWITCH
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.__dx = 0
        self.__dy = 0
        SWITCH = False

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
