[TODO]:
- start_game (logica di fine partita)   "partita_finita()"
- get_possible_destination: (logica per via degli scacchi, pin ...)

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

- utils:
    - funzioni per il funzionamento del gioco, o logica in generale non strettamente correlata ad un pezzo o la scacchiera [potrebbero implementare una interfaccia]

- main:  
    - funzioni di struttura generale del flow della partita


Sequenza:
- main :   (creazione scacchiera ... )
    - start_game  (si occupa del cambio turno, ottenere la mossa in input...)
        - muovi     (valida la mossa e la effettua, si avvale di "get_possible_destinations")
                ==> get_possible_destinations --> controlla logica scacchi, e sfrutta i metodi dei pezzi.


