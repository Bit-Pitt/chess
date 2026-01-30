from pezzi.pedone import Pedone
from pezzi.torre import Torre
from pezzi.re import Re
from pezzi.alfiere import Alfiere
from pezzi.cavallo import Cavallo
from pezzi.regina import Regina
from partite_debug import partite
from utils.graphic_utils import *
from utils.logic_utils import *
from scacchiera.chessboard import Scacchiera




# MOSSA VALIDA se la dest è una possibile destinazione
# @input (es nome=P csrc=(1,0) cdest=(2,0))  {primo pedone A2 to A3}
# @param scacchiera , nome pezzo, casella src, casella dest , pezzi_persi 
# COSA FA: controlla se la mossa è valida e in tal caso la effettua             
def muovi(scacchiera, nome, csrc, cdest,giocatore,pezzi_persi):
    pos = (csrc[0],csrc[1])
    piece = scacchiera.get_pezzo(pos)
    if not controlla_nome(piece,nome) or controlla_giocatore(giocatore,piece):
        return False
    
    # Qui avverranno tutti i controlli (scacco ... )
    possibili_dest = get_possible_destination(scacchiera,piece,csrc,giocatore)

    # La funzione restituisce:
    # - CASO GENERALE: lista di coppie (i,j) ovvero la posizione di destinazione del pezzo
    # - CASI SPECIALI:
    #       - "(i,j,"arrocco")", in tal caso si fa un controllo preventivo
    # Quindi prima controllo i casi particolari come arrocco / fine partita, altrimenti il caso generico in fondo

    
    #gestisco mosse speciali
    mosse_arrocco = trova_special_move(possibili_dest,"Arrocco")        #hai desso sai le (i,j) che sono in realtà degli arrocchi

    if cdest in mosse_arrocco:
        effettua_arrocco(scacchiera,cdest)
        return True

    # caso generico:  se la destinazione scelta dall'user "cdest" è nelle destinazioni del pezzo allora esegui (già fatti tutti i controlli necessari)
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
    partita_debug = partite["attiva_in_debug"]

    g1= "White"         #giocatori  
    g2 = "Black"
    g_di_turno = g1
    pezzi_persi_w,pezzi_persi_b = [] , []

    #ciclo di gioco
    while (True):
        print(g_di_turno+" turn")
        g_NON_di_turno = g2 if g_di_turno == g1 else g1
        pezzi_persi = pezzi_persi_b if g_di_turno == g1 else pezzi_persi_w      #es se turno del White allora può perderli il black

        #Controlla se partita finita
        res = partita_finita(scacchiera,g_di_turno)
        if res == 1:
            print("\n\n\n")
            print(f"Game ended for stalemate")
            print("\n\n\n")
            break
        elif res == 2:
            print("\n\n\n")
            print(f"Game ended, winner: {g_NON_di_turno}")
            print("\n\n\n")
            break

        #prova mossa
        valid_move = False
        while not valid_move:
            mossa = []
            
            if modalita == "due giocatori" or len(partita_debug) == 0:
                mossa = input("Immetti mossa: (es pedone da A2 a A3 -->  P A2 A3):  ")
                print("- per arrocco:  K [src] [dest]")
            if modalita == "DEBUG" and len(partita_debug) > 0:
                mossa = partita_debug[0]
                partita_debug.pop(0)
                if len(partita_debug) == 0:
                    print("Da adesso partita interattiva")
            
            
            mossa = mossa.split()
            if len(mossa) != 3 or not controlla_input(mossa):
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

        scacchiera.print()
        #print_pezzi_persi(pezzi_persi_w,"White")
        #print_pezzi_persi(pezzi_persi_b,"Black")
        print(vantaggio(scacchiera))



if __name__ == "__main__":
    print("Avvio partita")

    #Creazione schacchiera e pezzi
    scacchiera = Scacchiera()

    # es pedoni biani --> 2°riga in tutte le col quindi  [1,*]
    for i in range(8):
        pw = Pedone("white")
        pb = Pedone("black")
        scacchiera.aggiungi_pezzo(pw,(1,i))
        scacchiera.aggiungi_pezzo(pb,(6,i))
 
    scacchiera.aggiungi_pezzo(Torre("white"),(0,0))
    scacchiera.aggiungi_pezzo(Torre("white"),(0,7))
    scacchiera.aggiungi_pezzo(Torre("black"),(7,0))
    scacchiera.aggiungi_pezzo(Torre("black"),(7,7))

    scacchiera.aggiungi_pezzo(Re("white"),(0,4))
    scacchiera.aggiungi_pezzo(Re("black"),(7,4))

    scacchiera.aggiungi_pezzo(Alfiere("white"),(0,2))
    scacchiera.aggiungi_pezzo(Alfiere("white"),(0,5))
    scacchiera.aggiungi_pezzo(Alfiere("black"),(7,2))
    scacchiera.aggiungi_pezzo(Alfiere("black"),(7,5))

    scacchiera.aggiungi_pezzo(Cavallo("white"),(0,1))
    scacchiera.aggiungi_pezzo(Cavallo("white"),(0,6))
    scacchiera.aggiungi_pezzo(Cavallo("black"),(7,1))
    scacchiera.aggiungi_pezzo(Cavallo("black"),(7,6))

    scacchiera.aggiungi_pezzo(Regina("white"),(0,3))
    scacchiera.aggiungi_pezzo(Regina("black"),(7,3))

   
    scacchiera.print()

    start_game(scacchiera)
    print("Grazie per aver giocato")
