from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class EliminaPrenotazioneGUI(QDialog):

    def __init__(self, listaPrenotazioniCliente):
        super(EliminaPrenotazioneGUI,self).__init__()
        loadUi("EliminaPrenotazione.ui", self)
        self.comboBox.addItems(listaPrenotazioniCliente)
        self.stampa()

    def stampa(self):
        self.pushButton.clicked.connect(self.prova())
        self.show()

    def prova(self):
        print('ahahahha')
