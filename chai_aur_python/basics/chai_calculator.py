value1 =int(input("enter the first value"))
value2=int(input("enter the second value"))

while 1:
    operator=input("enter the operator")
    if operator=='+':
        print(value1+value2)
        break 
    elif operator=='-':
        print(value1-value2)
        break
    elif operator=='*':
        print(value1*value2)
        break
    elif operator=='/':
        print(value1/value2)
        break
    else :
        print("enter the operator in these between  + , - ,* ,/ ")