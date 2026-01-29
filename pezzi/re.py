from utils.logic_utils import *
from .pezzo import Pezzo

DEBUG = False

class Re(Pezzo):
    def __init__(self,colore):
        super().__init__(colore)
        self.nome = "King"
        self.mai_mosso = True   #per possibile arrocco

    def sposta(self,scacchiera,csrc,cdest):
        super().sposta(scacchiera,csrc,cdest)  
        self.mai_mosso = False
    

    # Possibili destinazioni re:
    # - 1) tutte le direzioni ma una casella di passo
    # - 2) Non devono essere controllate da altri pezzi nemici!    
    # - 3) arrocco   
    # @return tutte le destinazioni possibili (i,j)
    def destinations(self, scacchiera, csrc, giocatore):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "King":
            raise TypeError("[Internal error] Non è presente il re nella casella!")
        dest = []

        #1)
        dest = movimento_re(scacchiera,csrc,destinazioni=True)
        #2)
        avversario = nome_avversario(giocatore)
        controllate_da_avversario = case_controllate_da_giocatore(scacchiera,
                                                                    avversario,     
                                                                    togli_re=True,          # [*]
                                                                    colore_re=giocatore)  
        # Quei due parametri perchè avremo le case controllate dall'avversario ma come se nella scacchiera non ci fosse il re questo perchè:
        # se abbiamo tipo la torre che da scacco al re dalla stessa riga, allora non risulta che questa torre controlla tutta la riga perchè per l'appunto
        # c'è il re (questo per come creata la funzione "case controllate" dei pezzi), quindi così facendo daremo la possibilità al re di spostarsi lungo la riga
        # in direzione opposta alla torre ma non lo vogliamo, risolto grazie a questi due parametri!

        dest = [ pos for pos in dest if pos not in controllate_da_avversario]

        #3)   funzione apposita
        dest.extend(self.arrocco(scacchiera,csrc,giocatore,controllate_da_avversario))


        if DEBUG:
            DEBUG_print_caselle(dest,"destinazioni possibili del re:")
        
        return dest
    

    def case_controllate(self, scacchiera, csrc, giocatore=""):
        pos = (csrc[0],csrc[1])
        pezzo = scacchiera.get_pezzo(pos)
        if pezzo.my_name() != "King":
            raise TypeError("[Internal error] Non è presente un re nella casella!")
        pos_controllate = []

        pos_controllate += movimento_re(scacchiera,csrc,case_controllate=True)

        if DEBUG:
            DEBUG_print_caselle(pos_controllate,"case controllate dal re:")

        return pos_controllate
    
    def my_name(self):
        return self.nome
    
    def print_my_name(self):
        c = self.colore[0]
        return "K"+c

    #se ha la variabile "mai_mosso"
    def has_mai_mosso(self):
        return True
    
    # "contr_avv" case controllate dall'avversario
    #Ritorna la destinazione per il re (i,j,"arrocco") se può arroccare   [es arrocco corto bianco ritorna --> (cord(g1),"Arrocco")]   
    # Quando può arroccare:
    # re , torre mai mossi, caselle vuote tra loro, caselle dove il re passa non controllate (compresa la sua attuale!)
    def arrocco(self,scacchiera,csrc,giocatore,contr_avv):
        #controlla  i due arrocchi per nero e bianco se re mai mosso, torre mai mossa, se case dove si muove il re NON controllate da nemico
        dests = []
        if giocatore.upper() == "WHITE":
            pos_sua = (0,4)  
            t1_corto = scacchiera.get_pezzo((0,7))          #torre dell'arrocco corto, controllo dopo se è davvero lei

            if t1_corto != "empty" and t1_corto.my_name() == "Rook" and self.mai_mosso and t1_corto.mai_mosso:
                #se entrambi mai mossi controllo se le case tra i due pezzi vuote e case di movimento del re dell'arrocco corto: (0,5)(0,6)e pos sua

                pos1 = (0,5)
                pos2 = (0,6)
                if  scacchiera.caselle_vuote([pos1,pos2]) and pos1 not in contr_avv and pos2 not in contr_avv and pos_sua not in contr_avv:
                    dests.append((0,6,"Arrocco"))  

            t2_lungo =  scacchiera.get_pezzo((0,0)) 
            if  t2_lungo != "empty" and t2_lungo.my_name() == "Rook" and self.mai_mosso and t2_lungo.mai_mosso:
                pos1 = (0,2)
                pos2 = (0,3)
                if scacchiera.caselle_vuote([(0,1),pos1,pos2]) and pos1 not in contr_avv and pos2 not in contr_avv and pos_sua not in contr_avv:
                    dests.append((0,2,"Arrocco"))  
        else:        
            pos_sua = (7,4)                                   #analogo per il nero
            t1_corto = scacchiera.get_pezzo((7,7))          

            if t1_corto != "empty" and t1_corto.my_name() == "Rook" and self.mai_mosso and t1_corto.mai_mosso:
                pos1 = (7,5)
                pos2 = (7,6)
                if scacchiera.caselle_vuote([pos1,pos2]) and pos1 not in contr_avv and pos2 not in contr_avv and pos_sua not in contr_avv:
                    dests.append((7,6,"Arrocco"))  

            t2_lungo =  scacchiera.get_pezzo((7,0)) 
            if  t2_lungo != "empty" and t2_lungo.my_name() == "Rook" and self.mai_mosso and t2_lungo.mai_mosso:
                pos1 = (7,2)
                pos2 = (7,3)
                if scacchiera.caselle_vuote([(7,1),pos1,pos2]) and pos1 not in contr_avv and pos2 not in contr_avv and pos_sua not in contr_avv:
                    dests.append((7,2,"Arrocco"))  

        return  dests