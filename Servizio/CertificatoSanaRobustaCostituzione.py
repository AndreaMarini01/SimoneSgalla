from Servizio.CertificatoMedico import CertificatoMedico


class CertificatoSanaRobustaCostituzione(CertificatoMedico):

    def __init__(self):
        super().__init__(self)
        self.prezzo=100.00

    def compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio):
        super().compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio)

    def stampaCertificato(self):
        super().stampaCertificato(self)