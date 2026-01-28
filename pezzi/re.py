from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = True

class Re(Pezzo):
    def __init__(self,colore):
        super().__init__(colore)
        self.nome = "King"
        self.mai_mosso = True   #per possibile arrocco

    def sposta(self,scacchiera,csrc,cdest):
        super().sposta(scacchiera,csrc,cdest)  
        self.mai_mosso = False
    

    # Possibili destinazioni re:
    # - 1) tutte le direzioni ma una casella di passo
    # - 2) Non devono essere controllate da altri pezzi nemici!
    # - 3) arrocco   
    # @return tutte le destinazioni possibili (i,j)
    def destinations(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "King":
            raise TypeError("[Internal error] Non è presente il re nella casella!")
        dest = []

        #1)
        dest = movimento_re(scacchiera,csrc,destinazioni=True)
        #2)
        avversario = nome_avversario(giocatore)
        controllate_da_avversario = case_controllate_da_giocatore(scacchiera,avversario)

        dest = [ pos for pos in dest if pos not in controllate_da_avversario]

        #3)   [ottieni le due torri (se mai mosse sono li)]
        mosse_speciali = self.arrocco(scacchiera,csrc,giocatore,controllate_da_avversario)


        if DEBUG:
            DEBUG_print_caselle(dest,"destinazioni possibili del re:")
        
        return dest
    

    def case_controllate(self, scacchiera, csrc, giocatore=""):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "King":
            raise TypeError("[Internal error] Non è presente un pedone nella casella!")
        pos_controllate = []

        pos_controllate += movimento_re(scacchiera,csrc,case_controllate=True)

        if DEBUG:
            DEBUG_print_caselle(pos_controllate,"case controllate dal re:")

        return pos_controllate
    
    def my_name(self):
        return self.nome
    
    def print_my_name(self):
        c = self.colore[0]
        return "K"+c

    #se ha la variabile "mai_mosso"
    def has_mai_mosso(self):
        return True
    
    #Ritorna la destinazione per il re (i,j) se può arroccare   [es arrocco corto bianco ritorna --> g1]    
    def arrocco(self,scacchiera,csrc,giocatore,controllate_da_avversario):
        #controlla  i due arrocchi per nero e bianco se re mai mosso, torre mai mossa, se case dove si muove il re NON controllate da nemico

        #if not self.mai_mosso
        return 