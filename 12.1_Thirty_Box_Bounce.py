"""
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second.
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
"""


import arcade
import random

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
            x = random.randint(width, SW-width)
            y = random.randint(height, SH-height)
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
