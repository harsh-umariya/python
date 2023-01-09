s=str(input("Enter String : "))
vovle="aeiouAEIOU"
a=0
b=0
for i in s:
    if i in vovle:
        a+=1
    else:
        b+=1
print("Vovles are: ",a)
print("Consonent are: ",b)