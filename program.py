import sys
from PyQt4 import QtGui
from hauptdialog import Ui_HauptDialog as Dlg

class MeinDialog(QtGui.QDialog, Dlg):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    
app = QtGui.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())



