#WAP that prints multiplication table using while loop
n=int(input("Enter the number"))
i=1
while i<11:
    print(f"{n} * {i} = {n*i}")
    i+=1