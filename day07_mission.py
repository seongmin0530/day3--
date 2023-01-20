# 10. 10
class Laser:
    def does(self):
        return 'disintegrate (Laser)'


class Claw:
    def does(self):
        return 'crush (Claw)'


class SmartPhone:
    def does(self):
        return 'ring (SmartPhone)'


class Robot():
    def __init__(self, laser, claw, smartphone):
        self.laser = laser.does()
        self.claw = claw.does()
        self.smartphone = smartphone.does()

    def does(self):
        print(f'Robot can do {self.laser}, {self.claw}, {self.smartphone}.')


a_laser = Laser()
a_claw = Claw()
a_smartphone = SmartPhone()
robot = Robot(a_laser, a_claw, a_smartphone)
robot.does()
