if False:
    from lib.Processing3 import *


def setup():
    size(600, 600)


def draw():
    import  random as r
    background(0)
    x, y, z = r.random(0, 400), r.random(0, 400), r.random(0, 400)
    fill(255)
    noStroke()
    ellipse(x, y, 8, 8)
