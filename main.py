import sys

from PyQt5.QtWidgets import QApplication

from GUI.MenuClienteGUI import MenuClienteGUI
from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI
from GUI.loginGUI import loginGUI

app=QApplication(sys.argv)
#widget=QWidgets
form = loginGUI()
#pag2 = NuovaPrenotazioneGUI(["datetime.datetime.now(),datetime.datetime.now()]", 'ue'])
#prova=MenuClienteGUI()

sys.exit(app.exec_())