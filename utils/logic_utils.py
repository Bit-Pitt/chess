
################################################
# Qui le funzioni utili per la logica del gioco
################################################
from .graphic_utils import *



def valore_pezzo(pezzo):
    if pezzo == "empty" or pezzo.my_name() == "King":
        return 0
    if pezzo.my_name() == "Pawn":
        return 1 
    if pezzo.my_name() == "Bishop" or pezzo.my_name() == "Knight":
        return 3 
    if pezzo.my_name() == "Rook":
        return 5
    if pezzo.my_name() == "Queen":
        return 9
    raise Exception("Nome del pezzo non riconosciuto [fun:valore_pezzo]")


#controlla che il pezzo sia del giocatore
def controlla_giocatore(giocatore,pezzo):
    if giocatore.upper() != pezzo.my_name().upper():
        return False
    else:
        return True
    


'''     Regole da seguire       
--> funzione da usare "caselle controllate" da nemico [!= da destinations anche se simile] 
--> per fun caselle controllate (simile a "destinations") usare le stesse utility del tipo:
     [caselle_diagonali -->  restituisce TUTTE le caselle diag poi dest filtra quelle in cui può andare l'alfiere mentre "caselle controllate" 
                                aggiunge anche quelle che effettivametne controlla, poi la funzione "raggi_x" che servirà per le possibili inchiodature un ulteriore filtro diverso
# se mossa valida ovvero:
    # - la casella è raggiungibile  [fatti tornare dalla classe lista di coppie (i,j)]
    # - se non passa attraverso altri pezzi (eccez cavallo)
    # - se non è inchiodato!  {controllo preventivo da aggiungere a tutti}

    #altri casi PREVENTIVI :  
    # se pezzo il  re non permettere  casella  già minacciate
    # mosse speciali (arrocco /  en-passant)
    # se sono sotto scacco --> permetto di muovere il re, interporre un pezzo (se non cavallo) , catturare il pezzo   
    #  DOPPIO SCACCO    {doppio-scacco da direzioni diverse!} --> in questo caso permetti SOLO di muovere il re
    # promozione pedone

    # return "end-game" se ...
'''
def get_possible_destination(scacchiera,piece,csrc,giocatore):
    #controlla se doppio-scacco
    # scacco 
    # pezzo pinnato
    # aggiungi mossa en-passant   / arrocco   [magari come speciali]
    destinations = piece.destinations(scacchiera,csrc,giocatore)
    return destinations

# @return tutte le caselle (i,j) seguendo il movimento della torre [scacchiera vuota]
def movimento_torre(csrc):
    i = csrc[0]
    j = csrc[1]
    pos_verticali = []
    for k in range(8):
        if k != i:                  #non voglio mettere la posizione dove si trova il pezzo
            pos_verticali.append((k,j))
    pos_orizzontali = []
    for k in range(8):
        if k != j:                  #non voglio mettere la posizione dove si trova il pezzo
            pos_orizzontali.append((i,k))

    return pos_orizzontali+pos_verticali


# @return Es giocatore = "White" se pezzo è del black --> True
def pezzo_nemico(pezzo,giocatore):
    if pezzo == "empty":
        raise Exception("Internal error, dovrebbe essere passato un pezzo")
    if pezzo.colore.upper() == giocatore.upper():
        return False
    else:
        return True


# SE destinazioni=True
# @return le possibili destinazioni del pezzo se può muoversi in verticale
# @return case movimento in avanti [mi fermo se incontro un pezzo, se nemico aggiungo la pos]
# SE case_controllate=True
# @return tutte le case controllate dal pezzo in direzione verticale  
# @return case movimento in avanti [mi fermo se incontro un pezzo,in OGNI CASO aggiungo la pos]

def movimento_verticale(scacchiera,csrc,giocatore,avanti,destinazioni=False,case_controllate=False):
    if destinazioni  and case_controllate:
        raise Exception("Internal errore in movimento_verticale")
    dest = []
    i = csrc[0]         #pos (i,j) del pezzo
    j = csrc[1]  

    if avanti == True:          #se in vanti mi muovo da (i,j) del pezzo in (i+1..8,j)
        l = i+1 
        r = 8    
        passo = 1 
    else:                       #indietro   (i,j) --> (i-1..0,j)
        l = i-1
        r = -1 
        passo = -1 

    #mi muovo e mi fermo se incontro un pezzo 
    for k in range(l,r,passo):
        pos = (k,j)
        if scacchiera.casella_vuota(pos):
            dest.append(pos)
        else:
            pezzo = scacchiera.get_pezzo((k,j))
            if case_controllate:            #se voglio case controllate dal pezzo aggiungo a prescindere
                dest.append(pos)
            if destinazioni  and pezzo_nemico(pezzo,giocatore):             #se voglio le destinazioni del pezzo solo se il pezzo è nemico
                dest.append(pos)
            break 
    return dest

# Analogo di "destinazioni_verticali"
def movimento_orizzontale(scacchiera,csrc,giocatore,destra,destinazioni=False,case_controllate=False):
    if destinazioni  and case_controllate:
        raise Exception("Internal errore in movimento_orizzontale")
    dest = []
    i = csrc[0]         #pos (i,j) del pezzo
    j = csrc[1]  

    if destra == True:          #se dx mi muovo da (i,j) del pezzo in (i,j+1..8)
        l = j+1 
        r = 8    
        passo = 1 
    else:                       #indietro   (i,j) --> (i,j-1..0)
        l = j-1
        r = -1 
        passo = -1 

    #mi muovo e mi fermo se incontro un pezzo, se nemico aggiungo la pos
    for k in range(l,r,passo):
        pos = (i,k)
        if scacchiera.casella_vuota(pos):
            dest.append(pos)
        else:
            pezzo = scacchiera.get_pezzo((i,k))
            if case_controllate:            #se voglio case controllate dal pezzo aggiungo a prescindere
                dest.append(pos)
            if destinazioni  and pezzo_nemico(pezzo,giocatore):             #se voglio le destinazioni del pezzo solo se il pezzo è nemico
                dest.append(pos)
            break 
    return dest