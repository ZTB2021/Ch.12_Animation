"""
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

"""

import random
import arcade

SW = 600
SH = 600


class Box():
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_box(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_box(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        # bounce ball off of walls
        if self.pos_x > SW - self.rad or self.pos_x < self.rad:
            self.dx *= -1
        if self.pos_y > SH - self.rad or self.pos_y < self.rad:
            self.dy *= -1
        if self.pos_y < self.rad + 10:
            self.col = arcade.color.RED
            self.dy *= -1
            arcade.draw_circle_filled(200, 406, 20, arcade.color.BLUSH)
        if self.pos_x < self.rad + 15:
            self.col = arcade.color.BLUE
            self.dx *= -1
            arcade.draw_circle_filled(200, 406, 20, arcade.color.BARN_RED)
        if self.pos_y > - self.rad - 15 + SW:
            self.col = arcade.color.GOLD
            self.dy *= -1
            arcade.draw_circle_filled(200, 406, 20, arcade.color.BRIGHT_PINK)
        if self.pos_x > - self.rad - 10 + SW:
            self.col = arcade.color.GREEN
            self.dx *= -1
        if self.dx == 0:
            self.dx = 2
        if self.dy == 0:
            self.dy = 2
        if self.pos_x == 0:
            self.pos_x += 15


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.ball = []
        for i in range(20):
            rad = random.randint(3, 15)
            x = random.randint(rad + 10, SW - rad - 5)
            y = random.randint(rad + 10, SH - rad - 5)
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            col = arcade.color.BLACK
            ball = Box(x, y, dx, dy, rad, col)
            self.ball.append(ball)
        self.balls = []
        for i in range(60):
            rad = random.randint(3, 15)
            x = random.randint(rad + 10, SW - rad - 5)
            y = random.randint(rad + 10, SH - rad - 5)
            dx = random.randint(-10, 10)
            dy = random.randint(-10, 10)
            col = arcade.color.BLACK
            self.ball.append(ball)
            if y > - rad - 15 + SW:
                arcade.draw_circle_filled(random.randint(0 + 40, SW - 40), random.randint(0 + 40, SH - 40), 20,
                                          arcade.color.BRICK_RED)
                self.balls.append(ball)
            if y < rad + 15:
                arcade.draw_circle_filled(random.randint(0 + 40, SW - 40), random.randint(0 + 40, SH - 40), 20,
                                          arcade.color.BLUSH)
                self.balls.append(ball)
            if x < rad + 15:
                arcade.draw_circle_filled(random.randint(0 + 40, SW - 40), random.randint(0 + 40, SH - 40), 20,
                                          arcade.color.BARN_RED)
                self.balls.append(ball)
            if y > - rad - 15 + SW:
                arcade.draw_circle_filled(random.randint(0 + 40, SW - 40), random.randint(0 + 40, SH - 40), 20,
                                          arcade.color.BRIGHT_PINK)
                self.balls.append(ball)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball:
            ball.draw_box()
        arcade.draw_rectangle_filled(10, SH / 2, 20, SH - 35, arcade.color.BLUE)
        arcade.draw_rectangle_filled(SW - 10, SH / 2, 20, SH - 35, arcade.color.GREEN)
        arcade.draw_rectangle_filled(SW / 2, SH - 10, SW - 35, 20, arcade.color.GOLD)
        arcade.draw_rectangle_filled(SW / 2, 10, SW - 35, 20, arcade.color.RED)

    def on_update(self, dt):
        for ball in self.ball:
            ball.update_box()
        for ball in self.balls:
            ball.update_box()

def myprogram():
    window = MyGame(SW, SH, "Additive Balls")
    arcade.run()


if __name__ == "__main__":
    myprogram()
