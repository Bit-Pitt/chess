'''
    In questo file sono contenute le classi che rappresentano i vari pezzi
'''

#Classe generica (funge da "interfaccia" per descrivere il comportamento ovvero metodi in comune con le classi che la estendono)
class Pezzo:
    def __init__(self, nome, posizione,colore):
        self.nome = nome
        self.posizione = posizione
        self.colore = colore

    def sposta(self,scacchiera,casella_dest):
        return 0

    #   @return tutte le caselle controllate da quella posizione
    def campo_di_azione(self,scacchiera):
        return 0
    
    def nome(self):
        return "Piece"
        
class Pedone(Pezzo):
    def __init__(self, nome, posizione,colore):
        super().__init__(nome, posizione,colore)
        self.nome = "pawn"
        self.mai_mosso = True   #serve per poter giocare la prima mossa da due salti 

    def sposta(self,scacchiera,casella_dest):
        return 0

    def campo_di_azione(self,scacchiera):
        return 0
    
    def my_name(self):
            return "P"

