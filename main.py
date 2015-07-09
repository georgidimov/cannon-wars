import sys
from PyQt4 import QtGui
from src.game import Game

app = QtGui.QApplication([])
game = Game()

sys.exit(app.exec_())
