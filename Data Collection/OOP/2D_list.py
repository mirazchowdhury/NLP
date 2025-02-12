demo_variable = [["apple",2,3],[4,"Messi",6],[7,8,9.6251]]

# for i in range(len(demo_variable)):
#     for j in range(len(demo_variable[i])):
#         print(demo_variable[i][j])

# for row in demo_variable:
#     for col in row:
#         print(col)

blank_list=[]

for i in demo_variable:
    for j in i:
        blank_list.append(j)

print(blank_list)
