def ch(x):
    cont=1
    for i in range(2,x-1):
        if x%i==0:
            cont=cont+1
    if cont>=2:
        print("Number Is Not Prime")
    else:
        print("Number Is Prime")
x=int(input("Enter Number : "))
ch(x)
