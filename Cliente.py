import pickle
import socket
import Movimiento
import Triqui

triqui = Triqui.Triqui();

def SolicitarMovimiento(simboloJugador):
    ingreso = input("Ingrese X y Y: Ejemplo '0 1' sin comillas => ")
    partes = ingreso.split()
    x = int(partes[0])
    y = int(partes[1])
    return Movimiento.Movimiento(x,y,simboloJugador)

print("inicio cliente program")
host = "localhost"  
port = 5000 
client_socket = socket.socket()  
client_socket.connect((host, port))  
 
while True:
    #Envio
    movimientoAEnviar = SolicitarMovimiento("O")        
    movimientoAEnviarSerializado = pickle.dumps(movimientoAEnviar)    
    client_socket.sendall(movimientoAEnviarSerializado)
    if(triqui.RealizarMovimiento(movimientoAEnviar)):
        break

    #Recepcion
    movimientoRecibido = client_socket.recv(1024)     
    if movimientoRecibido != None:
        movimientoRecibidoDeserializado = pickle.loads(movimientoRecibido)
        if(triqui.RealizarMovimiento(movimientoRecibidoDeserializado)):
            break   

client_socket.close()  # close the connection


    