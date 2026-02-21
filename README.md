[TODO]
- en passant

Implementazione del gioco degli scacchi.


Estensioni:
- aggiungere un avversario BOT  -->  (fa ad es mosse casuali o ancora meglio crea un una funzione che valuta la "forza di una mossa")
    --> es se ti muovi in una zona controllata dal nemico (--), se dai scacco (++), se cattura vantaggiosa (++) ... euristiche
- aggiungi variazioni del gioco! (nouvi pezzi / mini-scacchiere / "carte magiche"... )




STRUTTURA E MODULARIZZAZIONE

Classi:
- pezzi:        [regola il comportamento specifico del pezzo]
    - pedone
    - torre
    - .... 

- scacchiera, riguarda un determinato tipo di scacchiera (standard:la classica)

- Game (incapsula la scacchiera e in generaile il "gioco")

- utils:
    - funzioni per il funzionamento del gioco, o logica in generale non strettamente correlata ad un pezzo o la scacchiera [potrebbero implementare una interfaccia]

- GUI: 
    - gestisce la gui

- main:  
    - creazione GUI e Game


Sequenza Vecchia:
- main :   (creazione scacchiera ... )
    - start_game  (si occupa del cambio turno, ottenere la mossa in input...)
        - muovi     (valida la mossa e la effettua, si avvale di "get_possible_destinations")
                ==> get_possible_destinations --> controlla logica scacchi, e sfrutta i metodi dei pezzi.


Sequenza Nuova:
Versione Interattiva:
- main :   (creazione Gui e Game)
    - la gui cattura le mosse e "invia" alla classe Game
Versione Debug:
- come la vecchia  [ogni partita salvata in "ultimo_game.txt" così da poter mettere in "partite_debug.py" e provarla] {ma non ha alcuni aggiornamenti}


Aspetti importanti notati:
- modularità del codice fondamentale
- indipendenza dei moduli
- incapsulamento in classi aiuta tantissimi la modularità
- tutto ciò che è "Hard-coded"  (es "WHITE" "BLACK", le celle della scacchiera tipo for i in range(8) ... ) non permetteranno eventuali 
    estensioni senza dover cambiare tutto il codice --> meglio che questi diventassero lo stato della scacchiera e poi si estendeva cambiano
    scacchiera (ovvero un altro oggetto della classe!)
