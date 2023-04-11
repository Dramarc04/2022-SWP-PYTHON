import random


class Element:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.array = []
        self.first = None
        self.last = None

    def append(self, data):
        new_element = Element(data)
        if not isinstance(data, int):
            raise ValueError("Data must be an integer")
        if self.first is None:
            self.first = new_element
            self.last = new_element
            self.array.append(new_element)
        else:
            self.last.next = new_element
            new_element.prev = self.last
            self.last = new_element
            self.array.append(new_element)

    def length(self):
        return len(self.array)

    def print_all(self):
        curr_element = self.first
        while curr_element:
            print(curr_element.data)
            curr_element = curr_element.next

    def get_element_by_index(self, index):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        return self.array[index]

    def insert(self, index, data):
        if not isinstance(data, int):
            raise ValueError("Data must be an integer")
        new_element = Element(data)
        if index == len(self.array):
            self.append(data)
        else:
            element_at_index = self.get_element_by_index(index)
            if element_at_index.prev:
                element_at_index.prev.next = new_element
            else:
                self.first = new_element
            new_element.prev = element_at_index.prev
            new_element.next = element_at_index
            element_at_index.prev = new_element
            self.array.insert(index, new_element)

    def remove(self, index):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of range")
        element_to_remove = self.get_element_by_index(index)
        if element_to_remove.prev:
            element_to_remove.prev.next = element_to_remove.next
        else:
            self.first = element_to_remove.next
        if element_to_remove.next:
            element_to_remove.next.prev = element_to_remove.prev
        else:
            self.first = element_to_remove.prev
        self.array.pop(index)


if __name__ == "__main__":
    list = DoubleLinkedList()
    for i in range(random.randint(5,10)):
        list.append(random.randint(1,100))
    print(list.length())
    list.print_all()
    print("---------------------------")
    list.insert(4,20)
    list.print_all()
    print("----------------------")
    list.remove(2)
    list.print_all()
    print("----------------------------")
