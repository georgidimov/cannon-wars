from PyQt4 import QtGui
from src.field import Field
from src.fieldUI import FieldUI
from src.cannon import Cannon
from src.cannonUI import CannonUI
from src.position import Position


class Game(QtGui.QWidget):
    def __init__(self):
        super(Game, self).__init__()

        self.windowW = 1000
        self.windowH = 768
        self.window_title = 'Cannon wars'
        self.logo_location = 'images/logo.png'

        self.__init_window()

        self.maps = [{}]
        self.current_map = 0
        self.__init_maps()

        bg_palette = QtGui.QPalette()
        bg_image = QtGui.QPixmap(self.maps[self.current_map]['background'])
        bg_brush = QtGui.QBrush(bg_image)
        bg_palette.setBrush(QtGui.QPalette.Background, bg_brush)
        self.setPalette(bg_palette)

        self.field = Field(self.maps[self.current_map]['location'])
        field_texture = self.maps[self.current_map]['grass']
        self.fieldUI = FieldUI(self.field, field_texture)

        self.cannons = []
        self.cannonsUI = []
        self.__init_cannons()

    def __init_window(self):
        self.resize(self.windowW, self.windowH)
        self.setWindowTitle(self.window_title)
        self.setWindowIcon(QtGui.QIcon(self.logo_location))
        self.show()

    def __init_maps(self):
        self.maps[0] = {
            'location': 'maps/map1',
            'grass': 'images/grass1.jpg',
            'background': 'images/background_0.png',
            'cannon0': 'images/cannon0_0.png',
            'cannon1': 'images/cannon0_1.png'
        }

        self.current_map = 0

    def __init_cannons(self):
        self.cannons.append(Cannon(Position(0, 400), 45, 30))
        self.cannons.append(Cannon(Position(600, 395), 45, 30))

        cannon_image = self.maps[self.current_map]['cannon0']
        self.cannonsUI.append(CannonUI(self.cannons[0], cannon_image))

        cannon_image = self.maps[self.current_map]['cannon1']
        self.cannonsUI.append(CannonUI(self.cannons[1], cannon_image))

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)

        self.fieldUI.draw(painter)

        for cannon in self.cannonsUI:
            cannon.draw(painter)

        painter.end()
