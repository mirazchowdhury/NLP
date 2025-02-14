class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        
    def display_info(self):
        print("the name of employe", self.name)
        print("the id of employe", self.emp_id)

class Manager(Employee):
    def display_department(self, dep_name):
        print("the name of department", dep_name)

class Developer(Manager):
    def display_expertise(self, lang_name):
        print("the name of department", lang_name)

# Example usage
manager = Manager('Salman', '101')
dev = Developer('Manaur', '102')

manager.display_info()
manager.display_department("Engineering")
dev.display_info()
dev.display_department("Engineering")
dev.display_expertise("Python")