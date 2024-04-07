import pickle
import socket

arrayOrdenamiento = []

def SolicitarNumeroEntero():
    ingreso = input("Ingrese un numero entero \n")    
    return ingreso

print("inicio cliente program")
host = "localhost"  
port = 5000 
client_socket = socket.socket()  
client_socket.connect((host, port))  
 
while True:
    #Envio
    numeroEntero = SolicitarNumeroEntero()        
    numeroEnteroSerializado = pickle.dumps(int(numeroEntero))   
    client_socket.sendall(numeroEnteroSerializado)
    
    #Recepcion
    arbolOrdenado = client_socket.recv(1024)
    arbolOrdenadoDeserializado = pickle.loads(arbolOrdenado)
    print("Array ordenado")
    print(arbolOrdenadoDeserializado)
   

client_socket.close()  # close the connection


    