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
            print("Override rectangle",self.l,self.w)
        def area(self):
            return self.l*self.w 
          

class Circle(Shape):
    def __init__(self,r):
            self.r = r
            #self.w = w
            print("Override circle",self.r)
    def area(self):
        return 3.1416*self.r*self.r
    
class Cubic(Shape):
        def __init__(self,l,w,h):
            super().__init__(l,w)
            #Shape.__init__(self,l,w)
            self.h = h
            print("Override cubic",self.l,self.w,self.h)
        def area(self):
            return self.l*self.w*self.h 



r = Rectangle(10,20)
c = Circle(10)
cub = Cubic(100,12,13)
print(r.area)
print(r.area())
print(cub.area())
print(c.area())