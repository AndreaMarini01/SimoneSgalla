from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.MenuClienteGUI import MenuClienteGUI


class loginGUI(QDialog):

    def __init__(self):
        super(loginGUI,self).__init__()
        loadUi("login.ui",self)
        self.lineEdit.text()
        self.lineEdit_2.text()
        self.show()
        self.buttonBox.clicked.connect(self.loginfunction)
        #self.show()

    def loginfunction(self):
        MenuClienteGUI()
        return self.lineEdit, self.lineEdit_2







