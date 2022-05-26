import os
import pickle


from Servizio.Documento import Documento


class Ricetta(Documento):

    def __init__(self):
        super().__init__(self)
        self.farmacoPrescritto=''

    def compilaRicetta(self,farmacoPrescritto,nomePaziente,nomeCognomeDottore,dataRilascio):
        self.CompilaDocumento(self=self,nomePaziente=nomePaziente, nomeCognomeDottore=nomeCognomeDottore, dataRilascio=dataRilascio)
        self.farmacoPrescritto=farmacoPrescritto

    def stampaRicetta(self):
        ricetta=self.StampaDocumento(self)
        ricetta['farmaco prescritto']=self.farmacoPrescritto
       # if os.path.isfile('dati/Ricetta.pickle'):
        with open ('dati/Ricetta.pickle', 'wb+') as f:
                pickle.dump(ricetta,f,pickle.HIGHEST_PROTOCOL)
      #  else:
        #    with open ("dati/Ricetta.pickle", 'xb') as f:
         #    pickle.dump(ricetta,f,pickle.HIGHEST_PROTOCOL)

    def prova(self):
        if os.path.isfile('dati/Ricetta.pickle'):
            with open('dati/Ricetta.pickle', 'rb') as f:
               a=pickle.load(f)
               for x in a:
                 print(x+": "+str (a[x]))


