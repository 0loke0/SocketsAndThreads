import socket

class Cliente:
    def client_program():
        print("inicio cliente program")
        host = "localhost"  
        port = 5000 
        client_socket = socket.socket()  
        client_socket.connect((host, port))  

        message = input(" -> ")  

        while True and message != "terminar" :
            client_socket.send(message.encode())  
            data = client_socket.recv(1024).decode()  
            print('Servidor: ' + data)  
            message = input(" -> ") 

        client_socket.close()  # close the connection


    if __name__ == '__main__':
        client_program()

        