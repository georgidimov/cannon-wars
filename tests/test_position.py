import unittest
from src.position import Position


class TestPosition(unittest.TestCase):
    def test_getters(self):
        position = Position(1, 2)
        x = position.get_horizontal_position()
        y = position.get_vertical_position()

        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def test_setters(self):
        position = Position()
        position.set_horizontal_position(21)
        position.set_vertical_position(42)

        x = position.get_horizontal_position()
        y = position.get_vertical_position()

        self.assertEqual(x, 21)
        self.assertEqual(y, 42)

    def test_defualt_values(self):
        position = Position()
        x = position.get_horizontal_position()
        y = position.get_vertical_position()

        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_to_tuple(self):
        position = Position(23, 47)
        self.assertEqual(position.to_tuple(), (23, 47))

    def test_serialization(self):
        position = Position(5, 25)
        self.assertEqual(position.serialize(), '(5, 25)')

    def test_deserialization(self):
        serialized = '(5, 25)'

        position = Position(2, 22)
        position.deserialize(serialized)

        x = position.get_horizontal_position()
        y = position.get_vertical_position()

        self.assertEqual(x, 5)
        self.assertEqual(y, 25)

    def test_updating_values(self):
        position = Position(2, 22)
        position.set_horizontal_position(0)
        position.set_vertical_position(1)
        position.deserialize('(7, 8)')

        x = position.get_horizontal_position()
        y = position.get_vertical_position()

        self.assertEqual(x, 7)
        self.assertEqual(y, 8)


if __name__ == '__main__':
    unittest.main()
