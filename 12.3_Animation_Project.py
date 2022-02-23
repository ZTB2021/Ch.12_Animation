'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''

import random
import arcade
SW = 600
SH = 600


class Box():
    def __init__(self, pos_x, pos_y, dx, dy, width, height, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.col = col

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col)

    def update_box(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        # bounce ball off of walls
        if self.pos_x > SW - self.width or self.pos_x < self.width:
            self.dx *= -1
        if self.pos_y > SH - self.width or self.pos_y < self.width:
            self.dy *= -1
        if self.pos_y < self.width + 10:
            self.col = arcade.color.RED
            self.dy *= -1
        if self.pos_x < self.width + 10:
            self.col = arcade.color.BLUE
            self.dx *= -1
        if self.pos_y > - self.width - 10 + SW:
            self.col = arcade.color.GOLD
            self.dy *= -1
        if self.pos_x > - self.width - 10 + SW:
            self.col = arcade.color.GREEN
            self.dx *= -1
        if self.dx == 0:
            self.dx = 1
        if self.dy == 0:
            self.dy = 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.box = []
        for i in range(30):
            height = random.randint(5, 25)
            width = height
            x = random.randint(width, SW - width)
            y = random.randint(height, SH - height)
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            col = arcade.color.BLACK
            box = Box(x, y, dx, dy, width, height, col)
            self.box.append(box)

    def on_draw(self):
        arcade.start_render()
        for box in self.box:
            box.draw_box()
        arcade.draw_rectangle_filled(10, SH / 2, 20, SH - 35, arcade.color.BLUE)
        arcade.draw_rectangle_filled(SW - 10, SH / 2, 20, SH - 35, arcade.color.GREEN)
        arcade.draw_rectangle_filled(SW / 2, SH - 10, SW - 35, 20, arcade.color.GOLD)
        arcade.draw_rectangle_filled(SW / 2, 10, SW - 35, 20, arcade.color.RED)

    def on_update(self, dt):
        for box in self.box:
            box.update_box()


def myprogram():
    window = MyGame(SW, SH, "30 Boxes")
    arcade.run()


if __name__ == "__main__":
    myprogram()
