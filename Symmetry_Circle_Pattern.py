if False:
    from lib.Processing3 import *

path = []
generation = 3
A = ['F', 'R', 'F']


def setup():
    global generation
    global A
    size(900, 900)
    for i in range(generation):
        for j in A:
            if j == 'F':
                path.append('R')
                path.append('F')
                path.append('L')
                path.append('F')
            else:
                path.append(j)


def draw():
    global path
    print(path)
    translate(width / 2, height / 2)
    my_pen = Pen()
    while len(path) > 0:
        instruction = path.pop()
        strokeWeight(random(10))
        my_pen.move(instruction)
    noLoop()


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

    def move(self, instruction):
        if instruction == 'F':
            self.forward()
        elif instruction == 'L':
            self.left()
        elif instruction == 'R':
            self.right()
