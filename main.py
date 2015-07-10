import sys
from PyQt4 import QtGui
from src.gameUI import GameUI

app = QtGui.QApplication([])
game = GameUI()

sys.exit(app.exec_())
