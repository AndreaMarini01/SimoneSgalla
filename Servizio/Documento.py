import datetime

class Documento:
    def __init__(self):
        self.dataRilascio
        self.nomeCognomeDottore=''
        self.nomePaziente=''

    def CompilaDocumento(self,nomePaziente,nomeCognomeDottore,dataRilascio):
        self.dataRilascio=dataRilascio
        self.nomeCognomeDottore=nomeCognomeDottore
        self.nomePaziente=nomePaziente

    def StampaDocumento(self):
        return {
            'data': self.dataRilascio,
            'rilasciato a': self.nomePaziente,
            'dal dottor':self.nomeCognomeDottore
        }