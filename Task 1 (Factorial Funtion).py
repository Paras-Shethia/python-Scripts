def cf(n):
    d=1
    for i in range(1,n+1):
        d*=i
    return d
num=int(input("Enter a number: "))
result=cf(num)
print("Factorial of",num ,"is:",result)