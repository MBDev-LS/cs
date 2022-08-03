import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication(sys.argv)
d1 = QDialog()
d1.show()
d2 = QDialog()
d2.show()
sys.exit(app.exec_())