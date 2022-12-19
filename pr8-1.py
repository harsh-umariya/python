import random

def unorder(Sample):
    random.shuffle(Sample)
    print(Sample)
    
Sample=[10,20,30,40,50,60,70,80,90,100]
unorder(Sample)

list=[]
x=int(input("Enter no of element you want to enter: "))
for i in range(0,x):

    ele=int(input("Enter element: "))
    list.append(ele)
unorder(list)