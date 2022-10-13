
from cmath import sqrt


a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
de=float((b**2)-(4*a*c))
sol1=(-b+sqrt(de))/(2*a)
sol2=(-b-sqrt(de))/(2*a)
print("ans 1 is: ",sol1)
print("ans 2 is: ",sol2)
