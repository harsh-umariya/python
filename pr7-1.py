print("------Create The Tuple--------")
tup=(1,2,3,4,5,6,7,8,9)
print(tup)

print("------Tuple to List convert-------")
tup=list(tup)
print(type(tup))
print(tup)

print("-------Deletetion-------")
del tup[1]
print(tup)

print("------List to tuple conert------")
tup1=tuple(tup)
print(type(tup1))
print(tup1)