import time

from easygopigo3 import EasyGoPiGo3

g = EasyGoPiGo3()
t = time
# # go forward
# g.forward()
# t.sleep(1)
# g.stop()
#
# t.sleep(1)
#
#
# g.drive_cm(50,True)
# t.sleep(1)
#
# g.right()
# t.sleep(1)

#
# g.left()
# t.sleep(1)
# g.stop()

radius = 30
g.set_speed(100)

g.orbit(-270, radius)
g.drive_cm(radius * 2)
g.orbit(270, radius)
g.drive_cm(radius * 2)
