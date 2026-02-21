
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
            #pezzo_catturato =  scacchiera.get_pezzo(posD)

        scacchiera.aggiungi_pezzo(self,posD)
        return "Non Promozione"

    #   @return tutte le caselle che il pezzo può raggiungere da quella posizione
    def destinations(self, scacchiera, csrc, giocatore):
        return (-1,-1)
    
    # @return tutte le caselle controllate dal pezzo (diverse da quelle che può raggiungere, es qui non considera pezzo pinnato) 
    def case_controllate(self, scacchiera, csrc, giocatore=""):
        return (-1,-1)
    
    def my_name(self):
        return "Piece"
    
    #Tengo questa informazioni solo per Torre pedone e re
    def has_mai_mosso(self):
        return False
    
    #Se destinazioni del pezzo vanno filtrate se il pezzo è inchiodato, lo è se togliendo il pezzo aumenta di 1 gli scacchi che subisco [potrei già star ricevendone uno]
    # in tal caso riconosco quale sia lo scacco che nasce dal togliere questo pezzo, e io potrò muovere questo pezzo SOLO nelle case in linea tra 
    # questo scacco e il pezzo inchiodato (o il pezzo stesso).  (questo è come funziona l'inchiodatura lungo uno scacco) {inchiodatura lunga 2+ direzioni impossibile}
    def filtro_inchiodatura(self,scacchiera,csrc,destinazioni):
        case_mantengono_inchiodatura = []           #se pinnato queste sono le case che non espongono il re
        # Controllo se pinnato 
        info = info_scacchi(scacchiera,self.colore)
        scacchiera.aggiungi_pezzo("empty",csrc)         #mi tolgo temporaneamente

        info_nuove = info_scacchi(scacchiera,self.colore)

        #riaggiungo pezzo
        scacchiera.aggiungi_pezzo(self,csrc)
        if info[0] < info_nuove[0]:
            print(f"[DEBUG] pezzo pinnato  {self.my_name()}")
        
            #adesso devo riconoscere quale scacco è provocato dalla rimozione
            scacchi = info_nuove[1::]                   #copia tutta la lista ad eccezione di l[0]
            pos_re = scacchiera.get_pos_re(self.colore)             #mio re
            for scacco in scacchi:
                case_in_mezzo = case_in_linea(pos_re,scacco)
                if csrc in case_in_mezzo:                                   #allora questo è la linea dell'inchiodatura
                    case_mantengono_inchiodatura = case_in_mezzo
                case_mantengono_inchiodatura.append(scacco)                     #sarebbe la cattura del pezzo che mi inchioda

            # finalmente adesso le destinazioni del pezzo sono le sue calcolate in precedenza da "destinations" ma che sono in linea con l'inchiodatura
            ds = set(destinazioni)
            cmis = set(case_mantengono_inchiodatura)
            unione = ds & cmis

            return list(unione)
        
        else:
            return destinazioni