from PyQt4 import QtGui, QtCore
from src.game import Game
from src.fieldUI import FieldUI
from src.cannonUI import CannonUI


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

    def __init_window(self):
        self.resize(self.game.get_window_width(), self.game.get_window_height())
        self.setWindowTitle(self.game.get_title())
        self.setWindowIcon(QtGui.QIcon(self.game.get_logo()))
        self.show()

    def __init_cannons(self):
        for i in range(self.game.get_cannons_count()):
            self.cannons.append(CannonUI())

    def __convert_to_qpoints(self, coordinates):
        converted_points = []

        for point in coordinates:
            converted_point = QtCore.QPointF()
            converted_point.setX(point.get_horizontal_position())
            converted_point.setY(point.get_vertical_position())

            converted_points.append(converted_point)

        return converted_points

    def convert_angle(self, angle):
        difference_in_image = 25
        return angle - difference_in_image

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)

        field_texture = self.game.get_field_texture()
        field_coordinates = self.game.get_field_coordinates()
        field_coordinates = self.__convert_to_qpoints(field_coordinates)
        self.field.draw(painter, field_texture, field_coordinates)

        for cannon in enumerate(self.cannons):
            cannon_index = cannon[0]
            image = self.game.get_cannon_texture(cannon_index)
            x = self.game.get_cannon_horizontal_position(cannon_index)
            y = self.game.get_cannon_vertical_position(cannon_index)
            width = self.game.get_cannon_width(cannon_index)
            height = self.game.get_cannon_height(cannon_index)
            angle = self.game.get_cannon_angle(cannon_index)
            angle = self.convert_angle(angle)
            cannon[1].draw(painter, image, x, y, width, height, angle)
        painter.end()

        print(event)
    '''
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.cannonsUI[0].draw

    '''
