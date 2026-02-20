import tkinter as tk

import os

BASE_DIR = os.path.dirname(__file__)


H = 100
W = 100

# Canvas e root
root = tk.Tk()
canvas = tk.Canvas(root, width=W*8, height=H*8)
canvas.pack()

immagini = {
    "Pb": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "pawn_black.png")),
    "Pw": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "pawn_white.png")),
    "Rb": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "rook_black.png")),
    "Rw": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "rook_white.png")),
    "Kb": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "king_black.png")),
    "Kw": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "king_white.png")),
    "Bb": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "bishop_black.png")),
    "Bw": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "bishop_white.png")),
    "Cb": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "knight_black.png")),
    "Cw": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "knight_white.png")),
    "Qb": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "queen_black.png")),
    "Qw": tk.PhotoImage(file=os.path.join(BASE_DIR, "immagini_pezzi", "queen_white.png")),
}


# Funzione per disegnare la scacchiera
def disegna_scacchiera():
    for r in range(8):
        for c in range(8):
            color = "gray" if (r + c) % 2 == 0 else "white"
            canvas.create_rectangle(c*H, r*H, (c+1)*H, (r+1)*H, fill=color)

# Funzione per disegnare i pezzi
def disegna_pezzi():
    # Per ora mettiamo solo un pedone in 0,0 bianco e uno nero in 0,1
    canvas.create_image(
        0*H + W/2,      # centro della casella colonna 0
        7*H + W/2,      # centro della casella riga 0
        image=immagini["Kb"]
    )
    canvas.create_image(
        1*100 + 50,     # col 1  (centro)
        7*100 + 50,      # centro row 0
        image=immagini["Qw"]
    )

def evidenzia_casella(square):
    row, col = square
    # convertiamo row logica in row grafica
    r_graph = 7 - row

    canvas.create_rectangle(
        col*W, r_graph*H,
        (col+1)*W, (r_graph+1)*H,
        outline="red",
        width=4
    )


def aggiorna_gui(evidenzia_square=None):
    canvas.delete("all")
    disegna_scacchiera()
    if evidenzia_square != None:
        evidenzia_casella(evidenzia_square)
    disegna_pezzi()

# Funzione click
def click(event):
    col = event.x // W
    row = event.y // H
    row = 7 - row  # inverte righe
    print("Hai cliccato:", row, col)
    selected_square = (row, col)
    aggiorna_gui(evidenzia_square=selected_square)



# Bind click
canvas.bind("<Button-1>", click)

# Disegna tutto
disegna_scacchiera()
disegna_pezzi()

root.mainloop()

