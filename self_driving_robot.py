import sys
import time

import easygopigo3

g = easygopigo3.EasyGoPiGo3()
dist = g.init_distance_sensor()

radius = 30
g.set_speed(300)

g.forward()


def self_driving():
    if 300 > dist.read_mm():
        print("smaller")
        g.turn_degrees(90, False)
        print("after turning")
    elif 300 > dist.read_mm():
        g.turn_degrees(180, False)
    elif 300 > dist.read_mm():
        g.turn_degrees(270, False)
    else:
        print("Moving forward")
        g.open_eyes()
        g.forward()
        time.sleep(2)


while True:
    try:
        print("Distance Sensor Reading (mm): " + str(dist.read_mm()))
        self_driving()
    except KeyboardInterrupt:
        g.stop()
        sys.exit()
