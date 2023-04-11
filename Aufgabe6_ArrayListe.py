import random


class ArrayList:
    def __init__(self):
        self.array = []
        self.first = None
        self.last = None

    def append(self, data):
        self.array.append(data)

    def length(self):
        return len(self.array)

    def print_all(self):
        for i in self.array:
            print(i)

    def get_by_index(self, index):
        return self.array[index]

    def insert_at_index(self, index, data):
        self.array[index] = data

    def remove(self, index):
        self.array.pop(index)

if __name__ == "__main__":
        list = ArrayList()
        for i in range(random.randint(5, 10)):
            list.append(random.randint(1, 100))
        print(list.length())
        list.print_all()
        print("---------------------------")
        list.insert_at_index(4, 20)
        list.print_all()
        print("----------------------")
        list.remove(2)
        list.print_all()
        print("----------------------------")