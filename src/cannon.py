from src.projectile import Projectile


class Cannon:
    def __init__(self, position, angle, initial_speed):
        self.position = position
        self.height = 92
        self.width = 150

        self.angle = angle
        self.initial_speed = initial_speed

    def get_projectile_trajectory(self):
        projectile = Projectile(self.position, self.angle, self.initial_speed)
        return projectile.get_coordinates()

    def set_horizontal_position(self, x):
        self.position.set_horizontal_position(x)

    def get_horizontal_position(self):
        return self.position.get_horizontal_position()

    def set_vertical_position(self, y):
        self.position.set_vertical_position(y)

    def get_vertical_position(self):
        return self.position.get_vertical_position()

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def set_angle(self, new_angle):
        self.angle = new_angle

    def get_angle(self):
        return self.angle

    def set_initial_speed(self, new_speed):
        self.initial_speed = new_speed

    def get_initial_speed(self):
        return self.initial_speed
