l1=[1,2,3,'d','h','r']
print("simply: ",l1)
l1.append("u")
print("add element using adding:",l1)
del l1[0:1]
print("remove element using delete:",l1)
print("the list using the index number:",l1[0])
print("count all element using lenth :",len(l1))

l2=[1,2,5,4,3,6,7,8,9]
print(l2)
l2.sort()
print("sorting list using sort:",l2)
l2.reverse()
print("revers list using reverse:",l2)

print("membership1:",l1+l2)
