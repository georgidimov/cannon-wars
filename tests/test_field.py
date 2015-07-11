import unittest
from src.field import Field


class TestField(unittest.TestCase):
    def setUp(self):
        self.field = Field('maps/map1')
        self.true_coordinates = [(0, 768), (0, 400), (300, 400), (500, 150),
                                 (600, 380), (1000, 420), (1000, 768)]

    def test_field_coordinates_as_tuples(self):
        field_coordinates = self.field.get_coordinates_as_tuples()

        self.assertEqual(self.true_coordinates, field_coordinates)

    def test_field_coordinates(self):
        field_coordinates = self.field.get_coordinates()

        field_coordinates_as_tuples = []
        for coordinate in field_coordinates:
            x = coordinate.get_horizontal_position()
            y = coordinate.get_vertical_position()
            field_coordinates_as_tuples.append((x, y))

        self.assertEqual(field_coordinates_as_tuples, self.true_coordinates)

if __name__ == '__main__':
    unittest.main()
