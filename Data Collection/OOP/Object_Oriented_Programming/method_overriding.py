class Shape:
    def __init__(self,l,w):
        self.l = l
        self.w = w
        print(self.l,self.w)
    def area(self):
        pass    

class Rectangle(Shape):
        def __init__(self,l,w):
            self.l = l
            self.w = w
            print("Override",self.l,self.w)
        def area(self):
            return self.l*self.w 
          

class Circle(Shape):
    def __init__(self,r):
            self.r = r
            #self.w = w
            print("Override circle",self.r)
    def area(self):
        return 3.1416*self.r*self.r
r = Rectangle(10,20)
c = Circle(10)

print(r.area)
print(r.area())

print(c.area())