'''Lab_02'''
class ArrayStack:
    '''Stack'''
    def __init__(self):
        '''Stack'''
        self.size = 0
        self.data = []
    def push(self, inp_data):
        '''Push'''
        try:
            if inp_data.isdigit():
                inp_data = int(inp_data)
            elif inp_data.replace(".", "", 1).isdigit():
                inp_data = float(inp_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(inp_data)
            self.size += 1
    def pop(self):
        '''Pop'''
        if self.size == 0:
            self.data = None
            return "Underflow: Cannot pop data from an empty list \n{data}".format(data=self.data)
        else:
            self.size -= 1
            return self.data.pop()
    def is_empty(self):
        '''Check'''
        if self.size == 0:
            return True
        else:
            return False
    def get_stack_top(self):
        '''Stack_Top'''
        if self.size == 0:
            return "Underflow: Cannot get stack top from an empty list \n{data}".format(data=self.data)
        else:
            return self.size
    def get_size(self):
        '''Size'''
        return self.size
    def print_stack(self):
        '''Print'''
        print(self.data)
def main():
    '''Stack(Create Stack)'''
    STACK_1 = ArrayStack()
 
    STACK_1.push("100")
    STACK_1.push(100)
    STACK_1.push("3.14")
    STACK_1.push(3.14)
    STACK_1.push("66.4a")
    STACK_1.push("Ackerman")
 
    STACK_1.print_stack()
 
    print(STACK_1.get_size())
    VAR_1 = STACK_1.pop()
    print(VAR_1)
    STACK_1.print_stack()
    print(STACK_1.get_size())
 
    while not STACK_1.is_empty():
        print(STACK_1.pop())
 
    print()
    print(STACK_1.pop())
    print(STACK_1.get_stack_top())
    print(VAR_1)
main()