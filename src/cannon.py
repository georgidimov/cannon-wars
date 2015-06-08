from src.projectile import Projectile


class Cannon:
    def __init__(self, position, angle, initial_speed):
        self.position = position
        self.angle = angle
        self.initial_speed = initial_speed

    def fire(self):
        projectile = Projectile(self.position, self.angle, self.initial_speed)
        return projectile.get_coordinates()
