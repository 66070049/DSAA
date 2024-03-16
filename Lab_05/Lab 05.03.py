'''Lab_05'''
class DataNode:
    '''Data_Node'''
    def __init__(self, data=None):
        '''Data'''
        self.__data = data
        self.__next = None
    def get_data(self):
        '''Get_data'''
        return self.__data
    def set_data(self, data):
        '''Set_Data'''
        self.__data = data
    def get_next(self):
        '''Get_next'''
        return self.__next
    def set_next(self, next_):
        '''Set_next'''
        self.__next = next_

class SinglyLinkedList:
    '''Singly_Linked_List'''
    def __init__(self):
        '''Data'''
        self.count = 0
        self.head = None
    def traverse(self):
        '''Traverse'''
        node = self.head
        if self.head == None:
            print("This is an empty list.")
            return
        while node is not None:
            if node.get_next() == None:
                print(node.get_data())
            else:
                print(node.get_data(), end=" -> ")
            node = node.get_next()

    def insert_last(self, data):
        '''Insert_Last'''
        last_node = DataNode(data)
        self.count += 1
        if self.head is None:
            self.head = last_node
        else:
            node = self.head
            while node.get_next() is not None:
                node = node.get_next()
            node.set_next(last_node)

    def insert_front(self, data):
        '''Insert_Front'''
        front_node = DataNode(data)
        front_node.set_next(self.head)
        self.head = front_node
        self.count += 1

    def insert_before(self, node, data):
        '''Insert_Before'''
        before_node = DataNode(data)
        if self.head is None:
            print("Cannot insert, " + node + " does not exist.")
            return
        if self.head.get_data() == node:
            before_node.set_next(self.head)
            self.head = before_node
            self.count += 1
            return
        data_node = self.head
        while data_node.get_next() is not None and data_node.get_next().get_data() != node:
            data_node = data_node.get_next()
        if data_node.get_next() is None:
            print("Cannot insert, " + node + " does not exist.")
            return
        before_node.set_next(data_node.get_next())
        data_node.set_next(before_node)
        self.count += 1

    def delete(self, data):
        '''Delete'''
        if self.head is None:
            print("Cannot delete, " + data + "does not exist.")
            return
        if self.head.get_data() == data:
            self.head = self.head.get_next()
            self.count -= 1
            return
        data_node = self.head
        while data_node.get_next() is not None and data_node.get_next().get_data() != data:
            data_node = data_node.get_next()
        if data_node.get_next() is None:
            print("Cannot delete, " + data + "does not exist.")
            return
        data_node.set_next(data_node.get_next().get_next())
        self.count -= 1

def main():
    '''Main'''
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()
