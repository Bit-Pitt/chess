'''
        LIST OF FUNCTION

                Giocatori related:
def controlla_nome(piece,nome):
def controlla_giocatore(giocatore,pezzo):


                Schacchiera related:
def valore_pezzo(pezzo):
def stringTOpos(string):
def traduci_nome(iniziale):
def nomePezzoInCasella(pezzo):
def print_scacchiera(scacchiera):
def print_pezzi_persi(pezzi_persi,color):    [TODO]
def vantaggio(scacchiera):
def casella_vuota(scacchiera,pos):
def caselle_vuote(scacchiera,caselle):
def casella_valida(pos):
def caselle_valide(caselle):
''' 




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


# converte pos in stringa to mat indexes   "B5-->[4][1]"
def stringTOpos(string):

    if len(string)!= 2:
        raise TypeError("Stringa da convertire non valida")
    
    col = ord(string[0].upper()) - ord('A') 
    row = int(string[1])-1
    return (row,col)

# Es  "P" --> "Pawn"
def traduci_nome(iniziale):
    if iniziale.upper() == "P":
        return "Pawn"
    if iniziale.upper() == "R":
        return "Rook"
    if iniziale.upper() == "K":
        return "King"
    if iniziale.upper() == "Q":
        return "Queen"
    if iniziale.upper() == "B":
        return "Bishop"
    if iniziale.upper() == "C":
        return "Knight"
    raise Exception("Iniziale del pezzo non riconosciuta [fun: traduci_nome]")



def nomePezzoInCasella(pezzo):
    if pezzo == "empty":
        return ""
    else:
        return pezzo.print_my_name()
    

# 8 spazi per casella es    | pb     | empty  |  ....  
# Stampo righe in reverse per aver effetto scacchiera classica
def print_scacchiera(scacchiera):
    print("\n\n")
    spazi_per_casella = 6
    for i in range(7,-1,-1):                    #7 6 .. 1 0
        print("---------------------------------------------------------")
        print("|",end="")
        for j in range(8):
            string = nomePezzoInCasella(scacchiera[i][j])
            spazi = spazi_per_casella - len(string) -1      #1 spazio iniziale
            if j != 7:
                print(" "+string+" "*spazi+"|",end="")
            else:
                print(" "+string+" "*spazi+"|")
    print("---------------------------------------------------------")
    print("\n\n")

# TODO
# Se perdi tipo 3 pedoni e una regina -->  [3 pawn, 1 queen]
def print_pezzi_persi(pezzi_persi,color):
    g = color
    string = ""
    # per ogni pezzo ottieni la chiave tipo la stringa "my_name" --> conti con il dizionario e poi usi per stampare

# @return Ritorna +x se bianco in vantaggio di x, e duale     [#nota che deve avere la scacchiera NON i pezzi persi]
def vantaggio(scacchiera):
    sum = 0
    for i in range(8):
        for j in range(8):
            if scacchiera[i][j] != "empty":
                pezzo = scacchiera[i][j]
                #Per tutti i pezzi
                if pezzo.colore.upper() == "WHITE":
                    sum += valore_pezzo(pezzo)
                else:
                    sum -= valore_pezzo(pezzo)
    if sum == 0:
        return "Giocatori in parità"
    elif sum > 0:
        return f"White  +{sum}"
    else:
        return f"Black  +{sum}"



#Controlla che il nome dato da input sia quello del pezzo giusto    "P-->pawn"
def controlla_nome(piece,nome):
    if piece == "empty":                        #controllo prima altrimenti .my_name() runtime error
        return False

    if piece.my_name().upper() == nome.upper():
        return True
    else:
        return False

#controlla che il pezzo sia del giocatore
def controlla_giocatore(giocatore,pezzo):
    if giocatore.upper() != pezzo.my_name().upper():
        return False
    else:
        return True
    

def casella_vuota(scacchiera,pos):
    if scacchiera[pos[0]][pos[1]] == "empty":
        return True
    else:
        return False

    
# true se tutte le caselle  [(i,j),(i,j)...] vuote   
def caselle_vuote(scacchiera,caselle):
    for pos in caselle:
        if not casella_vuota(scacchiera,pos):
            return False
    return True

#valida se (i,j) sia i che j compresi tra 0 e 7
def casella_valida(pos):
    if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[0] <= 7:
        return True
    else:
        return False
    
def caselle_valide(caselle):
    for pos in caselle:
        if not casella_valida(pos):
            return False
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
        if casella_vuota(scacchiera,pos):
            dest.append(pos)
        else:
            pezzo = scacchiera[k][j]
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
        l = i+1 
        r = 8    
        passo = 1 
    else:                       #indietro   (i,j) --> (i,j-1..0)
        l = i-1
        r = -1 
        passo = -1 

    #mi muovo e mi fermo se incontro un pezzo, se nemico aggiungo la pos
    for k in range(l,r,passo):
        pos = (i,k)
        if casella_vuota(scacchiera,pos):
            dest.append(pos)
        else:
            pezzo = scacchiera[k][j]
            if case_controllate:            #se voglio case controllate dal pezzo aggiungo a prescindere
                dest.append(pos)
            if destinazioni  and pezzo_nemico(pezzo,giocatore):             #se voglio le destinazioni del pezzo solo se il pezzo è nemico
                dest.append(pos)
            break 
    return dest