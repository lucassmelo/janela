from PySide import QtGui
import sys

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(250, 150)
wid.setWindowTitle('Janela')
wid.show()

sys.exit(app.exec_())
