from PyQt4 import QtGui, QtCore
from src.field import Field
from src.fieldUI import FieldUI
from src.cannon import Cannon
from src.position import Position


class Game(QtGui.QWidget):
    def __init__(self):
        super(Game, self).__init__()

        self.windowW = 1000
        self.windowH = 768
        self.__init_window()

        self.maps = [{}]
        self.current_map = 0
        self.__init_maps()

        self.fieldUI = FieldUI(Field(self.maps[self.current_map]['location']),
                               self.maps[self.current_map]['texture'])

        self.cannons = []

    def __init_window(self):
        self.resize(self.windowW, self.windowH)
        self.show()

    def __init_maps(self):
        self.maps[0] = {
            'location': 'maps/map1',
            'texture': 'images/grass1.jpg'
        }

        self.current_map = 0

    def __init_cannons(self):
        self.cannons[0] = Cannon(Position(50, 50), 45, 30)
        self.cannons[1] = Cannon(Position(950, 50), 45, 30)

    def __to_qpoints(self, points):
        converted_points = []

        for point in points:
            converted_point = QtCore.QPointF()
            converted_point.setX(point.get_horizontal_position())
            converted_point.setY(point.get_vertical_position())

            converted_points.append(converted_point)

        return converted_points

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.fieldUI.draw(painter)
        painter.end()
