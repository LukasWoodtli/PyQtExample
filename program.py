import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from hauptdialog import Ui_HauptDialog as Dlg

class MeinDialog(QDialog, Dlg):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
    
app = QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())



