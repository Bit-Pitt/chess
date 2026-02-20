from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = False

class Torre(Pezzo):
    def __init__(self,colore):
        super().__init__(colore)
        self.nome = "Rook"
        self.mai_mosso = True   #per possibile arrocco

    def sposta(self,scacchiera,csrc,cdest):
        super().sposta(scacchiera,csrc,cdest)  
        self.mai_mosso = False
    

    # Le possibili destinazioni della torre:
    # - 1) si muove a  "+"  [destinazioni si blocca se incontra un pezzo nemico / amico e sono casi diversi]
    # @return tutte le destinazioni possibili (i,j)
    def destinations(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Rook":
            raise TypeError("[Internal error] Non è presente una torre nella casella!")
        dest = []

        dest += movimento_verticale(scacchiera,csrc,giocatore,avanti = True,destinazioni=True)      #avanti sempre rispetto alla prospettiva del white!
        dest += movimento_verticale(scacchiera,csrc,giocatore,avanti = False,destinazioni=True)
        dest += movimento_orizzontale(scacchiera,csrc,giocatore,destra = True,destinazioni=True)
        dest += movimento_orizzontale(scacchiera,csrc,giocatore,destra = False,destinazioni=True)

        if DEBUG:
            DEBUG_print_caselle(dest,"possibili destinazioni da torre")
            
        dest = self.filtro_inchiodatura(scacchiera,csrc,dest)
        return dest
    
    def case_controllate(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Rook":
            raise TypeError("[Internal error] Non è presente una torre nella casella!")
        pos_controllate = []

        pos_controllate += movimento_verticale(scacchiera,csrc,giocatore,avanti = True,case_controllate=True)
        pos_controllate += movimento_verticale(scacchiera,csrc,giocatore,avanti = False,case_controllate=True)
        pos_controllate+= movimento_orizzontale(scacchiera,csrc,giocatore,destra = True,case_controllate=True)
        pos_controllate += movimento_orizzontale(scacchiera,csrc,giocatore,destra = False,case_controllate=True)

        if DEBUG:
            DEBUG_print_caselle(pos_controllate,"case controllate da torre")
        return pos_controllate
    
    def my_name(self):
        return self.nome
    
    def print_my_name(self):
        c = self.colore[0]
        return "R"+c

    #se ha la variabile "mai_mosso"
    def has_mai_mosso(self):
        return True