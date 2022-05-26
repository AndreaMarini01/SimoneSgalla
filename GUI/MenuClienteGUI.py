from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.EliminaPrenotazioneGUI import EliminaPrenotazioneGUI
from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI



class MenuClienteGUI(QDialog):

    def __init__(self):
        super(MenuClienteGUI, self).__init__()
        loadUi("MenuCliente.ui", self)
        self.menu()


    def menu (self):
        self.pushButton.clicked.connect(self.NuovaPrenotazione)
        self.pushButton_2.clicked.connect(self.EliminaPrenotazione)
        self.show()


    def NuovaPrenotazione(self):
        NuovaPrenotazioneGUI(['a','b'])

    def EliminaPrenotazione (self):
        EliminaPrenotazioneGUI(['a','b'])





