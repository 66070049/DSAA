'''Lab_10'''
class Student:
    '''Class_Student'''
    def __init__(self, std_id, name, gpa):
        '''Self'''
        self.std_id = int(std_id)
        self.name = name
        self.gpa = float(gpa)
    def get_std_id(self):
        '''get_Id'''
        return self.std_id
    def get_name(self):
        '''get_Name'''
        return self.name
    def get_gpa(self):
        '''get_Gpa'''
        return self.gpa
    def print_detail(self):
        '''get_Print'''
        print("ID: {}\nName: {}".format(self.std_id, self.name))
        print("GPA: %.2f" %self.gpa)
def main(text_in):
    '''Main'''
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()
main(input())
