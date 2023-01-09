mystr=input("Enter a String: ")
print(*map(mystr.lower().count,"aeiou"))