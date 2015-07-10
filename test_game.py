import unittest
from src.game import Game


class TestGameGetters(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_window_width(self):
        self.assertEqual(self.game.get_window_width(), 1000)

    def test_window_height(self):
        self.assertEqual(self.game.get_window_height(), 768)

    def test_get_title(self):
        self.assertEqual(self.game.get_title(), 'Cannon wars')

    def test_get_logo(self):
        self.assertEqual(self.game.get_logo(), 'images/logo.png')

    def test_get_background_image(self):
        image_path = 'images/background_0.png'
        self.assertEqual(self.game.get_background_image(), image_path)

    def test_get_field_texture(self):
        image_path = 'images/grass1.jpg'
        self.assertEqual(self.game.get_field_texture(), image_path)

    def test_get_field_coordinates(self):
        field_coordinates = self.game.get_field_coordinates()
        true_coordinates = [(0, 768), (0, 400), (300, 400), (500, 150),
                            (600, 380), (1000, 420), (1000, 768)]

        field_coordinates_as_tuples = []
        for coordinate in field_coordinates:
            x = coordinate.get_horizontal_position()
            y = coordinate.get_vertical_position()
            field_coordinates_as_tuples.append((x, y))

        self.assertEqual(field_coordinates_as_tuples, true_coordinates)

    def test_get_cannons_count(self):
        self.assertEqual(self.game.get_cannons_count(), 2)

    def test_get_cannons_turn(self):
        self.assertEqual(self.game.get_cannon_turn(), 0)

    def test_get_cannon_texture(self):
        index = 0
        image_path = 'images/cannon0_' + str(index) + '.png'
        self.assertEqual(self.game.get_cannon_texture(index), image_path)

    def test_get_cannon_width(self):
        self.assertEqual(self.game.get_cannon_width(0), 150)

    def test_get_cannon_height(self):
        self.assertEqual(self.game.get_cannon_height(0), 92)

    def test_get_cannon_x(self):
        self.assertEqual(self.game.get_cannon_horizontal_position(0), 0)

    def test_get_cannon_y(self):
        self.assertEqual(self.game.get_cannon_vertical_position(1), 395)

    def test_get_cannon_angle(self):
        self.assertEqual(self.game.get_cannon_angle(1), 65)

    def test_get_projectile_image(self):
        image_path = 'images/projectile0.png'
        self.assertEqual(self.game.get_projectile_image(0), image_path)

    def test_projectile_trajectory(self):
        coordinates = self.game.get_projectile_trajectory()
        first_coordinate = [210., 330.]
        medium_coordinate = [548.09460939, 569.45122963]
        last_coordinate = [886.18921879, -172.09754074]

        self.assertAlmostEqual(list(coordinates[0]), first_coordinate, places=3)
        self.assertAlmostEqual(coordinates[int(len(coordinates) / 2)][0],
                               medium_coordinate[0], places=3)
        self.assertAlmostEqual(coordinates[int(len(coordinates) / 2)][1],
                               medium_coordinate[1], places=3)
        self.assertAlmostEqual(coordinates[-1][0], last_coordinate[0], places=3)
        self.assertAlmostEqual(coordinates[-1][1], last_coordinate[1], places=3)


class TestGameSetters(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_increasing_cannon_angle(self):
        index = self.game.get_cannon_turn()
        angle = self.game.get_cannon_angle(index)
        self.game.increase_cannon_angle()

        self.assertEqual(self.game.get_cannon_angle(index), angle - 1)

    def test_decreasing_cannon_angle(self):
        index = self.game.get_cannon_turn()
        angle = self.game.get_cannon_angle(index)
        self.game.increase_cannon_angle()

        self.assertEqual(self.game.get_cannon_angle(index), angle - 1)

    def test_increasing_cannon_initial_speed(self):
        index = self.game.get_cannon_turn()
        speed = self.game.get_cannon_initial_speed(index)
        self.game.increase_cannon_initial_speed()

        self.assertEqual(self.game.get_cannon_initial_speed(index), speed + 1)

    def test_decreasing_cannon_initial_speed(self):
        index = self.game.get_cannon_turn()
        speed = self.game.get_cannon_initial_speed(index)
        self.game.decrease_cannon_initial_speed()

        self.assertEqual(self.game.get_cannon_initial_speed(index), speed - 1)


class TestGameLogic(unittest.TestCase):
    def test_shoot_and_game_over(self):
        game = Game()
        game.shoot()
        self.assertTrue(game.is_game_over())

    def test_winner(self):
        game = Game()
        game.shoot()
        self.assertEqual(game.winner(), 1)

if __name__ == '__main__':
    unittest.main()
