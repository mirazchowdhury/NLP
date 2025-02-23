class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print(self.x)
        print(self.y)
    def __add__(self,other):
        print(other.x)
        print(other.y)
        return self.x+other.x,self.y+other.y
p1 = Point(1,2)
p2 = Point(3,4)

p3 = p1 + p2

print(p3)


# a = 100
# b = 900
# print(a.__add__(b))

# a = "1"
# b = "900"
# print(a.__add__(b)) 
# output ---- 1900 [string_concat]

# https://www.geeksforgeeks.org/dunder-magic-methods-python/