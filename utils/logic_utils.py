
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
    if giocatore.upper() != pezzo.colore.upper():
        return False
    else:
        return True

# Se io sono "WHITE" --> avversario "BLACK"
def nome_avversario(giocatore):
    if giocatore.upper() == "WHITE":
        return "BLACK"
    else:
        return "WHITE"
    

# @return  [ num_scacchi , pos1, pos2 .. ==> pos dei pezzi che danno scacco al giocatore "giocatore"]
def info_scacchi(scacchiera,giocatore):
    res = []
    avversario  = nome_avversario(giocatore)
    count_scacchi = 0
    pos_re = scacchiera.get_pos_re(giocatore)              #ottengo pos del mio re
    #controllo le caselle controllate da tutti i pezzi nemici, controllo se mi danno scacco
    for i in range(8):
        for j in range(8):
            pezzo = scacchiera.get_pezzo((i,j))
            if pezzo != "empty" and pezzo.colore.upper() == avversario.upper():
                case = pezzo.case_controllate(scacchiera,(i,j), giocatore=avversario)     #destinations sarebbe sbagliato (pensa al pedone)
                if pos_re in case:
                    res.append((i,j))       #questo pezzo mi da scacco
                    count_scacchi += 1
    res.insert(0,count_scacchi)
    return res

# @return lista di posizioni  [(i,j)...]
#Restituisce la linea orrizzontale / verticale / diagonale di caselle da pos scacco a pos_re (non compresi)
# caso orizzontale ==> hai la stessa i, prendi la minore j e vai verso la maggiore creando le posizioni  [i fissa]
# caso verticale ==>  duale
# caso diagonale ==> qui osservi gli indici e vedi che prendi le due posizioni  (i,j) (x,y)
#     Adesso gli indici cambiano entrambi in 4 possibili modi (ovvero le 4 diagonali) per trattarli tutti insieme a partire dalla due posizioni:
#       - se i<x  allora la prima coordinata ++1 ogni nuova posizione  (altrimenti --1) e duale per l'altra indipendetemente!
def case_in_linea(pos_re,pos_scacco):
    pos = []
    #Orizzontale
    if pos_re[0] == pos_scacco[0]:
        i = pos_re[0]                                                          
        left = min(pos_re[1],pos_scacco[1])
        right = max(pos_re[1],pos_scacco[1])
        for j in range(left+1,right):
            pos.append((i,j))
        return pos
    
    #Verticale
    if pos_re[1] == pos_scacco[1]:
        j = pos_re[1]
        left = min(pos_re[0],pos_scacco[0])
        right = max(pos_re[0],pos_scacco[0])
        for i in range(left+1,right):
            pos.append((i,j))
        return pos

    #se arrivo qui allora è per forza diagonale
    #Diagonale   ["cammino" sulla diagonale da  "pos_re" --> "pos_scacco"]
    if pos_re[0] < pos_scacco[0]:           #in questo caso andrà ++1 per i (devo salire la riga..)
        dx = 1
    else:
        dx = -1 
    if pos_re[1] < pos_scacco[1]:
        dy = 1 
    else:
        dy = -1 

    #Prima posizione da aggiungere    (potevo mettere diretto nel ciclo)
    i = pos_re[0] + dx      
    j = pos_re[1] + dy

    while i != pos_scacco[0]:       #oppure j!=pos_scacco[1]
        pos.append((i,j)) 
        i += dx
        j += dy

    return pos

# @return True se ho subito scacco matto da singolo scacco quindi:  
#   1) Non possono muovere il re al sicuro   
#   2) Non posso catturare pezzo che da scacco
#   3) Non posso interporre un pezzo
#  @param  "info_scacchi" sono le informazioni sugli scacchi dati dalla funzoine "info_scacchi"
def matto_da_singolo_scacco(scacchiera,giocatore,info_scacchi):
    #1) Condizione
    pos_re = scacchiera.get_pos_re(giocatore)
    re = scacchiera.get_pezzo(pos_re)
    d = re.destinations(scacchiera,pos_re,giocatore)
    if len(d) > 0:
        return False

    # 2°     [controllo se tra le destinazioni dei miei pezzi {tranne il re} c'è la casella da cui ho ricevuto scacco]
    pos_scacco = info_scacchi[1]        #Se ho un solo scacco qui ho la effettiva posizione di chi mi da scacco
    case_controllate = case_controllate_da_giocatore(scacchiera,giocatore,non_considerare_re=True)
    if pos_scacco in case_controllate:
        return False
    
    # 3°   Interporre un pezzo:   
    #    - vale solo se l'attaccante NON è un cavallo
    #    - data la pos del re e casella che da scacco crea funzione che restituisce le caselle nella linea
    #    - controlla che queste possano essere raggiunte da un mio pezzo (tranne il re!)  [raggiunte == destinations NON case_controllate!]
    pezzo_attaccante = scacchiera.get_pezzo(pos_scacco)
    if pezzo_attaccante.my_name().upper != "KNIGHT":
        case_raggiungibili = case_raggiungibili_da_giocatore(scacchiera,giocatore,non_considerare_re=True)  
        #print(f"{pos_re},{pos_scacco}")     
        case_in_mezzo = case_in_linea(pos_re,pos_scacco)
        #print(f"[DEBUG] case raggiungibili {case_raggiungibili}")
        #print(f"[DEBUG] case in mezzo {case_in_mezzo}")
        for pos in case_in_mezzo:
            if pos in case_raggiungibili:
                return False       #vuol dire che posso interporre un mio pezzo

    #se siamo arrivato fino a qui allora è scacco matto
    print(f"[DEBUG] Scacco matto!")
    return True



# @ return 0 Se non finita
# @ return 1 Se stallo
# @ return 2: (se scacco matto) ovvero
#   - 2.1 doppio scacco e re non può muovesi
#   - 2.2 scacco e re non può muoversi / non si può interporre pezzo / catturare pezzo che da scacco
def partita_finita(scacchiera,giocatore):        
    info = info_scacchi(scacchiera,giocatore)
    num_scacchi = info[0]

    # 1 (stallo --> no sotto scacco, ma zero dest per ogni mio pezzo)
    dest = []
    if num_scacchi==0:
        is_stallo = True
        for i in range(8):
            if not is_stallo:
                    break
            for j in range(8):
                if not is_stallo:
                    break
                pezzo = scacchiera.get_pezzo((i,j))
                if pezzo != "empty" and pezzo.colore.upper() == giocatore.upper():
                    dest = pezzo.destinations(scacchiera, (i,j), giocatore) 
                    if len(dest) >= 1: 
                        is_stallo = False
                       
        if is_stallo:
            return 1


    # 2.1
    if num_scacchi >= 2 :
        pos_re = scacchiera.get_pos_re(giocatore)
        re = scacchiera.get_pezzo(pos_re)
        d = re.destinations(scacchiera,pos_re,giocatore)
        if len(d) == 0:
            return 2
        
    # 2.2 wrappato in funzione
    if num_scacchi == 1:
        if matto_da_singolo_scacco(scacchiera,giocatore,info):
            return 2

    return 0


'''    
    La funzione restituisce le destinazioni possibili del pezzo ma fa controlli preventivi
    - controlla doppio scacco   [devi muovere re ]
    - scacco            [ muovi re / interponi pezzo / catturi pezzo che da scacco]
    - altrimenti restituisci le destinazioni possibili del pezzo selezionato


    # @return : {
      La funzione restituisce:
     - CASO GENERALE: lista di coppie (i,j) ovvero la posizione di destinazione del pezzo
     - CASI SPECIALI:
           - "(i,j,"arrocco")", in tal caso si fa un controllo preventivo
    }
'''
def get_possible_destination(scacchiera,piece,csrc,giocatore):
    #controlla se doppio-scacco in tal caso solo il re può muoversi 
    info = info_scacchi(scacchiera,giocatore)
    num_scacchi = info[0]

    debug=True
    if debug:
        print(f"DEBUG: giocatore: {giocatore}")
        print(f"[DEBUG] Chiamata 'get_poss_dests su: {piece.print_my_name()}")
        print(f"[DEBUG] Info scacchi {info}")

    if num_scacchi >= 2 :
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
    # 1) in questo caso se quel determinato pezzo può catturare chi da scacco ok
    # 2) se non è il re e può interporsi ok
    # 3) se è il re e va in una posizione non attaccata ok 
    if num_scacchi == 1:

        destinations = piece.destinations(scacchiera,csrc,giocatore)
        d_filtrate = []
        pos_scacco = info[1]
        if pos_scacco in destinations:      #1) aggiungo questa dest possibile (cattura pezzo che da scacco)   
            d_filtrate.append(pos_scacco)

        pos_re = scacchiera.get_pos_re(giocatore)
        re = scacchiera.get_pezzo(pos_re)
        #2)
        if piece.my_name() != "King":
            case_in_mezzo = case_in_linea(pos_re,pos_scacco)  
            for pos in case_in_mezzo:
                if pos != csrc:
                    d_filtrate.append(pos)  
        else:#3)
            d_filtrate= re.destinations(scacchiera,csrc,giocatore)          #questo in realtà non ci sarebbe bisogno di farlo
    

        d_set = set(destinations)
        d_filtrate_set = set(d_filtrate)

        return d_set & d_filtrate_set


    destinations = piece.destinations(scacchiera,csrc,giocatore)
    return destinations




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
            if destinazioni  and pezzo_nemico(pezzo,giocatore):             #se voglio le destinazioni del pezzo allora aggiungo solo se il pezzo è nemico
                dest.append(pos)
            break 
    return dest


# Se destination = True
# @return  tutte le casella valide e vuote seguendo il movimento del re (una casella ogni direzione)
# Se case_controllate = True --> il filtro non viene applicato 
# NOTA: non viene effettuato il controllo speciale per il re (quello è compito del suo metodo così la funzione viene usata ad es anche per la regina)
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

    if destinazioni:    #se guardiamo le destinazioni allora devono essere vuote (o pezzo nemico)   [MODIFICATO QUESTO]
        tmp = []
        for pos in dest:
            if scacchiera.casella_vuota(pos):
                tmp.append(pos) 
            else:
                piece = scacchiera.get_pezzo(csrc)
                pezzo = scacchiera.get_pezzo(pos)
                if pezzo.colore.upper() != piece.colore.upper():
                    tmp.append(pos) 
        dest = tmp    
        
    return dest

# es se direzione= avanti_sx allora lo step_i = +1, step_j = -1  [provoca movimento diag a sinistra]
def calcola_step(direzione):
    if direzione == "avanti_sx":
        return [+1,-1]
    elif direzione == "avanti_dx":
        return [+1,+1]
    elif direzione == "indietro_sx":
        return [-1,-1]
    elif direzione == "indietro_dx":
        return [-1,+1]
    else:
        raise Exception("Direzione non esistente")

# @input: direzione (es avanti_sx) e destinazioni=True o case_controllate=True
# return: le possibili destinazioni / case controllate dalla casella csrc in quella diagonale (avanti_sx / avanti_dx / indietro_sx / indietro_dx)
def movimento_diagonale(scacchiera,csrc,giocatore,direzione,destinazioni=False,case_controllate=False):
    dest = []
    if destinazioni  and case_controllate:
        raise Exception("API [movimento_diagonale] si aspetta o destinazioni=True o case_controllate=True")
    step_i , step_j = calcola_step(direzione)
    start_pos = (csrc[0],csrc[1])
    next_pos = (start_pos[0]+step_i, start_pos[1] + step_j)        #Calcolo la prossima pos in base alla direzione (i +/- 1 e j +/- 1)

    while scacchiera.casella_valida(next_pos):      #Logica simile a "Movimento_orizzontale.." esco se casella non valida o incontrato pezzo

        if scacchiera.casella_vuota(next_pos):
            dest.append(next_pos)
        else:
            pezzo = scacchiera.get_pezzo(next_pos)
            if case_controllate:            #se voglio case controllate dal pezzo aggiungo a prescindere
                dest.append(next_pos)
            if destinazioni  and pezzo_nemico(pezzo,giocatore):             #se voglio le destinazioni del pezzo allora aggiungo solo se il pezzo è nemico
                dest.append(next_pos)
            break   # 2° caso d'uscita
        next_pos = (next_pos[0]+step_i, next_pos[1] + step_j)      

    return dest


# return: le possibili destinazioni / case controllate del cavallo
def movimento_cavallo(scacchiera,csrc,giocatore,destinazioni=False,case_controllate=False):
    dest = []
    if destinazioni  and case_controllate:
        raise Exception("API [movimento_diagonale] si aspetta o destinazioni=True o case_controllate=True")
    start_pos = (csrc[0],csrc[1])
    #Il cavallo ha 8 possibili posizioni, controlla solo se valida per "case_controllate" e se vuota o nemica per "destinazioni"
    avanti_dx = (start_pos[0]+2 , start_pos[1]+1)               #fatto così per leggibilità
    avanti_sx = (start_pos[0]+2 , start_pos[1]-1)
    destra_dx = (start_pos[0]-1 , start_pos[1]+2)
    destra_sx = (start_pos[0]+1 , start_pos[1]+2)
    indietro_dx = (start_pos[0]-2 , start_pos[1]+1) 
    indietro_sx = (start_pos[0]-2 , start_pos[1]-1) 
    sinistra_dx = (start_pos[0]-1 , start_pos[1]-2) 
    sinistra_sx = (start_pos[0]+1 , start_pos[1]-2) 
    dest = [avanti_dx, avanti_sx, destra_dx, destra_sx, indietro_dx, indietro_sx, sinistra_dx, sinistra_sx]

    dest = [ pos for pos in dest if scacchiera.casella_valida(pos)  ]           #primo filtro

    if destinazioni:            #controllo se vuota o c'è un pezzo nemico
        tmp = []
        for pos in dest:
            if scacchiera.casella_vuota(pos):
                tmp.append(pos)
            else:
                pezzo = scacchiera.get_pezzo(pos)
                if pezzo_nemico(pezzo,giocatore):
                    tmp.append(pos)
        dest = tmp

    return dest


def DEBUG_print_caselle(positions,str=""):
    print("[DEBUG] caselle stampate," + str)
    if len(positions) == 0:
        print(0)
    for pos in positions:
        print(posTOstring(pos),end=" ")
    print()


# @return TUTTE le case controllate dal giocatore
# -  se "togli_re = True" si fa la stessa cosa ma togliendo temporaneamente il re del giocatore "colore_re", motivo in re.destinations
# - se "Non_considerare_re" allora il re non partecipa alle case controllate
def case_controllate_da_giocatore(scacchiera,giocatore,togli_re=False,colore_re="", non_considerare_re=False):
    if togli_re:    #tolgo temp il re   
        if colore_re=="":
            raise Exception("Aggiungi il colore del re")
        pos_re = scacchiera.get_pos_re(colore_re)
        re = scacchiera.get_pezzo(pos_re)
        scacchiera.aggiungi_pezzo("empty",pos_re)

    case = set()
    for i in range(8):
        for j in range(8):
            pezzo = scacchiera.get_pezzo((i,j))

            if pezzo != "empty" and pezzo.colore.upper() == giocatore.upper():
                if non_considerare_re and pezzo.my_name().upper() == "KING":
                        continue
                else:
                    case.update(pezzo.case_controllate(scacchiera,(i,j),giocatore)) 
    #rimetto il re
    if togli_re:    #rimetto
        scacchiera.aggiungi_pezzo(re,pos_re)

    return list(case)

# @return TUTTE le case raggiungibili dal giocatore  (destinations)
# - se "Non_considerare_re" allora il re non partecipa alle case raggiungibili 
def case_raggiungibili_da_giocatore(scacchiera,giocatore,non_considerare_re=True):
    case = set()
    for i in range(8):
        for j in range(8):
            pezzo = scacchiera.get_pezzo((i,j))

            if pezzo != "empty" and pezzo.colore.upper() == giocatore.upper():
                if non_considerare_re and pezzo.my_name().upper() == "KING":
                        continue
                else:
                    case.update(pezzo.destinations(scacchiera,(i,j),giocatore)) 

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