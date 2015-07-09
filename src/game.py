from PyQt4 import QtGui, QtCore
from src.field import Field


class Game(QtGui.QWidget):
    def __init__(self):
        super(Game, self).__init__()

        self.windowW = 1000
        self.windowH = 768
        self.initWindow()

        self.maps = [{}]
        self.maps[0] = {
            'location': 'maps/map1',
            'texture': 'images/grass1.jpg'
        }

        self.current_map = 0
        self.field = Field(self.maps[self.current_map]['location'])

    def initWindow(self):
        self.resize(self.windowW, self.windowH)
        self.show()

    def to_qpoints(self, points):
        converted_points = []

        for point in points:
            converted_point = QtCore.QPointF()
            converted_point.setX(point.get_horizontal_position())
            converted_point.setY(point.get_vertical_position())

            converted_points.append(converted_point)

        return converted_points

    def paintEvent(self, e):
        field_coordinates = self.to_qpoints(self.field.get_coordinates())
        field_polygon = QtGui.QPolygonF(field_coordinates)

        field_path = QtGui.QPainterPath()
        field_path.addPolygon(field_polygon)

        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawPath(field_path)

        field_texture = QtGui.QPixmap(self.maps[self.current_map]['texture'])
        field_brush = QtGui.QBrush(field_texture)
        qp.fillPath(field_path, field_brush)
        qp.end()


