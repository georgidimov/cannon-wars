from PyQt4 import QtGui, QtCore


class CannonUI:
    def __init__(self, cannon, image_location):
        self.cannon = cannon
        self.image_location = image_location

    def draw(self, painter):
        cannon_rectangle = QtCore.QRect()
        cannon_rectangle.setWidth(self.cannon.get_width())
        cannon_rectangle.setHeight(self.cannon.get_height())

        bottom_left_point = QtCore.QPoint()
        bottom_left_point.setX(self.cannon.get_horizontal_position())
        bottom_left_point.setY(self.cannon.get_vertical_position())
        cannon_rectangle.moveBottomLeft(bottom_left_point)

        cannon_image = QtGui.QImage(self.image_location)
        painter.drawImage(cannon_rectangle, cannon_image)
