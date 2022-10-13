from cmath import sin

h = int(input("houeshight is: "))
a = int(input("angle is: "))
pie=(3.14)
alagler = ((pie/180)*a)
l=(h/sin(alagler))
print("ladder langht:",l)
