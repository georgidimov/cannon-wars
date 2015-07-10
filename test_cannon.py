import unittest
from src.cannon import Cannon
from src.position import Position


class TestCannonGetters(unittest.TestCase):
    def setUp(self):
        self.cannon_position = Position(25, 23)
        self.projectile_position = Position(35, 33)
        self.angle = 45
        self.initial_speed = 100
        self.cannon = Cannon(self.cannon_position, self.angle,
                             self.initial_speed, self.projectile_position)

    def test_horizontal_position(self):
        true_x = self.cannon_position.get_horizontal_position()
        cannon_x = self.cannon.get_horizontal_position()

        self.assertEqual(true_x, cannon_x)

    def test_vertical_position(self):
        true_y = self.cannon_position.get_vertical_position()
        cannon_y = self.cannon.get_vertical_position()

        self.assertEqual(true_y, cannon_y)

    def test_width(self):
        self.assertEqual(self.cannon.get_width(), 150)

    def test_height(self):
        self.assertEqual(self.cannon.get_height(), 92)

    def test_angle(self):
        self.assertEqual(self.cannon.get_angle(), self.angle)

    def test_initial_speed(self):
        self.assertEqual(self.cannon.get_initial_speed(), self.initial_speed)


class TestCannonSetters(unittest.TestCase):
    def setUp(self):
        self.cannon = Cannon(Position(0, 0), 42, 59, Position(1, 1))

    def test_horizontal_position(self):
        true_x = 5
        self.cannon.set_horizontal_position(true_x)
        cannon_x = self.cannon.get_horizontal_position()

        self.assertEqual(true_x, cannon_x)

    def test_vertical_position(self):
        true_y = 7
        self.cannon.set_vertical_position(true_y)
        cannon_y = self.cannon.get_vertical_position()

        self.assertEqual(true_y, cannon_y)

    def test_angle(self):
        true_angle = 42
        self.cannon.set_angle(true_angle)
        cannon_angle = self.cannon.get_angle()

        self.assertEqual(cannon_angle, true_angle)

    def test_initial_speed(self):
        true_initial_speed = 145
        self.cannon.set_initial_speed(true_initial_speed)
        cannon_initial_speed = self.cannon.get_initial_speed()

        self.assertEqual(true_initial_speed, cannon_initial_speed)


class TestCannonDestruction(unittest.TestCase):
    def test_default_destruction_state(self):
        cannon = Cannon(Position(0, 0), 42, 59, Position(1, 1))
        self.assertFalse(cannon.is_destroyed())

    def test_destruction(self):
        cannon = Cannon(Position(0, 0), 42, 59, Position(1, 1))
        cannon.destroy()
        self.assertTrue(cannon.is_destroyed())


if __name__ == '__main__':
    unittest.main()
