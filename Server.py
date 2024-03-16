import socket
import threading


def nuevoCliente(conexiones,address):
    while True:
        print("Conectado desde: " + str(address))
        data = conexiones.recv(1024).decode()
        if not data:
            break
        print("Cliente: " + str(data))
        data = input(' -> ')
        conexiones.send(data.encode()) 
    conexiones.close()
   
print("inicio server program")
host = "0.0.0.0"
port = 5000  
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
serverSocket.bind((host, port)) 
serverSocket.listen(5)
conexiones, address = serverSocket.accept()  
print("Conectado desde: " + str(address))
while True:       
        threading.Thread(nuevoCliente(conexiones,address)).start();

 