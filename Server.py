import socket

class Servidor:
    def server_program():        
        print("inicio server program")
        host = "127.0.0.1"
        port = 5000  
        serverSocket = socket.socket()     
        serverSocket.bind((host, port)) 
        serverSocket.listen(3)
        conexiones, address = serverSocket.accept()  
        print("Conectado desde: " + str(address))
        while True:       
            data = conexiones.recv(1024).decode()
            if not data:
                break
            print("Cliente: " + str(data))
            data = input(' -> ')
            conexiones.send(data.encode()) 

        conexiones.close() 

    if __name__ == '__main__':
        server_program()