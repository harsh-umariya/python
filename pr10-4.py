str1=input("Enter String:")
str2=input("Enter String:")
def check(str1,str2):
    if (sorted(str1)==sorted(str2)):
        print("Is Anagrams")
    else:
        print("Is not Anagrams")
check(str1,str2)            