class Triqui:
    def __init__(self, mapa):
        self.mapaTriqui = [ ["","",""],
                            ["","",""],
                            ["","",""]] if mapa == None else mapa

    # Recorrido
    # |1 |2 |3
    # |4 |5 |6
    # |7 |8 |9
    def ImprimirTablero (self):
        for mapaHorizontal  in self.mapaTriqui:
            for valor in mapaHorizontal:
                print("|",valor," ", end=" ")
            print("\n") #salto de linea
    
    def RealizarMovimiento(self,simboloJugador,cordenada):
        self.mapaTriqui[cordenada.x][cordenada.y] = simboloJugador
        self.ValidarGanador();
        return self.mapaTriqui;

    
    
    def ValidarGanador(self):
        self.jugadorX = 0;
        self.jugadorO = 0;

        cadenaOrdenada = [0,1,2]
        cadenaInvertida = [2,1,0]

        def sumarEnLinea(valor):
            if (valor == "X"):
                self.jugadorX += 1 
            if (valor == "O"):
                self.jugadorO += 1 
        
        def validarGanadorFinal():        
            if(self.jugadorX == 3):
                print("Has ganado jugador X")
            if(self.jugadorO == 3):
                print("Has ganado jugador O")
            else:
                self.jugadorX = 0;
                self.jugadorO = 0;

        #Horizontal
        for x in cadenaOrdenada:
            for y in cadenaOrdenada:
                valor = self.mapaTriqui[x][y]
                sumarEnLinea(valor)
            validarGanadorFinal()
        
        #Vertical 
        for y in cadenaOrdenada:
            for x in cadenaOrdenada:
                valor = self.mapaTriqui[x][y]
                sumarEnLinea(valor) 
            validarGanadorFinal()

        #Diagonal 
        for num in cadenaOrdenada:
            valor = self.mapaTriqui[num][num]
            sumarEnLinea(valor) 
        validarGanadorFinal()
        
        #Transversal 
        for num in cadenaInvertida:
            valor = self.mapaTriqui[num][num]
            sumarEnLinea(valor)
        validarGanadorFinal()

        

        
    