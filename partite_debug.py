# Partite per debug
# estension ==> crearle dinamicamente (randomicamente anche) e vedere se crasha qualcosa

# Dovresti creare una sorta di TEST_SUITE che utilizzi tutte queste partite di prova + random come dette sopra e controlla se il programma da errore

'''
            "",
            "",
            "",
            "",
            "",
            "",
'''
partite = {
    "attiva_in_debug":[
            "P D2 D4", 
            "P D7 D5",
            "b c1 h7",
            
        ],
    "2":[
            "P A2 A3", 
            "P B7 B5",
            "R A1 A2",
            "P A7 A5",
            "P B2 B4",
            "P A5 B4",
            "P A3 B4",
            "R  A8 A6",
            "K E1 D1",
            "R A6 A2",
            "P H2 H4",
        ],
    "3":[
            "P H2 H4",
        ],
    "arrocco_1":[                   #es arrocco corto
            "P A2 A3", 
            "P B7 B5", 
            " K e1 g1", 
    ],
    "arrocco_2":[                   #es arrocco non effettuabile
          [
          "P b2 b4",
          "p a7 a5",
          "p b4 a5",
          "r a8 a6",
          "r h1 g1",
          " r a6 b6",       
          " p d2 d3",
          "r b6 b2",
          "p d3 d4",
          "r b2 c2",        #IMPEDISCE ARROCCO
          "k e1 g1"     #non valida
        ]
             
    ]
}


