#Implementa una clase Stack y una clase Queue con listas de Python.

class Stack:
    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def push(self, item):
        """Añade un elemento a la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento superior de la pila."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Devuelve el elemento superior de la pila sin eliminarlo."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        """Devuelve el número de elementos en la pila."""
        return len(self.items)

class Queue:
    def __init__(self):
        """Inicializa una cola vacía."""
        self.items = []

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Añade un elemento al final de la cola."""
        self.items.append(item)

    def dequeue(self):
        """Elimina y devuelve el primer elemento de la cola."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Devuelve el primer elemento de la cola sin eliminarlo."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

    def size(self):
        """Devuelve el número de elementos en la cola."""
        return len(self.items)
    
# mistack = Stack()
# mistack.push(1)
# mistack.push(2)
# mistack.push(3)
# print("Pila:", mistack.items)
# print("Elemento superior:", mistack.peek()) 
# print("Tamaño de la pila:", mistack.size())
# print("Elemento eliminado de la pila:", mistack.pop())
# print("Pila después de eliminar un elemento:", mistack.items)
miqueue = Queue()
miqueue.enqueue(1)  
miqueue.enqueue(2)
miqueue.enqueue(3)
print("Cola:", miqueue.items)
print("Primer elemento de la cola:", miqueue.peek())
print("Tamaño de la cola:", miqueue.size())
print("Elemento eliminado de la cola:", miqueue.dequeue())
print("Cola después de eliminar un elemento:", miqueue.items)
