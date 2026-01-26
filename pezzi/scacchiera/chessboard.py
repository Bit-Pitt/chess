

class Scacchiera:
    def __init__(self):
        self.scacchiera = self.crea_scacchiera_vuota()


    def crea_scacchiera_vuota(self):
        grid = []
        for i in range(8):
            grid.append(list())
            for _ in range(8):
                grid[i].append("empty") 
        return grid