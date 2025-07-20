# **Replace all negative numbers in a list with 0.**


my_list=[-4,0,-5,1,5,6,0,8,]


# print(my_list)
# for i in my_list:
#     print(i)
#     if i < 0 :
#         my_list[i]=0
        
# print(my_list)

for i ,value in enumerate(my_list):
    if value<0:
        my_list[i]=0


print(my_list)
    


my_list2 = [-4, 0, -5, 1, 5, 6, 0, 8]

print("Original List:", my_list2)

# Replace negative numbers with 0 using index
for index in range(len(my_list2)):
    if my_list[index] < 0:
        my_list[index] = 0

print("Modified List:", my_list2)


