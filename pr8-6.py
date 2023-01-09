a=int(input("Enter a Loan amount: "))
b=int(input("Enter a year: "))
c=int(input("Enter a Interast rate: "))
def amo(a,b,c):
        T=((a*b*c)/100)
        print(T)
        TPB=T+a
        print(TPB)
        EMI=((TPB/b)/12)
        print(EMI)
amo(a,b,c)    