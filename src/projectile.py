from src.trajectory import Trajectory


class Projectile:
    def __init__(self, position, angle, initial_speed):
        self.coordinates = Trajectory(position, angle, initial_speed)

    def get_coordinates(self):
        return self.coordinates.get_coordinates()
