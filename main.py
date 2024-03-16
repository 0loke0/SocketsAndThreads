# import threading
# import Server 
# import Cliente
import Triqui
import Cordenadas
# hiloCliente = threading.Thread(Cliente.Cliente.client_program())

# hiloCliente.start();
mapa = [["X","O","O"],
        ["X","X","X"],
        ["7","8","9"]]
triqui = Triqui.Triqui(mapa);
triqui.ImprimirTablero();

cordenada = Cordenadas.Cordenada(2,2)
triqui.RealizarMovimiento("X",cordenada);
triqui.ImprimirTablero();