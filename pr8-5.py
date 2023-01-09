def GCD(a,b):
    if a==b:
        return a
    elif a<b:
        return GCD(b,a)
    else:
        return GCD(b,a-b)
a=int(input("Enter I Number : "))
b=int(input("Enter II Number : "))
print(GCD(a,b))