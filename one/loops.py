# while loop= used to repeat a block of code as long as
# condition remains  'TRUE'
# we re check the condition at the end of the loop 
# if we did'nt define the loop it will excuate continuasly ,infinilty 

# name=input("enter you name : ")

# while name == "":
#     name=int(input("enter you age : "))

# age=int(input("enter your age : "))

# while age <= 0:
#     age=int(input("enter your age : "))

# print(f"hello {name}")
# print(f"your age  is {age}")    



# for loop =used to iterate over a sequence such as (string ,list ,tupple ,set)
# repeat a block of code and exact amount of items

# range is function range(start ,stop, step)step like increaseing by ++
# for index in range(1,11,3):
#     print(index)

#print all odd numbers between 1  to 100
# for i in range(1,101,2):
#     print(i)
    
#print all  numbers which devided by 27  to 1 to 1000 range
# for i in range(1,1000,27):
#     print(i)
    
batman="Bruce wayne"
for letter in batman:
     print(letter,end=" ")
     print(letter,end="-")
     
# To go backwerd we use -1 in range step

for i in range(10,0,-1):
    print(i,end=" ")