import pickle

import Documento


class CertificatoMedico(Documento):

    def __init__(self):
        super().__init__(self)
        self.prezzo=0

    def compilaCertificato(self,nomePaziente,nomeCognomeDottore,dataRilascio):
        self.CompilaDocumento(self,nomePaziente,nomeCognomeDottore,dataRilascio)

    def stampaCertificato(self):
        documento=self.StampaDocumento(self)
        documento['importoPagato']=self.prezzo
        #if os.path.isfile('dati/Certificati.pickle'):
        with open ('dati/Certificati.pickle' , 'wb+') as f:
            pickle.dump(documento,f,pickle.HIGHEST_PROTOCOL)
        #else:
            #with open ("dati/Ricetta.pickle",'xb') as f:
                #pickle.dump(ricetta,f,pickle.HIGHEST_PROTOCOL)