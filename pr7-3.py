print("-------->print Dictionary<---------")
dic={"Name":"Harsh","Age":18,"En_roll":216060307008,"Department":"Computer"}
print(dic)


print("------>Add key value pair<------")
dic["collage_Name"]="JHDP"
print(dic)


print("------->Removing Opertion<------")
del dic["Age"]
dic.popitem()
dic.pop("Name")
print(dic)

print("---------->Inbilt Method<------------")
d1={"Hello":"hello world Program","My":5272}
dic.update(d1)
print(dic)


print("----------->Itrating a Dictionary<-----------")
for i in dic.items():
    print(i)
for i in dic.values():
    print(i)
for i in dic:
    print(i)
for i in dic:
    print(dic[i])
