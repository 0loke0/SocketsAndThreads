import pickle
import socket
import threading
import Movimiento
import Triqui

triqui = Triqui.Triqui();

def SolicitarMovimiento(simboloJugador):
    ingreso = input("Ingrese X y Y: Ejemplo '0 1' sin comillas => ")
    partes = ingreso.split()
    x = int(partes[0])
    y = int(partes[1])
    return Movimiento.Movimiento(x,y,simboloJugador)

def nuevoCliente(conexiones,address):
    while True:        
        #Recepcion
        movimientoRecibido = conexiones.recv(1024)
        if movimientoRecibido != None:
            movimientoRecibidoDeserializado = pickle.loads(movimientoRecibido)
            if(triqui.RealizarMovimiento(movimientoRecibidoDeserializado)):
                break        

        #Envio
        movimientoAEnviar = SolicitarMovimiento("X");
        movimientoAEnviarSerializado = pickle.dumps(movimientoAEnviar)        
        conexiones.sendall(movimientoAEnviarSerializado) 
        if(triqui.RealizarMovimiento(movimientoAEnviar)):
            break
    conexiones.close()
   
print("inicio server program")
host = "0.0.0.0"
port = 5000  
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
serverSocket.bind((host, port)) 
serverSocket.listen(5)
while True: 
    conexiones, address = serverSocket.accept()        
    threading.Thread(nuevoCliente(conexiones,address)).start();



 