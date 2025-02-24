class Person:
# Constructor works as a initializer. When we create an object for a class, then the constructor has called by automatically. It is basically initialize the object.

# If we won't write the constructor, it will call a constructor by default which will work as an arguement function


# self is basically used to reference an object.

    def __init__(self,name,age,email,university,department):
        self.name = name
        self.age = age
        self.email = email
        self.university = university
        self.department = department
        
    
    def method(self):
        return f"Hi!! I am {self.name}. I am from {self.university}. I am {self.age} years old. My email account is {self.email}. My department is {self.department}"
    
person1 = Person("Miraj", "25", "mirajuddinchowdhury@outlook.com","International Islamic University Chattogram", "Computer Science and Engineering")

print(person1.method())



