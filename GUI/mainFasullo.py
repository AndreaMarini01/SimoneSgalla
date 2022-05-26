import datetime
import sys

import datetime as datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import datetime

#from loginGUI import login
from GUI import MenuClienteGUI
from GUI.NuovaPrenotazioneGUI import PrenotazioneGUI
from GUI.loginGUI import login

app=QApplication(sys.argv)
lista2 = []
lista = ([datetime.datetime.now(), datetime.datetime.now()])
for giorno in lista:
    lista2.append(giorno.strftime("%m/%d/%Y, %H:%M"))
widget = QtWidgets.QStackedWidget()
mainwindow = PrenotazioneGUI
widget.addWidget(mainwindow)
widget.show()
print('a')
sys.exit(app.exec_())


