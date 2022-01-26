class Node:
    def __init__(self, obj, ptr_next):
        self.__obj = obj
        self.__ptr_next = ptr_next

    def get_obj(self):
        return self.__obj

    def set_obj(self, obj):
        self.__obj = obj

    def get_next(self):
        return self.__ptr_next

    def set_next(self, next):
        self.__ptr_next = next

