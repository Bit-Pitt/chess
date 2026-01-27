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



