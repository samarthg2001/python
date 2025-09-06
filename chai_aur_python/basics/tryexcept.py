try:
    a=10/0
except :
    print("hello world")
else:
    print("this is else block")
    
def fun(*a):
    for i in a:
        print(i)

my_list=[10,20,30,4,5,6,8,]

my_value=("afds","fasfas","fdasfd" ,"")

fun(my_list)
fun(my_value)

fun(9,10,2,3,5,60)

def sample(a,b,c,d):
    print(a,b,c,d)
def sample1(*t):
    for i in t:
        print(i)

sample1(*my_list)
sample1(*my_value)
# sample(*my_list) TypeError: sample() takes 4 positional arguments but 7 were given
sample(*my_value)