class Position:
    def __init__(self):
        self.coordinates = []

    def get_horizontal_position(self):
        return self.coordinates[0]

    def set_horizontal_position(self, value):
        self.coordinates[0] = value

    def get_vertical_position(self):
        return self.coordinates[1]

    def set_vertical_position(self, value):
        self.coordinates[1] = value

    def serialize(self):
        serialized_string = '('
        for coordinate in self.coordinates:
            serialized_string += str(coordinate)

            if coordinate != self.coordinates[-1]:
                serialized_string += ', '

        serialized_string += ')'

        return serialized_string

    def deserialize(self, string):
        string = string.replace('(', '').replace(')', '').replace('\n', '')

        for number in string.split(','):
            self.coordinates.append(int(number))
