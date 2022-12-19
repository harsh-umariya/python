def dup(list):
    list1=[]
    for i in(list):
        if i not in list1:
            list1.append(i)
    print(list1)

list=[]
x=int(input("Enter number of elements you want to enter : "))
for i in range(0,x):
    ele=int(input("Enter element : "))
    list.append(ele)
print(list)
dup(list)