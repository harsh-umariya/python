def ch(x):
    cont=1
    for i in range(2,x-1):
        if x%i==0:
            cont=cont+1
    if cont>=2:
        print("number is not prime")
    else:
        print("number is prime")
x=int(input("Enter number : "))
ch(x)