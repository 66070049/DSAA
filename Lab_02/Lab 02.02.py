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
            return "Underflow: Cannot pop data from an empty list"
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
            return "Underflow: Cannot get stack top from an empty list"
        else:
            return self.data[-1]
    def get_size(self):
        '''Size'''
        return self.size
    def print_stack(self):
        '''Print'''
        print(self.data)

NAMES_ = [
    "Walter", "Skyler", "Jesse", "Saul",
    "Mike", "Hank", "Marie",
    "Kim", "Gustavo", "Salamanca"
]


def print_status():
    """Print all stacks"""
    print("This is stack 1 (%d): " % STACK1_.get_size(), end='')
    STACK1_.print_stack()
    print("This is stack 2 (%d): " % STACK2_.get_size(), end='')
    STACK2_.print_stack()
    print("This is stack 3 (%d): " % STACK3_.get_size(), end='')
    STACK3_.print_stack()
    print()


STACK1_ = ArrayStack()
STACK2_ = ArrayStack()
STACK3_ = ArrayStack()
for i in range(len(NAMES_) // 2):
    STACK1_.push(NAMES_.pop())
    STACK2_.push(NAMES_.pop())
print_status()

while not STACK1_.is_empty() and not STACK2_.is_empty():
    STACK3_.push(STACK1_.get_stack_top())
    STACK3_.push(STACK2_.pop())
print_status()

for _ in range(STACK3_.get_size() + 1):
    STACK3_.pop()
print(STACK3_.pop())
print_status()

while not STACK1_.is_empty():
    TEMP_ = STACK1_.pop()
    STACK2_.push(TEMP_)
    STACK3_.push(TEMP_)
print_status()

while not STACK2_.is_empty():
    TEMP_ = STACK2_.pop()
    print(TEMP_)
print()
print_status()

while not STACK3_.is_empty():
    STACK2_.push(STACK3_.pop())
print_status()
