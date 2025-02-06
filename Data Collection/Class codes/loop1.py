loop_list=[]
for i in range(1,6):
    if(i>=4 and i<5):
        j=4
        print(4)
        loop_list.append(j)
    elif(i==5):
        print(5)
        loop_list.append(5)
    else:
        print(i)
        loop_list.append(i)



print(loop_list)        
