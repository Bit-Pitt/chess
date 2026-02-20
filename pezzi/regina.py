from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = False

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

        dest +=  movimento_re(scacchiera,csrc,destinazioni=True)

        dest += movimento_verticale(scacchiera,csrc,giocatore,avanti = True,destinazioni=True)      
        dest += movimento_verticale(scacchiera,csrc,giocatore,avanti = False,destinazioni=True)
        dest += movimento_orizzontale(scacchiera,csrc,giocatore,destra = True,destinazioni=True)
        dest += movimento_orizzontale(scacchiera,csrc,giocatore,destra = False,destinazioni=True) 

        dest += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_sx",destinazioni=True)
        dest += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_dx",destinazioni=True)
        dest += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_sx",destinazioni=True)
        dest += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_dx",destinazioni=True)

        dest = list(set(dest))      #rimuovo posizioni duplicate

        if DEBUG:
            DEBUG_print_caselle(dest,"possibili destinazioni della regina : ")
        
        dest = self.filtro_inchiodatura(scacchiera,csrc,dest)
        return dest
    
    #Analogo
    def case_controllate(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Queen":
            raise TypeError("[Internal error] Non è presente una regina nella casella!")
        pos_controllate = []

        pos_controllate += movimento_re(scacchiera,csrc,case_controllate=True)  

        pos_controllate += movimento_verticale(scacchiera,csrc,giocatore,avanti = True,case_controllate=True)
        pos_controllate += movimento_verticale(scacchiera,csrc,giocatore,avanti = False,case_controllate=True)
        pos_controllate+= movimento_orizzontale(scacchiera,csrc,giocatore,destra = True,case_controllate=True)
        pos_controllate += movimento_orizzontale(scacchiera,csrc,giocatore,destra = False,case_controllate=True)

        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_sx",case_controllate=True)
        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_dx",case_controllate=True)
        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_sx",case_controllate=True)
        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_dx",case_controllate=True)

        pos_controllate = list(set(pos_controllate))      #rimuovo posizioni duplicate

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