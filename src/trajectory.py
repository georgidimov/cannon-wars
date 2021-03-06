import numpy
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

    def get_coordinates(self):
        num_steps = 200
        position = numpy.zeros([num_steps + 1, 2])
        velocity = numpy.zeros([num_steps + 1, 2])

        position[0] = 0

        velocity[0] = [self.initial_speed * math.cos(self.angle),
                       self.initial_speed * math.sin(self.angle)]
        acceleration = numpy.array([0.0, -self.G])

        for step in range(num_steps):
            position[step + 1] = position[step] + self.h * velocity[step]
            velocity[step + 1] = velocity[step] + self.h * acceleration

        for point in position:
            point[0] += self.position.get_horizontal_position()
            point[1] += self.position.get_vertical_position()
        return position
