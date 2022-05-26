import datetime


class Prenotazione:

    def __init__(self):
        self.certificatoMedico
        self.cliente
        self.dataOra=datetime.datetime
        self.dottore
        self.durataVisita=datetime.time(0,15)
        self.note
        self.ricettaMedica
        self.visitaGenerica

    def setCliente(self,cliente):
        self.cliente=cliente

    def setDottore(self,dottore):
        self.dottore=dottore

    def setDataOra(self,dataOra):
        self.dataOra=dataOra

    def setNote(self,note):
        self.note=note

    def tipoAppuntamento(self):
        pass

    def getDataOra(self):
        return self.dataOra

    def getCliente(self):
        return self.cliente

    def getDottore(self):
        return self.dottore