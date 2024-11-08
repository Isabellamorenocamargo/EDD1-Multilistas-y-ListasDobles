### Santiago Eljach e Isabella Moreno
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    # Método para agregar nodos al final de la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    # Método para imprimir la lista
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()
    def ordenar(self):
        if not self.cabeza:
            return  # Lista vacía, no hay nada que ordenar

        intercambiado = True
        while intercambiado:
            intercambiado = False
            actual = self.cabeza
            while actual.siguiente:
                if actual.dato > actual.siguiente.dato:
                    # Intercambiamos los datos de los nodos
                    actual.dato, actual.siguiente.dato = actual.siguiente.dato, actual.dato
                    intercambiado = True
                actual = actual.siguiente
lista = ListaDoblementeEnlazada()
lista.agregar(4)
lista.agregar(2)
lista.agregar(5)
lista.agregar(1)
lista.agregar(3)

print("Lista antes de ordenar:")
lista.mostrar()

# Ordenamos la lista
lista.ordenar()

print("Lista después de ordenar:")
lista.mostrar()