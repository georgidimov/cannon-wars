from PyQt4 import QtCore


class ProjectileUI:
    def __init__(self):
        self.in_cannon = True

    def shoot(self):
        self.in_cannon = False

    def draw(self, painter, image, trajectory):
        if not self.in_cannon:
            painter.setPen(QtCore.Qt.red)
            for point in trajectory:
                painter.drawPoint(point[0], point[1])
            self.in_cannon = False
