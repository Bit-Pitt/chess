from utils.logic_utils import *
from .pezzo import Pezzo

class Pedone(Pezzo):
    def __init__(self,colore):
        super().__init__(colore)
        self.nome = "pawn"
        self.mai_mosso = True   #serve per poter giocare la prima mossa da due salti 

    def sposta(self,scacchiera,csrc,cdest):
        super().sposta(scacchiera,csrc,cdest)  
        self.mai_mosso = False
    

    # Il pedone si muove di:
    # - 1) in avanti o due in avanti [se non ha pezzi in mezzo!]
    # - 2) se nelle due caselli diagonali ha un pezzo nemico anche quelle!
    # - 3) se pedone bianco si muove in avanti di una riga se nero indietro!
    # @return tutte le destinazioni possibili (i,j)
    def destinations(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Pawn":
            raise TypeError("[Internal error] Non è presente un pedone nella casella!")
        dest = []

        #####################################
        # LOGICA PER GIOCATORE BIANCO            (differenzio solo per i pedoni che vanno uni-direzionali)
        #####################################
        if giocatore.upper() == "WHITE":
            # 1) 
            uno_avanti = (csrc[0]+1,csrc[1])     #ovvero una riga più in su
            if scacchiera.casella_valida(uno_avanti) and scacchiera.casella_vuota(uno_avanti):
                dest.append(uno_avanti) 
            # 2)
            due_avanti = (csrc[0]+2,csrc[1])  
            caselle = [uno_avanti,due_avanti]
            if pezzo.mai_mosso and  scacchiera.caselle_valide(caselle) and scacchiera.caselle_vuote(caselle):
                dest.append(due_avanti)

            # 3)    La casella deve essere occupata da avversario
            diag_sx =  (csrc[0]+1,csrc[1]-1) 
            if scacchiera.casella_valida(diag_sx) and not scacchiera.casella_vuota(diag_sx):
                piece = scacchiera.get_pezzo(diag_sx)
                if piece.colore.upper() == "BLACK":
                    dest.append(diag_sx) 

            diag_dx =   (csrc[0]+1,csrc[1]+1)

            if scacchiera.casella_valida(diag_dx):
                print(f"[DEBUG] Valida: {diag_dx}")
                
            if scacchiera.casella_valida(diag_dx) and not scacchiera.casella_vuota(diag_dx):
                piece = scacchiera.get_pezzo(diag_dx)
                if piece.colore.upper() == "BLACK":
                    dest.append(diag_dx) 

        #####################################
        # LOGICA PER GIOCATORE NERO            
        #####################################
        if giocatore.upper() == "BLACK":
            # 1) 
            uno_avanti = (csrc[0]-1,csrc[1])     #ovvero una riga più in giù
            if scacchiera.casella_valida(uno_avanti) and scacchiera.casella_vuota(uno_avanti):
                dest.append(uno_avanti) 
            # 2)
            due_avanti = (csrc[0]-2,csrc[1])  
            caselle = [uno_avanti,due_avanti]
            if pezzo.mai_mosso and  scacchiera.caselle_valide(caselle) and scacchiera.caselle_vuote(caselle):
                dest.append(due_avanti)

            # 3)    La casella deve essere occupata da avversario       (diag sx dalla prospettiva del bianco)[ma è uguale tanto dopo fai l'altra]
            diag_sx =  (csrc[0]-1,csrc[1]+1) 
            if scacchiera.casella_valida(diag_sx) and not scacchiera.casella_vuota(diag_sx):
                piece = scacchiera.get_pezzo(diag_sx)
                if piece.colore.upper() == "WHITE":
                    dest.append(diag_sx) 

            diag_dx =   (csrc[0]-1,csrc[1]-1)
            if scacchiera.casella_valida(diag_dx) and not scacchiera.casella_vuota(diag_dx):
                piece = scacchiera.get_pezzo(diag_dx)
                if piece.colore.upper() == "WHITE":
                    dest.append(diag_dx) 
    
        return dest
    
    #Il pedone controlla le due case diagonali
    def case_controllate(self, scacchiera, csrc, giocatore):

        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "Pawn":
            raise TypeError("[Internal error] Non è presente un pedone nella casella!")
        pos_controllate = []

        if giocatore.upper() == "WHITE":
            diag_sx = (csrc[0]+1,csrc[1]-1) 
            diag_dx = (csrc[0]+1,csrc[1]+1)
        else:
            diag_sx = (csrc[0]-1,csrc[1]+1) 
            diag_dx = (csrc[0]-1,csrc[1]-1)

        if scacchiera.casella_valida(diag_dx):
            pos_controllate.append(diag_sx)
        if scacchiera.casella_valida(diag_dx):
            pos_controllate.append(diag_dx)

        return pos_controllate

    
    def my_name(self):
        return "Pawn"
    
    def print_my_name(self):
        c = self.colore[0]
        return "P"+c

    def has_mai_mosso(self):
        return True