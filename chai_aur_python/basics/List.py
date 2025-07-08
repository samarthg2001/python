# '''
# A list in Python is:

# An ordered collection of items

# Mutable (you can change it)

# Can contain mixed data types

# Allows duplicate value
# '''
# # Empty list
# empty = []

# # List of integers
# nums = [1, 2, 3, 4]

# # Mixed data types
# mixed = [1, "two", 3.0, False]

# # Nested list
# nested = [[1, 2], [3, 4]]



# myList=[10,20,'s','python',5.5,["`hello" ,"world"]]

# print(myList[-1][-2]) #hello
# print(myList[5][1]) #world
# print(myList[2]) #s
# print(myList[1:5]) #[20, 's', 'python', 5.5]

# lst = ['a', 'b', 'c', 'd']
# for item in lst:
#     print(item)

# # With index
# for i, item in enumerate(lst):
#     print(f"Index {i}: {item}")
    
# ## access by loop
# for i in myList:
#     print(i)

# lst[0]=123

# lst.append(5)# in last 
# lst.extend([4,5,8]) # add in last
# lst.insert(1,5)# index value

 #  / give float value  // give interger value

mylist=[10,20,30,40,50]

# mylist[0]="first"
# mylist[-1]="last"
# midd_value=len(mylist)//2 
# int(midd_value)
# mylist[midd_value]="middle value"

# print(mylist)

# mylist.append("another last value") 
# mylist.insert(2,"2nd element")

# print(mylist)

# mylist.remove(10)# need to give value in remove(value)
# print(mylist)

# mylist.pop() # deafult last element pop(index)
# print(mylist)

# print(mylist[0:3])
# print(mylist[-4:-1])

# # we can not add direct string value in multiple if condition
# value="this value"
# mylist.append("another value")
# print(mylist)
# if ( 40 in mylist or "this value" in mylist ):
#     print("this value is present")
# else :
#     print("this value not present" )


# x=int(input("enter number of element of list"))
# emt=[]
# for i in range(x):
#     emt.append(input(f"enter the {i} element in list"))

# search_element=input("enter the serach element ")
# count=0
# for i in emt:
#     if (search_element == i):
#         count +=1
# print(emt)
# print(count)


print(mylist)

print(len(mylist))

mylist.reverse()
print(mylist)

rev=mylist[::-1]

print(rev)

sum=0
for i in mylist:
    sum+=i
print(sum)

