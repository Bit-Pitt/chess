from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = True

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

        # Crea una UNICA fun: "movimento_diagonale" a cui passi per parametro direzione es "avanti_sx" e se destinazioni,case_controllate
        # dest += movimento_diagonale(direzione)

        if DEBUG:
            DEBUG_print_caselle(dest,"possibili destinazioni dell'alfiere: ")
        
        return dest
    
    def case_controllate(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Bishop":
            raise TypeError("[Internal error] Non è presente un'alfiere nella casella!")
        pos_controllate = []

        # dest += movimento_diagonale ... 


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