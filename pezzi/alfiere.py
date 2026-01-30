from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = False

class Alfiere(Pezzo):
    def __init__(self,colore):
        super().__init__(colore)
        self.nome = "Bishop"
        

    def sposta(self,scacchiera,csrc,cdest):
        super().sposta(scacchiera,csrc,cdest)  

    

    # Le possibili destinazioni dell' alfiere:
    # - 1) si muove a  "x"  [destinazioni si blocca se incontra un pezzo nemico / amico e sono casi diversi]
    # @return tutte le destinazioni possibili (i,j)
    def destinations(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Bishop":
            raise TypeError("[Internal error] Non è presente un'alfiere nella casella!")
        dest = []

        dest += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_sx",destinazioni=True)
        dest += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_dx",destinazioni=True)
        dest += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_sx",destinazioni=True)
        dest += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_dx",destinazioni=True)
        
        if DEBUG:
            DEBUG_print_caselle(dest,"possibili destinazioni dell'alfiere: ")
        
        return dest
    
    def case_controllate(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Bishop":
            raise TypeError("[Internal error] Non è presente un'alfiere nella casella!")
        pos_controllate = []

        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_sx",case_controllate=True)
        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"avanti_dx",case_controllate=True)
        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_sx",case_controllate=True)
        pos_controllate += movimento_diagonale(scacchiera,csrc,giocatore,"indietro_dx",case_controllate=True)


        if DEBUG:
            DEBUG_print_caselle(pos_controllate,"case controllate dall'alfiere:")

        return pos_controllate
    
    def my_name(self):
        return self.nome
    
    def print_my_name(self):
        c = self.colore[0]
        return "B"+c

    #se ha la variabile "mai_mosso"
    def has_mai_mosso(self):
        return False