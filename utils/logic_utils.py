
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

# Se io sono "WHITE" --> avversario "BLACK"
def nome_avversario(giocatore):
    if giocatore.upper() == "WHITE":
        return "BLACK"
    else:
        return "WHITE"
    
#Il giocatore è sotto doppio scacco se 2 pezzi nemici hanno come "case controllate" quella del mio re
# nota --> questo implicitamente implica che lo scacco avvenga da due direzioni e quindi il re si deve muovere
def doppio_scacco(scacchiera,giocatore):
    avversario  = nome_avversario(giocatore)
    count_scacchi = 0
    pos_re = scacchiera.get_pos_re(giocatore)              #ottengo pos del mio re
    #controllo le caselle controllate da tutti i pezzi nemici e vedo se mi danno più di uno scacco
    for i in range(8):
        for j in range(8):
            pezzo = scacchiera.get_pezzo((i,j))
            if pezzo != "empty" and pezzo.colore.upper() == avversario:
                case = pezzo.case_controllate(scacchiera,(i,j), giocatore=avversario)
                if pos_re in case:
                    count_scacchi += 1
    if count_scacchi > 1:
        return True
    else:
        return False

# @ return 0 Se non finita
# @ return 1 Se stallo
# @ return 2: (se scacco matto) ovvero
#   - 2.1 doppio scacco e re non può muovesi
#   - 2.2 scacco e re non può muoversi / non si può interporre pezzo / catturare pezzo che da scacco
def partita_finita(scacchiera,giocatore):
    # 2.1
    if doppio_scacco(scacchiera,giocatore):
        pos_re = scacchiera.get_pos_re(giocatore)
        re = scacchiera.get_pezzo(pos_re)
        d = re.destinations(scacchiera,pos_re,giocatore)
        if len(d) == 0:
            return 2
    #[TODO]


    return 0


'''    
    La funzione restituisce le destinazioni possibili del pezzo ma fa controlli preventivi
    - controlla doppio scacco   [devi muovere re / se non puoi end-game]
    - scacco            [ muovi re / interponi pezzo / catturi pezzo che da scacco]
    - altrimenti restituisci le destinazioni possibili del pezzo selezionato


    # @return : {
      La funzione restituisce:
     - CASO GENERALE: lista di coppie (i,j) ovvero la posizione di destinazione del pezzo
     - CASI SPECIALI:
           - "end-game", se la partita è finita
           - "(i,j,"arrocco")", in tal caso si fa un controllo preventivo
    }
'''
def get_possible_destination(scacchiera,piece,csrc,giocatore):
    #controlla se doppio-scacco in tal caso solo il re può muoversi 
    if doppio_scacco(scacchiera,giocatore):
        pos_re = scacchiera.get_pos_re(giocatore)
        re = scacchiera.get_pezzo(pos_re)
        destinations = re.destinations(scacchiera,pos_re,giocatore)
        if len(destinations) == 0:
            raise Exception("La partita dovrebbe essere terminata")
        if piece.my_name() == "King":
            return piece.destinations(scacchiera,csrc,giocatore)
        else:
            return []       #ovvero ho provato a muovere un altro pezzo diverso dal re
                
        
    # scacco singolo

    # LOGICA DA AGGIUNGERE
    # pezzo pinnato
    # aggiungi mossa en-passant   
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
        raise Exception("API chiamata incorrettamente")
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
        raise Exception("API chiamata incorrettamente")
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


# Se destination = True
# @return  tutte le casella valide e vuote seguendo il movimento del re (una casella ogni direzione)
# Se case_controllate = True --> le caselle non devono essere vuote
def movimento_re(scacchiera,csrc,destinazioni=False,case_controllate=False):
    if destinazioni  and case_controllate:
        raise Exception("API chiamata incorrettamente")
    #al più 8
    dest = []
    pos_avanti = (csrc[0]+1,csrc[1])                # POV bianco, ma è uguale, così per leggibilità
    pos_indietro = (csrc[0]-1,csrc[1])
    pos_dx = (csrc[0],csrc[1]+1)
    pos_sx = (csrc[0],csrc[1]-1)
    diag_avanti_sx = (csrc[0]+1,csrc[1]-1)
    diag_avanti_dx = (csrc[0]+1,csrc[1]+1)
    diag_indietro_sx = (csrc[0]-1,csrc[1]-1)
    diag_indietro_dx = (csrc[0]-1,csrc[1]+1)

    dest.extend([pos_avanti,pos_indietro,pos_dx,pos_sx,diag_avanti_dx,diag_avanti_sx,diag_indietro_dx,diag_indietro_sx])

    #filtra se valida 
    dest = [ pos for pos in dest if scacchiera.casella_valida(pos)   ]

    if destinazioni:    #se guardiamo le destinazioni allora devono essere vuote
        dest = [ pos for pos in dest if scacchiera.casella_vuota(pos)   ]
        
    return dest

def DEBUG_print_caselle(positions,str=""):
    print("[DEBUG] caselle stampate," + str)
    if len(positions) == 0:
        print(0)
    for pos in positions:
        print(posTOstring(pos),end=" ")
    print()


# @return TUTTE le case controllate dal giocatore, se "togli_re = True" si fa la stessa cosa ma togliendo temporaneamente il re del giocatore "colore_re", motivo in re.destinations
def case_controllate_da_giocatore(scacchiera,giocatore,togli_re=False,colore_re=""):
    if togli_re == True:    #tolgo temp il re
        pos_re = scacchiera.get_pos_re(colore_re)
        re = scacchiera.get_pezzo(pos_re)
        scacchiera.aggiungi_pezzo("empty",pos_re)

    case = set()
    for i in range(8):
        for j in range(8):
            pezzo = scacchiera.get_pezzo((i,j))
            if pezzo != "empty" and pezzo.colore.upper() == giocatore.upper():
                case.update(pezzo.case_controllate(scacchiera,(i,j),giocatore)) 
    #rimetto il re
    if togli_re == True:    #rimetto
        scacchiera.aggiungi_pezzo(re,pos_re)

    return list(case)



# input:  lista  [(i,j)...], potenzialmente mosse speciali come arrocco: (i,j,"arrocco")
# return: le mosse (i,j) del tipo (i,j,"Arrocco") se stai cercando ad esempio per mosse speciali "Arrocco"  [togliendo quindi "arrocco"]
def trova_special_move(mosse,nome_mossa_speciale="Arrocco"):
    mosse_speciali = []
    for mossa in mosse:
        if len(mossa) == 3 and mossa[2]==nome_mossa_speciale:
            move_ij = (mossa[0],mossa[1])
            mosse_speciali.append(move_ij)
    return mosse_speciali

# da cdest(i,j) capiamo se arrocco corto/lungo per bianco/nero  [ASSUMO già fatto i controlli necessari]
# es se cdest == (0,6) ==> arrocco corto bianco
def effettua_arrocco(scacchiera,cdest):

    if cdest == (0,6):                          #arrocco corto bianco
        re = scacchiera.get_pezzo((0,4))
        torre = scacchiera.get_pezzo((0,7))
        re.sposta(scacchiera,(0,4),cdest)
        torre.sposta(scacchiera,(0,7),(0,5))

    elif cdest == (0,2):                        #arrocco lungo bianco
        re = scacchiera.get_pezzo((0,4))
        torre = scacchiera.get_pezzo((0,0))
        re.sposta(scacchiera,(0,4),cdest)
        torre.sposta(scacchiera,(0,0),(0,3))

    elif cdest == (7,6):                        #arrocco corto bianco
        re = scacchiera.get_pezzo((7,4))
        torre = scacchiera.get_pezzo((7,7))
        re.sposta(scacchiera,(7,4),cdest)
        torre.sposta(scacchiera,(7,7),(7,5))
    
    elif cdest == (7,2):                        #arrocco lungo bianco
        re = scacchiera.get_pezzo((7,4))
        torre = scacchiera.get_pezzo((7,0))
        re.sposta(scacchiera,(7,4),cdest)
        torre.sposta(scacchiera,(7,0),(7,3))
    else:
        raise Exception("Chiamato arrocco ma con destinazione del re non valida")