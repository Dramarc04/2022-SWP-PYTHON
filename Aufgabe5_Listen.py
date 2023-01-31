import random


class EinfacheVerketteteListe():
    def __init__(self):
        self.startElement = Element("Header")

    def get_last_ele(self):
        pointerElem = self.startElement
        while pointerElem.nextElem is not None:
            pointerElem = pointerElem.get_next_elem()
        return pointerElem

    def append_new_elem(self, newElem):
        last_ele = self.get_last_ele()
        last_ele.set_next_elem(newElem)

    def print_elems(self):
        pointerElem = self.startElement
        while pointerElem.nextElem is not None:
            pointerElem = pointerElem.get_next_elem()
            print(pointerElem.content)

    def get_length(self):
        pointerElem = self.startElement
        count = 0
        while pointerElem is not None:
            count += 1
            pointerElem = pointerElem.get_next_elem()
        return count-1

    def get_ele_index(self, index):
        pointerElem = self.startElement
        current_index = 0
        while current_index is not index:
            pointerElem = pointerElem.get_next_elem()
            current_index += 1
        return pointerElem

    def patch_ele_index(self, index, new_content):
        pointerElem = self.startElement
        current_index = 0
        while current_index is not index:
            pointerElem = pointerElem.get_next_elem()
            current_index += 1
        pointerElem.content = new_content



class Element():
    def __init__(self, content):
        self.content = content
        self.nextElem = None

    def set_next_elem(self, nextElem):
        self.nextElem = nextElem

    def get_next_elem(self):
        return self.nextElem

    def get_content(self):
        return self.content

if __name__ == '__main__':
    el_list = EinfacheVerketteteListe()
    for i in range(random.randint(5, 10)):
        el_list.append_new_elem(Element(random.randint(0,100)))
    print(el_list.get_length())
    print("------------")
    el_list.print_elems()
    print("------------")
    print(el_list.get_ele_index(3).content)
    print("------------")
    el_list.patch_ele_index(3,0)
    print(el_list.get_ele_index(3).content)
