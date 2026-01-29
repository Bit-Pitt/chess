from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = True

class Regina(Pezzo):
    def __init__(self,colore):
        super().__init__(colore)
        self.nome = "Queen"
        

    def sposta(self,scacchiera,csrc,cdest):
        super().sposta(scacchiera,csrc,cdest)  

    

    # Le possibili destinazioni della regina:
    # - mette insieme quelle del re, torre, alfiere
    # @return tutte le destinazioni possibili (i,j)
    def destinations(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Queen":
            raise TypeError("[Internal error] Non è presente una regina nella casella!")
        dest = []

        # dest += 

        if DEBUG:
            DEBUG_print_caselle(dest,"possibili destinazioni della regina : ")
        
        return dest
    
    def case_controllate(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Queen":
            raise TypeError("[Internal error] Non è presente una regina nella casella!")
        pos_controllate = []

        # dest +=  


        if DEBUG:
            DEBUG_print_caselle(pos_controllate,"case controllate dalla regina:")
        return pos_controllate
    
    def my_name(self):
        return self.nome
    
    def print_my_name(self):
        c = self.colore[0]
        return "Q"+c

    #se ha la variabile "mai_mosso"
    def has_mai_mosso(self):
        return False