
import sys
from PyQt4 import QtCore, QtGui

class Simulation(QtGui.QMainWindow):
	def __init__(self, size):
		QtGui.QMainWindow.__init__(self)

		self.setGeometry(size, size, 200, 200)
		self.setWindowTitle('Prometheus simulation')


# Main class
app = QtGui.QApplication(sys.argv)
s = Simulation(400)
s.show()
sys.exit(app.exec_())