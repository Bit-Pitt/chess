
# Classe per la scacchiera classica
class Scacchiera:
    def __init__(self):
        self._scacchiera = self.crea_scacchiera_vuota()


    def crea_scacchiera_vuota(self):
        grid = []
        for i in range(8):
            grid.append(list())
            for _ in range(8):
                grid[i].append("empty") 
        return grid
    
    #valida se (i,j) sia i che j compresi tra 0 e 7
    def casella_valida(self,pos):
        if len(pos) != 2:
            raise Exception("Chiamato API a scacchiera con formato pos errato")
        if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
            return True
        else:
            return False
    
    def aggiungi_pezzo(self,pezzo,pos):
        if len(pos) != 2:
            raise Exception("Chiamato API a scacchiera con formato pos errato")
        if self.casella_valida(pos):
            self._scacchiera[pos[0]][pos[1]] = pezzo


    # 8 spazi per casella es    | pb     | empty  |  ....  
    # Stampo righe in reverse per aver effetto scacchiera classica
    def print(self):
        print("\n\n")
        spazi_per_casella = 6
        for i in range(7,-1,-1):                    #7 6 .. 1 0
            print("---------------------------------------------------------")
            print("|",end="")
            for j in range(8):
                string = self.nomePezzoInCasella(self._scacchiera[i][j])
                spazi = spazi_per_casella - len(string) -1      #1 spazio iniziale
                if j != 7:
                    print(" "+string+" "*spazi+"|",end="")
                else:
                    print(" "+string+" "*spazi+"|")
        print("---------------------------------------------------------")
        print("\n\n")


    def nomePezzoInCasella(self,pezzo):
        if pezzo == "empty":
            return ""
        else:
            return pezzo.print_my_name()
        
    def get_pezzo(self,pos):
        if not isinstance(pos, tuple) or not all(isinstance(x, int) for x in pos) or len(pos) != 2:
            raise Exception("Chiamato API a scacchiera con formato pos errato [API: get_pezzo]")
        
        piece = self._scacchiera[pos[0]][pos[1]]
        return piece


    def casella_vuota(self,pos):
        #if not isinstance(pos, tuple) or not all(isinstance(x, int) for x in pos) or len(pos) != 2 or self.casella_valida(pos):
            #raise Exception("Chiamato API a scacchiera con formato pos errato [API: get_pezzo]")
        if self._scacchiera[pos[0]][pos[1]] == "empty":
            return True
        else:
            return False

        
    # true se tutte le caselle  [(i,j),(i,j)...] vuote   
    def caselle_vuote(self,caselle):
        for pos in caselle:
            if not self.casella_vuota(pos):
                return False
        return True


        
    def caselle_valide(self,caselle):
        for pos in caselle:
            if not self.casella_valida(pos):
                return False
        return True
    
    # @return pos (i,j) del re di quel giocatore
    def get_pos_re(self,giocatore):
        for i in range(8):
            for j in range(8):
                pezzo = self.get_pezzo((i,j))
                if pezzo != "empty" and pezzo.my_name() == "King" and pezzo.colore.upper() == giocatore.upper():
                    return (i,j)
        raise Exception("Re non trovato ?!")
      