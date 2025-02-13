car={'Brand':'Toyota','Price':'20000000','Year':2020}
print(car)
print(car.keys())
print(car.values())

#It will show the keys, not the values
for i in car:
    print(i)

#It will show the values
for i in car:
    print(car[i])

#It will also show the values
for i in car.values():
    print(i)

#It will show cars and items 
for i,j in car.items():
    print(i,j)