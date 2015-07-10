import unittest
from src.trajectory import Trajectory
from src.position import Position


class TestTrajectoryCalculation(unittest.TestCase):
    def setUp(self):
        self.trajectory = Trajectory(Position(20, 21), 45, 60)
        self.coordinates = self.trajectory.get_coordinates()

    def test_starting_positian(self):
        true_position = [20, 21]
        first_position = list(self.coordinates[0])

        self.assertAlmostEqual(first_position[0], true_position[0], places=3)
        self.assertAlmostEqual(first_position[1], true_position[1], places=3)

    def test_medium_position(self):
        true_position = [444.26406871, -40.33093129]
        medium_position = list(self.coordinates[int(len(self.coordinates) / 2)])

        self.assertAlmostEqual(medium_position[0], true_position[0], places=3)
        self.assertAlmostEqual(medium_position[1], true_position[1], places=3)

    def test_last_postion(self):
        true_position = [868.5281374, -1082.66186258]
        last_position = list(self.coordinates[-1])

        self.assertAlmostEqual(last_position[0], true_position[0], places=3)
        self.assertAlmostEqual(last_position[1], true_position[1], places=3)


if __name__ == '__main__':
    unittest.main()
