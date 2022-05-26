from Servizio.CertificatoMedico import CertificatoMedico


class CertificatoAgonistico(CertificatoMedico):

    def __init__(self):
        super().__init__(self)
        self.prezzo=50.00

    def compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio):
        super().compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio)

    def stampaCertificato(self):
        super().stampaCertificato(self)