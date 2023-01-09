def fibo(n):
    if n<=1:
        return n 
    else:
        return (fibo(n-1)+fibo(n-2))

num=int(input("Enter number to get Fibonacci Series : "))
fibo(num)
for i in range(num):
    print(fibo(i))