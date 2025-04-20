# List [] =mutable ,most flexiable
# tuple () = immutable ,faster 

# set {} =mutable(add/remove) ,unordered
#     no duplicates ,best for membership testing
#  to check (if statemtn )given element is within that set 

# fruits= ["apple ","orange", "banana","coconut" ]

# print(fruits)
# print(fruits[1])
# # print(fruits[5]) IndexError: list index out of range

# for i in fruits:
#     print(i,end=" ")
    
# fruits[1]="mango"
# fruits.append("kiwi") # it will add in last
# # fruits.remove("banana")
# # fruits.pop(2)# it will remove 2 index value
# #  fruits.clear() it will remove all the items if list []

# print(fruits)



# fruits1= ("apple ","orange", "banana","coconut" )

# for i in fruits1:
#     print(i,end=" ")

fruits1= {"apple","orange", "banana","coconut" }
for i in fruits1:
    print(i,end=" ")
fruits2= {"apple","orange", "banana","coconut" ,"coconut" ,"coconut" ,"coconut" ,"coconut" ,"coconut" }
fruits2.add("kiwi")
fruits2.add("grapes")
# fruits1.pop(2) TypeError: set.pop() takes no arguments (1 given)
fruits2.remove("apple")
for i in fruits1:
    print(i,end=" ")    

fruit=input("enter the fruit to found : ")
if fruit in fruits1 :
    print(f"{fruit} is  found in fruits ")
else: 
    print(f"{fruit} is not found in fruits ")
