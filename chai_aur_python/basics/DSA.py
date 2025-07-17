
my_list=[75,2,35,48,96,]
print(my_list)


## find the highest and lowest

min=my_list[0]
max=my_list[0]

for i in my_list:
    if i>min:
        min=i
    elif i<max:
        max=i
    else:
        continue

print(max,min)

my_list.sort()

print("the max is ",my_list[-1],"the min is ",my_list[0])
    
