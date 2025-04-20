# Typecasting = the process of converting a variable from 
# one data type to another
# str() ,int(), float(),bool()

name='samarth ganamote'
age=25
gpa=3.2
is_employee=True # 0 false 1 true

# to check the type of variable  type()

print(type(gpa))


# float to integer 

gpa=int(gpa)
print(type(gpa),gpa," integer type casting ")

# name=int(name) it will give error 
print(type(name),name,"string  to integer")
is_employee=int(is_employee)
print(type(is_employee),is_employee)

name=bool(name) 
# it will give true until the string is empty ,empty string give false
print(type(name),name)