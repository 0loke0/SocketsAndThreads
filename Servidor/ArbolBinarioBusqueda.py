#Definir la clase para recorrer el arbol
from Servidor.Nodo import Nodo


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)


    def _insertar_recursivo(self, nodo, valor):
        #Caso base: si el nodo es none, creamos el nuevo nodo con el valor
        if nodo is None:
            return Nodo(valor)

        # si el valor s menor que el valor del nodo, isertamos a la izquierda
        if valor < nodo.valor:
            nodo.hijoIzquierda = self._insertar_recursivo(nodo.hijoIzquierda, valor)
        # Si el valor es mayor, insertamos a la derecha
        elif valor > nodo.valor:
            nodo.hijoDerecha = self._insertar_recursivo(nodo.hijoDerecha, valor)

        #Si el valor ya está en el arbol, no hacemos nada
        return nodo
    #Método que realiza el recorrido inorder (izquierda, raiz, derecha)
    contador = 0
    listaArbolInorden = []
    def ObtenerInorder(self, nodo):
        if nodo:
            #recorrer izquierda            
            self.ObtenerInorder(nodo.hijoIzquierda)
            #imprimir el valor del nodo donde estoy
            self.listaArbolInorden.append(nodo.valor)     
            self.ObtenerInorder(nodo.hijoDerecha)
        return self.listaArbolInorden
            

    def ObtenerHijosCompletos(self, nodo):       
         if nodo:
            if nodo.hijoIzquierda and nodo.hijoDerecha:
                print(nodo.valor, end=" ")
            self.ObtenerHijosCompletos(nodo.hijoIzquierda)        
            self.ObtenerHijosCompletos(nodo.hijoDerecha)

    def ObtenerHijosConPar(self, nodo):       
         if nodo:
            if (nodo.hijoIzquierda and nodo.hijoIzquierda.valor % 2 == 0) or (nodo.hijoDerecha and nodo.hijoDerecha.valor % 2 == 0) :
                print(nodo.valor, end=" ")                
            self.ObtenerHijosConPar(nodo.hijoIzquierda)        
            self.ObtenerHijosConPar(nodo.hijoDerecha)
    
    def ObtenerSumaHijos(self, nodo):      
         suma = 0 
         if nodo:            
            if nodo.hijoIzquierda : 
                suma = suma + nodo.hijoIzquierda.valor
            if nodo.hijoDerecha:
                suma = suma + nodo.hijoDerecha.valor
            print(suma, end=" ")                    
            self.ObtenerSumaHijos(nodo.hijoIzquierda)        
            self.ObtenerSumaHijos(nodo.hijoDerecha)

    pilaruta = []
    def ObtenerRutaNodo(self, nodo, valorbuscado):               
         if nodo: 
            self.pilaruta.append(nodo.valor) 
            if nodo.valor is valorbuscado:
                print(self.pilaruta);                                          
            self.ObtenerRutaNodo(nodo.hijoIzquierda,valorbuscado)        
            self.ObtenerRutaNodo(nodo.hijoDerecha,valorbuscado)
            self.pilaruta.pop()  