from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = False

class Cavallo(Pezzo):
    def __init__(self,colore):
        super().__init__(colore)
        self.nome = "Knight"
        

    def sposta(self,scacchiera,csrc,cdest):
        super().sposta(scacchiera,csrc,cdest)  

    

    # Le possibili destinazioni dell' alfiere:
    # - 1) movimento speciale, 8 caselle al più, basta controllare che le caselle siano valide e vuote
    # @return tutte le destinazioni possibili (i,j)
    def destinations(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Knight":
            raise TypeError("[Internal error] Non è presente un cavallo nella casella!")

        dest = movimento_cavallo(scacchiera,csrc,giocatore,destinazioni=True)

        if DEBUG:
            DEBUG_print_caselle(dest,"possibili destinazioni del cavallo: ")
        
        return dest
    
    def case_controllate(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Knight":
            raise TypeError("[Internal error] Non è presente un cavallo nella casella!")

        pos_controllate = movimento_cavallo(scacchiera,csrc,giocatore,case_controllate=True)

        if DEBUG:
            DEBUG_print_caselle(pos_controllate,"case controllate da cavallo")
        return pos_controllate
    
    def my_name(self):
        return self.nome
    
    def print_my_name(self):
        c = self.colore[0]
        return "C"+c

    #se ha la variabile "mai_mosso"
    def has_mai_mosso(self):
        return False