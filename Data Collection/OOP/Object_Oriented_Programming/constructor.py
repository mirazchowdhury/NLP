class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        print(self.name)
        print(self.id)
        print("This is a student constructor")
        #pass

name = "Rubel"
id = "C201074"
Student1 = Student(name,id)


class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def info(self):
        return self.name,self.id
        
name = "Rubel"
id = "C201074"
Student1 = Student(name,id)

s_name, s_id = Student1.info()
print(s_name)
print(s_id)