from PyQt4 import QtGui, QtCore


class CannonUI:
    def draw(self, painter, texture, x, y, width, height, angle):
        cannon_rectangle = QtCore.QRect()
        cannon_rectangle.setWidth(width)
        cannon_rectangle.setHeight(height)

        center = QtCore.QPoint()
        center.setX(x + width / 2)
        center.setY(y - height)

        painter.save()
        painter.translate(center)
        painter.rotate(angle)

        cannon_image = QtGui.QImage(texture)

        painter.drawImage(cannon_rectangle, cannon_image)
        painter.restore()
