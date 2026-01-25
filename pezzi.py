'''
    In questo file sono contenute le classi che rappresentano i vari pezzi
'''
from utils import * 
# TODO: per miglior pulizia codice bisogna tenere privati attributi privati e gestibili solo dalla classe come il colore del pezzo etc
#Classe generica (funge da "interfaccia" per descrivere il comportamento ovvero metodi in comune con le classi che la estendono)
class Pezzo:
    def __init__(self,colore):
        self.colore = colore            

    #Sposto il pezzo (già effettuati i controlli necessari)
    # Porto il pezzo nella nuova posizione
    # Svuoto la casella di partenza
    def sposta(self,scacchiera,csrc,cdest):
        pezzo_catturato = "empty"
        scacchiera[csrc[0]][csrc[1]] = "empty"
        if not casella_vuota(scacchiera,cdest):
            print("Catturato un pezzo!")
            pezzo_catturato =  scacchiera[cdest[0]][cdest[1]]
        scacchiera[cdest[0]][cdest[1]] = self 
        return pezzo_catturato

    #   @return tutte le caselle controllate da quella posizione
    def destinations(self,scacchiera):
        return 0
    
    def my_name(self):
        return "Piece"
    
    #Tengo questa informazioni solo per Torre pedone e re
    def has_mai_mosso(self):
        return False
        
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
        pezzo = scacchiera[csrc[0]][csrc[1]]
        if pezzo.my_name() != "Pawn":
            raise TypeError("[Internal error] Non è presente un pedone nella casella!")
        dest = []

        #####################################
        # LOGICA PER GIOCATORE BIANCO            (differenzio solo per i pedoni che vanno uni-direzionali)
        #####################################
        if giocatore.upper() == "WHITE":
            # 1) 
            uno_avanti = (csrc[0]+1,csrc[1])     #ovvero una riga più in su
            if casella_valida(uno_avanti) and casella_vuota(scacchiera,uno_avanti):
                dest.append(uno_avanti) 
            # 2)
            due_avanti = (csrc[0]+2,csrc[1])  
            caselle = [uno_avanti,due_avanti]
            if pezzo.mai_mosso and  caselle_valide(caselle) and caselle_vuote(scacchiera,caselle):
                dest.append(due_avanti)

            # 3)    La casella deve essere occupata da avversario
            diag_sx =  (csrc[0]+1,csrc[1]-1) 
            if casella_valida(diag_sx) and not casella_vuota(scacchiera,diag_sx):
                piece = scacchiera[diag_sx[0]][diag_sx[1]]
                if piece.colore.upper() == "BLACK":
                    dest.append(diag_sx) 

            diag_dx =   (csrc[0]+1,csrc[1]+1)
            if casella_valida(diag_dx) and not casella_vuota(scacchiera,diag_dx):
                piece = scacchiera[diag_dx[0]][diag_dx[1]]
                if piece.colore.upper() == "BLACK":
                    dest.append(diag_dx) 

        #####################################
        # LOGICA PER GIOCATORE NERO            
        #####################################
        if giocatore.upper() == "BLACK":
            # 1) 
            uno_avanti = (csrc[0]-1,csrc[1])     #ovvero una riga più in giù
            if casella_valida(uno_avanti) and casella_vuota(scacchiera,uno_avanti):
                dest.append(uno_avanti) 
            # 2)
            due_avanti = (csrc[0]-2,csrc[1])  
            caselle = [uno_avanti,due_avanti]
            if pezzo.mai_mosso and  caselle_valide(caselle) and caselle_vuote(scacchiera,caselle):
                dest.append(due_avanti)

            # 3)    La casella deve essere occupata da avversario       (diag sx dalla prospettiva del bianco)[ma è uguale tanto dopo fai l'altra]
            diag_sx =  (csrc[0]-1,csrc[1]+1) 
            if casella_valida(diag_sx) and not casella_vuota(scacchiera,diag_sx):
                piece = scacchiera[diag_sx[0]][diag_sx[1]]
                if piece.colore.upper() == "WHITE":
                    dest.append(diag_sx) 

            diag_dx =   (csrc[0]-1,csrc[1]-1)
            if casella_valida(diag_dx) and not casella_vuota(scacchiera,diag_dx):
                piece = scacchiera[diag_dx[0]][diag_dx[1]]
                if piece.colore.upper() == "WHITE":
                    dest.append(diag_dx) 
    
        return dest
    
    def my_name(self):
        return "Pawn"
    
    def print_my_name(self):
        c = self.colore[0]
        return "P"+c

    def has_mai_mosso(self):
        return True
