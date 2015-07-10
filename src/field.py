from src.position import Position


class Field:
    def __init__(self, file_path):
        self.coordinates = []
        with open(file_path) as input_file:
            for line in input_file:
                position = Position()
                position.deserialize(line)
                self.coordinates.append(position)

    def get_coordinates_as_tuples(self):
        converted_coordinates = []

        for coordinate in self.coordinates:
            x = coordinate.get_horizontal_position()
            y = coordinate.get_vertical_position()
            converted_coordinates.append((x, y))

        return converted_coordinates

    def get_coordinates(self):
        return self.coordinates
