search_list=[12,3,56,8,2,6,82]

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