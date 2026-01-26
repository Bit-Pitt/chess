#######################################################
###      Qui le funzioni riguardanti aspetti grafici   /  User interface
#######################################################



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




# TODO
# Se perdi tipo 3 pedoni e una regina -->  [3 pawn, 1 queen]
def print_pezzi_persi(pezzi_persi,color):
    g = color
    string = ""
    # per ogni pezzo ottieni la chiave tipo la stringa "my_name" --> conti con il dizionario e poi usi per stampare

# @return Ritorna +x se bianco in vantaggio di x, e duale     [#nota che deve avere la scacchiera NON i pezzi persi]
def vantaggio(scacchiera):
    from .logic_utils import valore_pezzo
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
        return f"Black  +{-sum}"
    

#Controlla che il nome dato da input sia quello del pezzo giusto    "P-->pawn"
def controlla_nome(piece,nome):
    if piece == "empty":                        #controllo prima altrimenti .my_name() runtime error
        return False

    if piece.my_name().upper() == nome.upper():
        return True
    else:
        return False