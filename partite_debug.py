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
             "P E2 E4" ,
             "P E7 E5" ,
            "Q D1 F3" ,
            "P A7 A6" ,
            "B F1 C4" ,
            "C B8 C6" ,
            "Q F3 F7" ,
      
            
        ],
    "2":[
         "P E7 E5" ,
            "Q D1 F3" ,
            "P A7 A6" ,
            "B F1 C4" ,
            "C B8 C6" ,
            "Q F3 F7" ,
      
        ],
    "3":[
            "P A2 A3", 
            "R A8 A3",
            "R h1 g1",
            "R a3 a1"
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


