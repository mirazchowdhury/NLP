def fib(limit):
    num1,num2 = 0,1


    while num1<limit:
        yield num1
        num1, num2 = num2, num1+num2

gen_fib = fib(100)

print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))
print(next(gen_fib))




