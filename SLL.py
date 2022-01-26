from Node import Node


class SLL:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def get_node(self, pos):
        counter = 1
        tmp_node = None
        while counter <= pos:
            if counter == 1:
                tmp_node = self.__head
            else:
                tmp_node = tmp_node.get_next()
            counter = counter + 1
        return tmp_node

    def add(self, obj_data):
        if self.__head == None:
            self.__head = Node(obj_data, None)
        else:
            tail = self.get_node(self.__size)
            new_node = Node(obj_data, None)
            tail.set_next(new_node)
        self.__size = self.__size + 1

    def remove(self, pos):
        if pos == 1:
            tmp_node = self.get_node(1)
            self.__head = tmp_node.get_next()
        elif pos == self.__size and self.__size >1:
            tmp_node = self.get_node(pos-1)
            tmp_node.set_next(None)
        else:
            current = self.get_node(pos)
            previous = self.get_node(pos-1)
            previous.set_next(current.get_next())
        self.__size = self.__size - 1

    def size(self):
        return self.__size
