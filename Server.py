import pickle
import socket
import threading
from Servidor.ArbolBinarioBusqueda import ArbolBinarioBusqueda

arbol = ArbolBinarioBusqueda()

def OrdenarPorBurbuja(arr):
    n = len(arr)
    # Iterar a través de todos los elementos del array
    for i in range(n):
        # Last i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def nuevoCliente(conexiones,address):
    while True:        
        #Recepcion
        numeroEnteroRecibido = conexiones.recv(1024)
        numeroEnteroRecibidoDeserializado = pickle.loads(numeroEnteroRecibido)
        if numeroEnteroRecibido != None:
            arbol.insertar(int(numeroEnteroRecibidoDeserializado))      
            
        #Envio
        arbol.listaArbolInorden = []
        estructuraArbol = arbol.ObtenerInorder(arbol.raiz)
        OrdenarPorBurbuja(estructuraArbol)
        print(estructuraArbol)
        estructuraArbolSerializado = pickle.dumps(estructuraArbol)        
        conexiones.sendall(estructuraArbolSerializado) 
        
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



 