'''Lab_01'''
class Point:
    '''Lab_01'''
    def __init__(self, xxx, yyy):
        '''Lab_01'''
        self.set_coor(xxx, yyy)
    def set_coor(self, xxx, yyy):
        '''Lab_01'''
        self.xxx = xxx
        self.yyy = yyy
    def get_coot(self):
        '''Lab_01'''
        return (self.xxx, self.yyy)
    def cal_dis(self, other):
        '''Lab_01'''
        return (((other.xxx - self.xxx)**2) + ((other.yyy - self.yyy)**2))**0.5
def main():
    '''Lab_01'''
    p_1 = Point(float(input()), float(input()))
    p_2 = Point(float(input()), float(input()))
    total = p_1.cal_dis(p_2)
    print("%.2f" % total)
main()
