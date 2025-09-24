search_list=[12,3,56,8,2,6,82,2,65,56,2]

print("liner search")
search_element=int(input("Enter the value that need to find in list "))

flag=False
index=0
for i in search_list:
    if search_element in search_list:
        index=i
        flag=True
        print(f"element found in {i} index ")
        break

if not flag :
    print("Value is not found in list")

print("program end")


def count_element(listvalue, element):
    count=0
    for i in listvalue:
        if i == element:
            count=count+1
    return count;


repated_number=count_element(search_list,2)
print(f"repated numbers {repated_number}")