#function

#built-in function

#user-defined function
def sub(x,y):
    substitute = x-y
    return substitute

a = int(input())
b = int(input())
result = sub(a,b)
print(result)

#Global variable declare inside the function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#How does lambda function works in python

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))