


from Servidor.ArbolBinarioBusqueda import ArbolBinarioBusqueda


arbol = ArbolBinarioBusqueda()

arbol.insertar(18)
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(4)
arbol.insertar(1)
arbol.insertar(8)
arbol.insertar(20)
arbol.insertar(19)
arbol.insertar(21)
arbol.insertar(22)

arbollista = arbol.ObtenerInorder(arbol.raiz);

print(arbollista)
arbollista = arbol.ObtenerInorder(arbol.raiz);

print(arbollista)
