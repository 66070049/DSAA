'''Lab_02'''
class ArrayStack:
    '''Group'''
    def __init__(self):
        '''Group'''
        self.data = []
    def push(self, inp_data):
        '''Push'''
        self.data.append(inp_data)
    def pop(self):
        '''Pop'''
        return self.data.pop()