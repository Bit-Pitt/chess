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