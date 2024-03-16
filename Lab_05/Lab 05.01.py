'''Lab_05'''
class DataNode:
    '''Data'''
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

def main():
    '''Main'''
    d_1 = DataNode(input())
    print(d_1.get_data())
    print(d_1.get_next())
main()
