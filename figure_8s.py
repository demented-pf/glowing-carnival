from easygopigo3 import EasyGoPiGo3

gpg = EasyGoPiGo3()

radius = 30

gpg.orbit(-270, radius)
gpg.drive_cm(radius * 2)
gpg.orbit(270, radius)
gpg.drive_cm(radius * 2)
