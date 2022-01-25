if False:
    from lib.Processing3 import *


class Pen(object):
    x, y = 0, 0
    angle = 0
    step = 0

    def __init__(self):
        self.x = 0
        self.y = 0
        self.angle = 0
        self.step = 50

    # Move Forward
    def forward(self):
        new_x = self.x - self.step * sin(radians(self.angle))
        new_y = self.y - self.step * cos(radians(self.angle))
        # Draw line
        line(self.x, self.y, new_x, new_y)
        self.x = new_x
        self.y = new_y

    # Turn Left
    # Turn Right
    def right(self):
        self.angle -= 90

    def left(self):
        self.angle += 90
