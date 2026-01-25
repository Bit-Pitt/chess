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

'''     Regole da seguire       --> funzione da usare "caselle minacciate" da nemico
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