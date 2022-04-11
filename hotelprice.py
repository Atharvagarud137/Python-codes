print("Enter the number of people:")
no_of_person=int(input())
if no_of_person==2:
    cost = 2500
elif no_of_person==3:
    cost = 3500
elif no_of_person==4:
    cost = 4500
print("Are there any additional guest(Y/N)?")
resp1=input()
if resp1=='Y' or resp1=='y':
    print("Enter number of additional persons:")
    add_persons=int(input())
    cost1=cost+(add_persons*1000)
print("Are you a company employee or a businessman(Y/N)?")
ans1=input()
if ans1=='Y' or ans1=='y':
    cost2=cost1-(0.2*cost1)
print("Are you above 60 years of age(Y/N)?")
ans2=input()
if ans2=='Y' or ans2=='y':
    cost3=cost2-(0.15*cost2)
print("Total payable cost is: ",cost3)
