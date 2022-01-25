if False:
    from lib.Processing3 import *
    from math import floor

number_of_particle = 2500
incre_ment = 0.5
zoff_incre_ment = 0.004
vector_mag = 1
speed_max = 8
speed_min = 2
column, row = 0, 0
scl = 20
zoff = 0
particles = []
flow_field = []


def setup():
    global column, row, scl, flow_field, number_of_particle, speed_min, speed_max
    size(1200, 1200, P2D)
    background(0)
    column = floor(width / scl) + 1
    row = floor(height / scl) + 1

    for i in range(number_of_particle):
        particles.append(Particle(random(speed_min, speed_max)))


def draw():
    try:
        print(frameRate)
        global incre_ment, row, column, zoff, particles, flow_field, zoff_incre_ment, vector_mag

        yoff = 0

        for y in range(row):
            xoff = 0
            for x in range(column):
                index = x + y * column
                angle = noise(xoff, yoff, zoff) * TWO_PI
                xoff += incre_ment
                v = PVector.fromAngle(angle)
                v.setMag(vector_mag)
                flow_field.append(v)
                # stroke(0, 55)
                # pushMatrix()
                # translate(x * scl, y * scl)
                # rotate(v.heading())
                # #line(0, 0, scl, 0)
                # popMatrix()

            yoff += incre_ment
            zoff += zoff_incre_ment

            for particle in particles:
                particle.follow(flow_field)
                particle.update()
                particle.edges()
                particle.show()

    except Exception as e:
        print(e)


def keyPressed():
    if key == 's':
        saveFrame("img/line-######.png")
        print("Image Saved")

class Particle(object):
    # position = PVector(0, 0)
    # velocity = PVector(0, 0)
    # acceleration = PVector(0, 0)
    # prev_pos = PVector(0, 0)
    # max_speed = 0

    def __init__(self, speed):
        self.position = PVector(random(width/4), random(height/4))
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.max_speed = speed
        self.prev_pos = self.position.copy()

    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.max_speed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def apply_force(self, force):
        self.acceleration.add(force)

    def show(self):
        stroke(0, 255, 0, random(5))
        strokeWeight(1)
        # point(self.position.x, self.position.y)
        line(self.position.x, self.position.y, self.prev_pos.x, self.prev_pos.y)
        self.update_prev_pos()

    def update_prev_pos(self):
        self.prev_pos.x = self.position.x
        self.prev_pos.y = self.position.y

    def edges(self):
        if self.position.x > width:
            self.position.x = 0
            self.update_prev_pos()
        if self.position.x < 0:
            self.position.x = width
            self.update_prev_pos()
        if self.position.y > height:
            self.position.y = 0
            self.update_prev_pos()
        if self.position.y < 0:
            self.position.y = height
            self.update_prev_pos()

    def follow(self, vectors):
        x = floor(self.position.x / scl)
        y = floor(self.position.y / scl)
        index = x + y * column
        if index < len(vectors):
            force = vectors[index]
            self.apply_force(force)
