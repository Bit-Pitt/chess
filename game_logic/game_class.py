
from utils.graphic_utils import *
from utils.logic_utils import *



# Wrappato in una classe, indipendente ora utilizzabile dalla gui per un sistema Event-based
class Game:

    def __init__(self, scacchiera):
        self.scacchiera = scacchiera
        self.g1 = "White"
        self.g2 = "Black"
        self.turno = self.g1
        self.pezzi_persi_w = []
        self.pezzi_persi_b = []

        self.crea_file_partita()

    def crea_file_partita(self):
        with open("ultimo_game.txt", "w") as f:
            f.write(f'Ultima partita giocata.\n')

    def get_board(self):
        return self.scacchiera

    def processa_mossa(self, mossa_stringa):

        mossa = mossa_stringa.split()

        if len(mossa) != 3 or not controlla_input(mossa):
            print("Input non valido")
            return False

        nome = traduci_nome(mossa[0])
        csrc = stringTOpos(mossa[1])
        cdest = stringTOpos(mossa[2])

        pezzi_persi = (
            self.pezzi_persi_b if self.turno == self.g1
            else self.pezzi_persi_w
        )
        print(f"[DEBUG] parametri: {nome} {csrc} {cdest} {self.turno} {pezzi_persi} ")
        valid_move = self.muovi(
            self.scacchiera,
            nome,
            csrc,
            cdest,
            self.turno,
            pezzi_persi
        )

        if not valid_move:
            print("Mossa non valida")
            return False
        else:

            # salva su file
            with open("ultimo_game.txt", "a") as f:
                f.write(f' "{mossa_stringa}" ,\n')

            # cambio turno
            print("DEBUG: CAMBIO TURNO")
            self.turno = self.g2 if self.turno == self.g1 else self.g1

            self.scacchiera.print()     #per debug su terminale
            return True

    def check_fine_partita(self):
        res = partita_finita(self.scacchiera, self.turno)

        if res == 1:
            print("Patta")
            return True
        elif res == 2:
            g_NON_di_turno = self.g2 if self.turno == self.g1 else self.g1
            print("Vince:", g_NON_di_turno)
            return True

        return False
    
        # MOSSA VALIDA se la dest è una possibile destinazione
    # @input (es nome=P csrc=(1,0) cdest=(2,0))  {primo pedone A2 to A3}
    # @param scacchiera , nome pezzo, casella src, casella dest , pezzi_persi 
    # COSA FA: controlla se la mossa è valida e in tal caso la effettua             
    def muovi(self,scacchiera, nome, csrc, cdest,giocatore,pezzi_persi):
        pos = (csrc[0],csrc[1])
        piece = scacchiera.get_pezzo(pos)
        if not controlla_nome(piece,nome) or not controlla_giocatore(giocatore,piece):
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