n=input("enter Integer value of n: ")
i=1
data=0
pattern=""
if(int(n)<1)|(int(n)>9):
    print("please enter a number between 1 to 9")
else:
    print("Print the sum of series for",n)
    while(i<=int(n)):
        num=i*n
        pattern=pattern+"+"+num
        data=data+int(num)
        i+=1
pattern=pattern.lstrip("+")
print(pattern,"=",data)