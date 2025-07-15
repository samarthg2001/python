print("hello")
a='''adskfhkjds
vdasknfjdsal
fndsafkjasld'''

value1=6//3
value13=2
value2=6/3

print("the first value //",value1,"the second value /",value2)
list()
tuple()
my_list=[1,2.0,'s','sdhfkahsf','''dsafsadfsd
         sfdssajhfkjsdf''',"mylist"]
my_list2=[1,2.0,'s','sdhfkahsf','''dsafsadfsd
         sfdssajhfkjsdf''',"mylist"]
for i in my_list:
    print(i)
my_tuple=(1,2,3.0,"s","dashfkahs",'''dfasdfe
          sdafas''')
my_tuple2=(1,2,3.0,"s","dashfkahs",'''dfasdfe
          sdafas''')
for i in my_tuple:
    print(i)
    
    
my_dist={
    'key1':"value1",
        'key2':"value2"
}

print(my_dist)
print(id(value1),id(value2),id(value13))
print(my_dist.items)
print(id(my_list2),id(my_list))
print(id(my_tuple2),id(my_tuple))
print(value13 is value1) #True
print(value1 == value13) #True


print()
print()