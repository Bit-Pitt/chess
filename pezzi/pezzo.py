
from utils.logic_utils import *

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
        
        pos_s = (csrc[0],csrc[1])
        scacchiera.aggiungi_pezzo("empty",pos_s)
        posD = (cdest[0],cdest[1])
        if not scacchiera.casella_vuota(cdest):
            print("Catturato un pezzo!")
            pezzo_catturato =  scacchiera.get_pezzo(posD)

        scacchiera.aggiungi_pezzo(self,posD)
        return pezzo_catturato

    #   @return tutte le caselle che il pezzo può raggiungere da quella posizione
    def destinations(self, scacchiera, csrc, giocatore):
        return (-1,-1)
    
    # @return tutte le caselle controllate dal pezzo (diverse da quelle che può raggiungere) 
    def case_controllate(self, scacchiera, csrc, giocatore=""):
        return (-1,-1)
    
    def my_name(self):
        return "Piece"
    
    #Tengo questa informazioni solo per Torre pedone e re
    def has_mai_mosso(self):
        return False