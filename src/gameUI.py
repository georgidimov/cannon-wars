from PyQt4 import QtGui, QtCore
from src.game import Game
from src.fieldUI import FieldUI
from src.cannonUI import CannonUI
from src.projectileUI import ProjectileUI


class GameUI(QtGui.QWidget):
    def __init__(self):
        super(GameUI, self).__init__()
        self.game = Game()

        self.__init_window()

        background_palette = QtGui.QPalette()
        background_image = QtGui.QPixmap(self.game.get_background_image())
        background_brush = QtGui.QBrush(background_image)
        background_palette.setBrush(QtGui.QPalette.Background, background_brush)
        self.setPalette(background_palette)

        self.field = FieldUI()

        self.cannons = []
        self.__init_cannons()

        self.projectiles = []
        self.__init_projectiles()

    def __init_window(self):
        self.resize(self.game.get_window_width(), self.game.get_window_height())
        self.setWindowTitle(self.game.get_title())
        self.setWindowIcon(QtGui.QIcon(self.game.get_logo()))
        self.show()

    def __init_cannons(self):
        for i in range(self.game.get_cannons_count()):
            self.cannons.append(CannonUI())

    def __init_projectiles(self):
        for i in range(self.game.get_cannons_count()):
            self.projectiles.append(ProjectileUI())

    def __convert_to_qpoints(self, coordinates):
        converted_points = []

        for point in coordinates:
            converted_point = QtCore.QPointF()
            converted_point.setX(point.get_horizontal_position())
            converted_point.setY(point.get_vertical_position())

            converted_points.append(converted_point)

        return converted_points

    def __convert_trajectory(self, trajectory):
        for point in trajectory:
            point[1] = self.game.get_window_height() - point[1]

        return trajectory

    def __convert_angle(self, angle):
        difference_in_image = 25
        return angle - difference_in_image

    def __draw_field(self, painter):
        field_texture = self.game.get_field_texture()
        field_coordinates = self.game.get_field_coordinates()
        field_coordinates = self.__convert_to_qpoints(field_coordinates)
        self.field.draw(painter, field_texture, field_coordinates)

    def __draw_cannons(self, painter):
        for cannon in enumerate(self.cannons):
            index = cannon[0]
            cannon_image = self.game.get_cannon_texture(index)
            x = self.game.get_cannon_horizontal_position(index)
            y = self.game.get_cannon_vertical_position(index)
            width = self.game.get_cannon_width(index)
            height = self.game.get_cannon_height(index)
            angle = self.game.get_cannon_angle(index)
            angle = self.__convert_angle(angle)
            cannon[1].draw(painter, cannon_image, x, y, width, height, angle)

            projectile_image = self.game.get_projectile_image(index)
            trajectory = self.game.get_projectile_trajectory(index)
            trajectory = self.__convert_trajectory(trajectory)
            self.projectiles[index].draw(painter, projectile_image, trajectory)

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)

        self.__draw_field(painter)
        self.__draw_cannons(painter)

        painter.end()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.projectiles[0].shoot()
        self.update()
