print("This program will calculate your BMI: ")
weight =int(input("enter Weight: ")) 
height =int(input("enter Height: "))
bmi = weight /(height ** 2)
if bmi < 19:
    print("you are underwight")
elif bmi > 25:
    print("you are overwight")
else:
    print("you are helthy") 