#WAP that takes input from user and checks if it is a positive negative or zero number
n=int(input("Enter the number"))
if (n<0):
    print(f"{n} is a negative number")
elif (n==0):
    print(f"{n} is zero")
else:
    print(f"{n} is a positive number")
