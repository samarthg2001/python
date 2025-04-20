# if statemetn = execute some code only if a condition is True
#               they allow for basic decision making
#               (if ,   elif,   else)
# == to compare the values
age=int(input("enter your age : "))

if age>= 18:
    print("you are a adult")
elif age<0:
    print("you are not born yet ")
elif age==0:
    print("you are now born! ")
else:
    print("your are child")