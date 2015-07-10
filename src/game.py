from src.field import Field
from src.cannon import Cannon
from src.position import Position


class Game:
    def __init__(self):
        super(Game, self).__init__()

        self.window_width = 1000
        self.window_height = 768
        self.title = 'Cannon wars'
        self.logo_location = 'images/logo.png'

        self.maps = [{}]
        self.current_map = 0
        self.cannon_turn = 0

        self.__init_maps()
        self.field = Field(self.maps[self.current_map]['field_source_file'])

        self.cannon_angle_step = 1
        self.cannon_initial_speed_step = 1
        self.cannons_count = 2
        self.cannons = []
        self.__init_cannons()

    def __init_maps(self):
        self.maps[0] = {
            'field_source_file': 'maps/map1',
            'field_texture': 'images/grass1.jpg',
            'background': 'images/background_0.png',
            'cannon0': 'images/cannon0_0.png',
            'cannon1': 'images/cannon0_1.png',
            'projectile0': 'images/projectile0.png',
            'projectile1': 'images/projectile0.png'
        }

        self.current_map = 0

    def __init_cannons(self):
        cannon = Cannon(Position(0, 400), 65, 80, Position(210, 330))
        self.cannons.append(cannon)

        cannon = Cannon(Position(600, 395), 65, 80, Position(680, 310))
        self.cannons.append(cannon)

    def get_window_height(self):
        return self.window_height

    def get_window_width(self):
        return self.window_width

    def get_title(self):
        return self.title

    def get_logo(self):
        return self.logo_location

    def get_background_image(self):
        return self.maps[self.current_map]['background']

    def get_field_texture(self):
        return self.maps[self.current_map]['field_texture']

    def get_field_coordinates(self):
        return self.field.get_coordinates()

    def get_cannons_count(self):
        return self.cannons_count

    def get_cannon_turn(self):
        return self.cannon_turn

    def get_cannon_texture(self, index):
        return self.maps[self.current_map]['cannon' + str(index)]

    def get_cannon_width(self, index):
        return self.cannons[index].get_width()

    def get_cannon_height(self, index):
        return self.cannons[index].get_height()

    def get_cannon_horizontal_position(self, index):
        return self.cannons[index].get_horizontal_position()

    def get_cannon_vertical_position(self, index):
        return self.cannons[index].get_vertical_position()

    def set_cannon_angle(self, index, angle):
        self.cannons[index].set_angle(angle)

    def increase_cannon_angle(self):
        cannon = self.cannons[self.cannon_turn]
        angle = cannon.get_angle()
        cannon.set_angle(angle + self.cannon_angle_step)

    def decrease_cannon_angle(self):
        cannon = self.cannons[self.cannon_turn]
        angle = cannon.get_angle()
        cannon.set_angle(angle - self.cannon_angle_step)

    def increase_cannon_initial_speed(self):
        cannon = self.cannons[self.cannon_turn]
        speed = cannon.get_initial_speed() + self.cannon_initial_speed_step
        cannon.set_initial_speed(speed)

    def decrease_cannon_initial_speed(self):
        cannon = self.cannons[self.cannon_turn]
        speed = cannon.get_initial_speed() - self.cannon_initial_speed_step
        cannon.set_initial_speed(speed)

    def get_cannon_angle(self, index):
        angle = self.cannons[index].get_angle()

        if index == 0:
            angle = 90 - angle

        return angle

    def get_projectile_trajectory(self):
        return self.cannons[self.cannon_turn].get_projectile_trajectory()

    def get_projectile_image(self, index):
        return self.maps[self.current_map]['projectile' + str(index)]

    def shoot(self):
        self.cannon_turn += 1
        self.cannon_turn %= self.cannons_count
