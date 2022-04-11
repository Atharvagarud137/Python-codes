print("Enter a number:")
num=int(input())
if num<0:
    print("Square root of the number cannot be calculated.")
else:
    sqrt=num**0.5
    print("Square root of the number is: ",sqrt)
sq=num**2
cube=num**3
print("Square of the number is: ",sq)
print("Cube of the number is: ",cube)
if num < 0:
    print("Prime number is not defined for negative numbers.")
else:
    if num > 1:
        for i in range(2, int((num/2)+1)):
            if (num%i) == 0:
                print(num,"is not a prime number.")
                break
    else:
        print(num,"is a prime number.")
