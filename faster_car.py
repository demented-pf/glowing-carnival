from time import sleep

from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()

curent_speed = 50

end_speed = 400

step = (end_speed - curent_speed) / 20

gpg.forward()
while curent_speed <= end_speed:
    sleep(0.5)
    gpg.set_speed(curent_speed)
    curent_speed += step
gpg.open_eyes()

sleep(.1)
gpg.close_eyes()

gpg.forward()

while curent_speed > 0:
    sleep(0.5)
    gpg.set_speed(curent_speed)
    curent_speed -= step

gpg.stop()
