import threading
import Server 
import Cliente

hiloServidor = threading.Thread(Server.Servidor.server_program())
# hiloCliente = threading.Thread(Cliente.Cliente.client_program())

hiloServidor.start();
# hiloCliente.start();

