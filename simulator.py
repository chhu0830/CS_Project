#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math
import os
from utils.om2m import create_container, create_content_instance, get_data

class Car(object):
    def __init__(self, idx=None):
        self.idx = idx
        self.speed = int(50 + np.random.random_sample() * 50)        # 50 < speed < 100
        self.x = 0
        self.y = 0
        create_container("COMMAND", str(idx))

    def move(self):
        self.x += self.speed

    def faster(self):
        self.speed += 5

    def slower(self):
        self.speed -= 5

cars = [Car(0)]
maxspeed = 100

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 10000))
tunnel, = ax.plot([car.x for car in cars],
                  [car.y for car in cars], 'ro')


# animation function.  This is called sequentially
def animate(i):
    if (i+1) % 20 == 0:
        cars.append(Car(i+1))
    if cars[0].x >= 10000:
        cars.pop(0)

    speeds = [car.speed for car in cars]
    slowest = min(speeds)
    fastest = max(speeds)
    mean_speed = sum(speeds) / len(speeds)
    os.system("clear")

    for idx, car in enumerate(cars):
        data = "%d %lf %lf" % (car.idx, car.speed, math.inf if idx == 0 else cars[idx-1].x - car.x)
        create_content_instance("APP", "DATA", data)
        command = get_data("COMMAND", str(car.idx))[0]
        print(car.idx, car.speed, command, mean_speed, fastest, slowest, sep=",")
        if command == "FAST":
            car.faster()
        if command == "SLOW":
            car.slower()
        car.move()

    tunnel.set_data([car.x for car in cars],
                    [car.y for car in cars])

    return tunnel,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, interval=20)

plt.show()
