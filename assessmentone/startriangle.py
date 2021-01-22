n=int(input("Enter the number of rows in the * triangle: "))
if (n<=2):
    print("please enter a number greater than 2")
else:
    print("Triangle of", n, " rows with *")
    for row in range (1,(n+1)):
        for col in range(2,(2*n)-1):
            sum=row+col
            diff=col-row
            if (row==n)|(sum==(n+1))|(diff==(n-1)):
                print("*",end="")
            else:
                print(end=" ")
        print()