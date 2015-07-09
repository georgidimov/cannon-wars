from PyQt4 import QtCore
from PyQt4 import QtGui


class FieldUI:
    def __init__(self, field, texture_location):
        self.field = field
        self.texture_location = texture_location

    def __to_qpoints(self, points):
        converted_points = []

        for point in self.field.get_coordinates():
            converted_point = QtCore.QPointF()
            converted_point.setX(point.get_horizontal_position())
            converted_point.setY(point.get_vertical_position())

            converted_points.append(converted_point)

        return converted_points

    def draw(self, painter):
        field_coordinates = self.__to_qpoints(self.field.get_coordinates())
        field_polygon = QtGui.QPolygonF(field_coordinates)

        field_path = QtGui.QPainterPath()
        field_path.addPolygon(field_polygon)

        painter.drawPath(field_path)

        field_texture = QtGui.QPixmap(self.texture_location)
        field_brush = QtGui.QBrush(field_texture)
        painter.fillPath(field_path, field_brush)
