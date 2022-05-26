import datetime

from PyQt5.uic.properties import QtWidgets

from GUI.NuovaPrenotazioneGUI import PrenotazioneGUI

from Servizio import Prenotazione


class Cliente:
    def __init__(self):
        self.nomeCognome = ""
        self.nomeDottore = ""
        self.password = ""
        self.email = ""
        self.numeroDiTelefono = ""
        self.codiceFiscale = ""
        self.id = -1
        self.messaggio = ""
        self.prenotazione

    def inserisciNomeCognome (self, nome, cognome):
           if nome.isalpha() and cognome.isalpha():
                self.nomeCognome = nome +" "+cognome
                return True
           else :
                return False

    def inserisciEmail (self, email):
        if "@" in email:
            stringa1, stringa2 = email.split("@")
            if "." in stringa2:
                self.email = email
                return True
        return False

    def inserisciNumeroDiTelefono (self, numeroDiTelefono):
        if numeroDiTelefono.isdecimal():
            self.numeroDiTelefono = numeroDiTelefono
            return True
        else:
            return False

    def inserisciCodiceFiscale (self, codiceFiscale):
        c=0
        y=0
        for x in codiceFiscale:
            if x.isalpha:
                c+=1
            if x.isdecimal:
                y+=1
        if c==9 and y==7:
            self.codiceFiscale = codiceFiscale
            return True
        else :
            return False

    def inserisciPassword (self, password):
        self.password = password

    def selezionaMedico (self, nomeDottore):
        self.nomeDottore = nomeDottore

    def setId (self, id):
        self.id=id

    def getId (self):
        return self.id

    def getEmail (self):
        return self.email

    def getNomeCognome (self):
        return self.nomeCognome

    def getNumeroDiTelefono (self):
        return self.numeroDiTelefono

    def registrazione (self):
        pass

    def richiediPrenotazione(self, listaPrenotazioni, listaDottori):
        self.prenotazione = Prenotazione
        delta = datetime.time(minute=15)
        for dottore in listaDottori:
            if dottore.nomeCognome == self.nomeDottore:
                lista = dottore.orarioLavoro
        for contatore in range(0, 24):
            contatore += 1
            lista.append(lista.index(contatore) + delta)
            listaPrenotate = 0
        for prenotazione in listaPrenotazioni:
            listaPrenotate.append(prenotazione.dataOra)
        listaFinale = lista - listaPrenotate
        x=PrenotazioneGUI(listaFinale,prenotazione)
        pass



    def selezionaDataOra(self,listaPrenotazioni, listaDottori):
        delta=datetime.time(minute=15)
        lista2 = []
        for dottore in listaDottori:
            if dottore.nomeCognome==self.nomeDottore:
                lista =dottore.orarioLavoro
        for contatore in range (0,24) :
            contatore += 1
            lista.append(lista.index(contatore)+delta)
            listaPrenotate=0
        for prenotazione in listaPrenotazioni:
            listaPrenotate.append(prenotazione.dataOra)
        listaFinale = lista-listaPrenotate

        # self.prenotazione.orario=Grafica.show(listaFinale)
