#######################################################
###      Qui le funzioni riguardanti aspetti grafici   /  User interface
#######################################################

'''     GUI FUNZIONAMENTO IN BREVE
    -   l'utente clicca due caselle ==> si crea la mossa che "invio" alla partita tramite il metodo predefinito
'''
import tkinter as tk
import os 


BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # risale di 1 livello



class ChessGUI:

    def __init__(self, partita):

        # dimensioni caselle
        self.H = 100
        self.W = 100

        self.partita = partita

        self.mossa = []         #Quando si hanno due caselle allora è pronta per essere eseguita

        # finestra
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=self.W*8, height=self.H*8)
        self.canvas.pack()

        self.immagini = self.crea_immagini() 

        # bind click
        self.canvas.bind("<Button-1>", self.click)

        # primo disegno
        self.aggiorna_gui()


    # AVVIO
    def run(self):
        self.root.mainloop()


    def termina_gui(self):
        print("Chiudo la GUI")
        self.root.destroy()


    # DISEGNO SCACCHIERA
    def disegna_scacchiera(self):
        for r in range(8):
            for c in range(8):
                color = "gray" if (r + c) % 2 == 0 else "white"
                self.canvas.create_rectangle(
                    c*self.W, r*self.H,
                    (c+1)*self.W, (r+1)*self.H,
                    fill=color
                )

    # Es:  (0,0) converti nel SI grafico (7,0) --> trovi il centro di quello square: 
    #  # Per ora mettiamo solo un pedone in 0,0 bianco e uno nero in 0,1
    #  canvas.create_image(
    #    0*H + W/2,      # centro della casella colonna 0 --> questa è la x  (perchè Sistema di coordinate è  1) --> x   2) in giù y)
    #    7*H + W/2,      # centro della casella riga 0
    def converti_pos_pixel(self, pos):
        """
        pos: (row, col) logico (0,0 in basso a sinistra)
        ritorna: (x_pixel, y_pixel) del centro della casella
        """
        row, col = pos
        # Invertiamo la riga perché nel canvas 0 è in alto
        row_graph = 7 - row

        # centro della casella
        x = col * self.W + self.W / 2
        y = row_graph * self.H + self.H / 2

        return x, y

    # DISEGNO PEZZI 
    def disegna_pezzi(self):
        scacchiera = self.partita.get_board()
        
        for r in range(8):
            for c in range(8):
                pos = (r,c)
                piece = scacchiera.get_pezzo(pos)
                if piece != "empty":
                    x,y = self.converti_pos_pixel(pos)
                    self.canvas.create_image(
                        x,      # centro della casella Coordinata colonna 
                        y,      # centro della casella Coordinata riga 
                        image=self.immagini[piece.print_my_name().upper()]
                    )
             

 
    # EVIDENZIA     (la casella selezionata)
    def evidenzia_casella(self, square):

        row, col = square
        r_graph = 7 - row

        self.canvas.create_rectangle(
            col*self.W, r_graph*self.H,
            (col+1)*self.W, (r_graph+1)*self.H,
            outline="red",
            width=4
        )

    # AGGIORNA GUI
    def aggiorna_gui(self):

        self.canvas.delete("all")
        self.disegna_scacchiera()

        for pos in self.mossa:
            self.evidenzia_casella(pos)

        self.disegna_pezzi()

    # CLICK EVENT
    def click(self, event):

        col = event.x // self.W
        row = event.y // self.H
        row = 7 - row

        print("Hai cliccato:", row, col)
        selected_square = (row, col)
        self.mossa.append(selected_square)
        
        #controlla eventuale fine partita (metodo già creato)
        # print terminale della scacchiera per debug
        if len(self.mossa) == 2:
            # crea la mossa nel formato usato fino ad ora es "P A2 A3" 
            stringa_mossa = crea_stringa(self.mossa,self.partita.get_board())
            # "inviala" alla scacchiera
            res = self.partita.processa_mossa(stringa_mossa)
            
            #Controllo se c'è una promozione
            if len(res)>1:
                print("PROMOZIONE AUTOMATICA A REGINA:")
                # ... aggiungi gui
                self.partita.promuovi("Queen")
                self.partita.get_board().print()
            self.mossa = []
        
        self.aggiorna_gui()

        res = self.partita.check_fine_partita()
        if res[0]:
            self.root.after(300, self.mostra_fine_partita(res[1]))
        

    def mostra_fine_partita(self,vincitore):
        self.canvas.create_rectangle(
            0, 0, self.W*8, self.H*8,
            fill="black",
            stipple="gray50"
        )
        stringa_output=""
        if vincitore.upper() == "WHITE":
            stringa_output = "Vincitore: Player White"
        elif vincitore.upper() == "BLACK":
            stringa_output = "Vincitore: Player Black"
        else:
            stringa_output = "Partita finita in patta"

        self.canvas.create_text(
            self.W*4,
            self.H*4,
            text=stringa_output,
            fill="white",
            font=("Arial", 40, "bold")
        )


    def crea_immagini(self):
        immagini = {
        "PB": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "pawn_black.png")),
        "PW": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "pawn_white.png")),
        "RB": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "rook_black.png")),
        "RW": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "rook_white.png")),
        "KB": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "king_black.png")),
        "KW": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "king_white.png")),
        "BB": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "bishop_black.png")),
        "BW": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "bishop_white.png")),
        "CB": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "knight_black.png")),
        "CW": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "knight_white.png")),
        "QB": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "queen_black.png")),
        "QW": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "queen_white.png")),
        }
        return immagini



####################################  Adesso utils "grafiche" più legate alla logica "user"

# Serve per creare la stringa nel formato richiesto da input es se pedone restituisce "P".
def get_iniziale(pezzo):
    if pezzo == "empty":
        return "e"          #invaliderà la mossa dopo
    nome = pezzo.print_my_name()                
    return nome[0]


# @param mossa: Es  [(1,0) , (2,0)]
# La converto in [P A1 A2] se effettivamente lì ce il pedone
def crea_stringa(mossa,scacchiera):
    csrc = mossa[0]
    cdest = mossa[1]
    string_csrc = posTOstring(csrc)
    string_dest = posTOstring(cdest)
    pezzo = scacchiera.get_pezzo(csrc)
    iniziale = get_iniziale(pezzo)

    stringa = f"{iniziale} {string_csrc} {string_dest}"
    print(f"[DEBUG] {stringa}")
    return stringa


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
        error_string = f"Posizione da convertire non valida: {pos}"
        raise Exception(error_string)
    
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
    
#controllo che il formato di input sia "lettera" "csrc" "cdest" in particolare:
# csrc e cdest siano una lettera dell'alfabeto a-z o A-Z e una cifra
# lettera sia una che raffigura un pezzo degli scacchi (P,...)
def controlla_input(mossa):
    csrc = mossa[1]
    cdest = mossa[2]
    if csrc[0].lower() < 'a' or csrc[0].lower() > 'z' or not csrc[1].isdigit():
        return False
    if cdest[0].lower() < 'a' or cdest[0].lower() > 'z' or not cdest[1].isdigit():
        return False
    iniziali_pezzi = ("P","K","C","Q","B","R")

    if mossa[0].upper() not in iniziali_pezzi:
        return False

    return True
    

