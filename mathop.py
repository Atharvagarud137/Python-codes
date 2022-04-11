print("Enter a number:")
num=int(input())
sqrt=num**0.5
sq=num**2
cube=num**3
print("Square of the number is: ",sq)
print("Square root of the number is: ",sqrt)
print("Cube of the number is: ",cube)
if num > 1:
    for i in range(2, int((num/2)+1)):
        if (num%i) == 0:
            print(num,"is not a prime number.")
            break
    else:
        print(num,"is a prime number.")
        
else:
    print(num,"is not a prime number.")
