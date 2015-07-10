from PyQt4 import QtGui


class FieldUI:
    def draw(self, painter, texture, coordinates):
        field_polygon = QtGui.QPolygonF(coordinates)

        field_path = QtGui.QPainterPath()
        field_path.addPolygon(field_polygon)

        painter.drawPath(field_path)

        field_texture = QtGui.QPixmap(texture)
        field_brush = QtGui.QBrush(field_texture)
        painter.fillPath(field_path, field_brush)
