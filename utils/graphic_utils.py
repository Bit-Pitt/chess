#######################################################
###      Qui le funzioni riguardanti aspetti grafici   /  User interface
#######################################################






# @return Ritorna +x se bianco in vantaggio di x, e duale     [#nota che deve avere la scacchiera NON i pezzi persi]
def vantaggio(scacchiera):
    from .logic_utils import valore_pezzo
    sum = 0
    for i in range(8):
        for j in range(8):
            pezzo = scacchiera.get_pezzo((i,j))
            if pezzo != "empty":
                #print(f"Trovato pezzo in pos: ({i},{j}), colore {pezzo.colore.upper()} valore {valore_pezzo(pezzo)}")   #[DEBUG]
                if pezzo.colore.upper() == "WHITE":
                    sum += valore_pezzo(pezzo)
                else:
                    sum -= valore_pezzo(pezzo)
    if sum == 0:
        return "Giocatori in parità"
    elif sum > 0:
        return f"White  +{sum}"
    else:
        return f"Black  +{-sum}"


# converte pos in stringa to mat indexes   "B5-->[4][1]"
def stringTOpos(string):

    if len(string)!= 2:
        raise TypeError("Stringa da convertire non valida")
    
    col = ord(string[0].upper()) - ord('A') 
    row = int(string[1])-1
    return (row,col)

# "[4][1] --> B5"
def posTOstring(pos):
    if len(pos) != 2:
        raise TypeError("Posizione da convertire non valida")
    
    row, col = pos
    if row < 0 or col < 0:
        raise ValueError("Indici non validi")
    
    lettera = chr(col + ord('A'))
    numero = str(row + 1)
    
    return lettera + numero

    
    




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




# TODO
# Se perdi tipo 3 pedoni e una regina -->  [3 pawn, 1 queen]
def print_pezzi_persi(pezzi_persi,color):
    g = color
    string = ""
    # per ogni pezzo ottieni la chiave tipo la stringa "my_name" --> conti con il dizionario e poi usi per stampare

    

#Controlla che il nome dato da input sia quello del pezzo giusto    "P-->pawn"
def controlla_nome(piece,nome):
    if piece == "empty":                        #controllo prima altrimenti .my_name() runtime error
        return False

    if piece.my_name().upper() == nome.upper():
        return True
    else:
        return False
    
#controllo che il formato di input sia "nome" "csrc" "cdest" in particolare:
# csrc e cdest siano una lettera dell'alfabeto a-z o A-Z e una cifra
def controlla_input(mossa):
    csrc = mossa[1]
    cdest = mossa[2]
    if csrc[0].lower() < 'a' or csrc[0].lower() > 'z' or not csrc[1].isdigit():
        return False
    if cdest[0].lower() < 'a' or cdest[0].lower() > 'z' or not cdest[1].isdigit():
        return False
    return True
    