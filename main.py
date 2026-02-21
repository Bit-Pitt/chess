from pezzi.pedone import Pedone
from pezzi.torre import Torre
from pezzi.re import Re
from pezzi.alfiere import Alfiere
from pezzi.cavallo import Cavallo
from pezzi.regina import Regina
from scacchiera.chessboard import Scacchiera
from game_logic.game_class import Game
from utils.graphic_utils import *
from utils.logic_utils import *
from game_no_gui_debug import partita_no_gui

#Per avviare il game in modalità debug
DEBUG = False

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

    if DEBUG:           #Se vuoi attivare la versione senza uso GUI [puoi usare il debug file..]
        partita_no_gui(scacchiera)
    else:
        partita = Game(scacchiera)      #creata la classe wrappata della logica di gioco
        #avvio GUI:        Lei crea il "while true" event based, sarà lei a chiamare l'evento alla scacchiera (in Game)
        gui = ChessGUI(partita)
        gui.run()

    

    print("Grazie per aver giocato")
