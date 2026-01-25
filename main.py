from pezzi import *
from utils import * 

#Crea scacchiera vuota   (lista di liste "matrice")
def crea_scacchiera():
    grid = []
    for i in range(8):
        grid.append(list())
        for _ in range(8):
            grid[i].append("empty") 
    return grid




# La funzione se la mossa è valida cambia effettivamente la scacchiera   [in esteso sotto]
# @input (es nome=P csrc=(1,0) cdest=(2,0))  {primo pedone A2 to A3}
# @param scacchiera , nome pezzo, casella src, casella dest
# @return se la mossa è valida
def muovi(scacchiera, nome, csrc, cdest,giocatore):
    piece = scacchiera[csrc[0]][csrc[1]]
    if not controlla_nome(piece,nome) or controlla_giocatore(giocatore,piece):
        return False
    
    possibili_dest = piece.destinations(scacchiera,csrc,giocatore)

    if cdest in possibili_dest:
        piece.sposta(scacchiera,csrc,cdest)
        return True
    else:
        return False

'''     Regole da seguire
# se mossa valida ovvero:
    # - la casella è raggiungibile  [fatti tornare dalla classe lista di coppie (i,j)]
    # - se non passa attraverso altri pezzi (eccez cavallo)
    # - se non è inchiodato!  {controllo preventivo da aggiungere a tutti}

    #altri casi:  per il re se quella casella è già minacciata
    # mosse speciali (arrocco /  en-passant)
    # o se sono sotto scacco
    # promozione pedone

    #in tal caso
    # muovi pezzo (libera casella di partenza! "==empty"), occupa la nuova ==>se catturi un pezzo stampa tipo che è stato perso il pezzo ..
'''


def start_game(scacchiera):

    g1= "White"         #giocatori  
    g2 = "Black"
    g_di_turno = g1

    #ciclo di gioco
    while (True):
        print(g_di_turno+" turn")

        #prova mossa
        valid_move = False
        while not valid_move:
            mossa = input("Immetti mossa: (es pedone da A2 a A3 -->  P A2 A3):  ")
            mossa = mossa.split()
            if len(mossa) != 3:
                valid_move = False
            else:
                nome= traduci_nome(mossa[0])
                csrc = stringTOpos(mossa[1])   
                cdest = stringTOpos(mossa[2])             
                valid_move = muovi(scacchiera, nome, csrc, cdest, g_di_turno)
            
            if not valid_move:
                print("Mossa non valida,  mossa effettuata:"+str(mossa))

        #cambio turno
        if g_di_turno == g1:
            g_di_turno = g2 
        else:
            g_di_turno = g1

        print_scacchiera(scacchiera)



if __name__ == "__main__":
    print("Avvio partita")

    #Creazione schacchiera e pezzi
    scacchiera = crea_scacchiera()

    #pedoni biani --> 2°riga in tutte le col quindi  [1,*]
    for i in range(8):
        pw = Pedone("white")
        pb = Pedone("black")
        scacchiera[1][i] = pw 
        scacchiera[6][i] = pb

    print_scacchiera(scacchiera)

    start_game(scacchiera)
