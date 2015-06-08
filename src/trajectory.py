import math


class Trajectory:
    def __init__(self, position, angle, initial_speed):
        self.position = position
        self.angle = self.__to_radians(angle)
        self.initial_speed = initial_speed
        self.h = 0.1  # 0.1
        self.G = 9.81

    def __to_radians(self, angle):
        return math.pi / 180. * angle

    def get_next_position(self):
        position = self.position
        velocity = [self.initial_speed * math.cos(self.angle),
                    self.initial_speed * math.sin(self.angle)]

        while True:
            position[0] = position[0] + self.h * velocity[0]
            position[1] = position[1] + self.h * velocity[1]

            velocity[0] = velocity[0] + self.h * 0
            velocity[1] = velocity[1] + self.h * self.G * -1

            yield position
