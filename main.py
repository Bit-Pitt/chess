from pezzi import *
from utils import * 
from partite_debug import *

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
# @param scacchiera , nome pezzo, casella src, casella dest , pezzi_persi 
# @return se la mossa è valida
def muovi(scacchiera, nome, csrc, cdest,giocatore,pezzi_persi):
    piece = scacchiera[csrc[0]][csrc[1]]
    if not controlla_nome(piece,nome) or controlla_giocatore(giocatore,piece):
        return False
    
    
    possibili_dest = get_possible_destination(scacchiera,piece,csrc,giocatore)
    #if possibili_dest == "end-game":
        

    if cdest in possibili_dest:
        pezzo_perso = piece.sposta(scacchiera,csrc,cdest)
        if pezzo_perso != "empty":
            pezzi_persi.append(pezzo_perso)
        return True
    else:
        return False


# Funzione un po troppo grossa
def start_game(scacchiera,modalita="due giocatori"):
    modalita="DEBUG"
    partita_debug = partite["1"]

    g1= "White"         #giocatori  
    g2 = "Black"
    g_di_turno = g1
    pezzi_persi_w,pezzi_persi_b = [] , []

    #ciclo di gioco
    while (True):
        print(g_di_turno+" turn")
    
        pezzi_persi = pezzi_persi_b if g_di_turno == g1 else pezzi_persi_w      #es se turno del White allora può perderli il black

        #prova mossa
        valid_move = False
        while not valid_move:
            mossa = []
            if modalita == "due giocatori":
                mossa = input("Immetti mossa: (es pedone da A2 a A3 -->  P A2 A3):  ")
            if modalita == "DEBUG":
                if len(partita_debug) == 0:
                    print("Partita simulata finita")
                    return 
                mossa = partita_debug[0]
                partita_debug.pop(0)
            mossa = mossa.split()
            if len(mossa) != 3:
                valid_move = False
            else:
                nome= traduci_nome(mossa[0])
                csrc = stringTOpos(mossa[1])   
                cdest = stringTOpos(mossa[2])             
                valid_move = muovi(scacchiera, nome, csrc, cdest, g_di_turno,pezzi_persi)
            
            if not valid_move:
                print("Mossa non valida,  mossa effettuata:"+str(mossa))

        #cambio turno
        g_di_turno = g2 if g_di_turno == g1 else g1

        print_scacchiera(scacchiera)
        #print_pezzi_persi(pezzi_persi_w,"White")
        #print_pezzi_persi(pezzi_persi_b,"Black")
        print(vantaggio(scacchiera))



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
