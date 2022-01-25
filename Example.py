if False:
    from lib.Processing3 import *
dia = 400
angle = float(0.0)

def setup():
    size(900, 900)
    this.surface.setLocation(987, 70)
    strokeCap(CORNER)
    stroke(255)


def draw():
    global angle
    background(0, 40, 65)
    translate(width/2, height/2)
    rotate(angle)
    for a in range(0, 360, 30):
        pushMatrix()
        rotate(radians(a))
        for r in range(0, 180, 8):
            sW = map(cos(radians(r)), -1, 1, 15, 1)
            strokeWeight(sW)
            line(sin(radians(r)) * dia, cos(radians(r)) * dia, sin(radians(-r)) * dia, cos(radians(-r)) * dia)
        popMatrix()
    angle += TWO_PI/720

    noFill()
    stroke(255)
    ellipse(0, 0, dia*2, dia*2)
