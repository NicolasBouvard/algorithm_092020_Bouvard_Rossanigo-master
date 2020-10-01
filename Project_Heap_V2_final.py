class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def __init__(self, value):
        self.value = value

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        if type(value) != int:
            raise Exception("Incorrect type value, please enter an integer")
        self.value.append(value)
        Heap.move_down(self.value, 0, len(self.value) - 1)
        print(self.value)

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        minimum = self.value[0]
        for value in self.value:
            if value < minimum:
                minimum = value
        return minimum

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        minimum = Heap.find_min(self)
        self.value.remove(min)
        return minimum

    def decrease_key(self, current_value: int, new_value: int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        if (type(current_value) or type(new_value)) != int:
            raise Exception("Incorrect type value, please enter an integer")
        for i in range(0, len(self.value)):
            if self.value[i] == current_value:
                self.value[i] = new_value

    def merge(self, heap) -> None:
        """
        Fusionne deux arbres
        """
        for i in range(0, len(heap.value)):
            Heap.insert(self, heap.value[i])

    def move_down(self, start_position, current_position):
        if (type(start_position) or type(current_position)) != int:
            raise Exception("Incorrect type value, please enter an integer")
        newitem = self[current_position]
        while current_position > start_position:
            parentpos = (current_position - 1) >> 1
            parent = self[parentpos]
            if newitem < parent:
                self[current_position] = parent
                current_position = parentpos
                continue
            break
        self[current_position] = newitem


class Trees:
    def __init__(self, value):
        self.order = 0
        self.value = value
        self.children = []


class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement

    https://en.wikipedia.org/wiki/Fibonacci_heap

    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """

    def __init__(self):
        self.trees = []
        self.min = None
        self.count = 0

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        if type(value) != 'int':
            raise Exception("Incorrect type value, please enter an integer")
        tree = Trees(value)
        self.trees.append(tree)
        if value < self.min.value or self.min is None:
            self.min = tree
        self.count = self.count + 1

    def find_min(self) -> int or None:
        """
        Retourne la valeur minimum dans l'arbre
        """
        if self.min is None:
            return None
        else:
            return self.min.value

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        minimum = FibonacciHeap.find_min(self)
        self.value.remove(minimum)
        return minimum

    def merge(self, fibonnaci_heap) -> None:
        """
        Fusionne deux arbres
        """
        if type(fibonnaci_heap) != Heap:
            raise Exception("Incorrect type value, please enter an Heap object")
        if FibonacciHeap.find_min(self) < FibonacciHeap.find_min(fibonnaci_heap):
            for i in range(0, len(fibonnaci_heap.value)):
                FibonacciHeap.insert(self, fibonnaci_heap[i])
        else:
            for i in range(0, len(self.value)):
                FibonacciHeap.insert(fibonnaci_heap, self[i])
