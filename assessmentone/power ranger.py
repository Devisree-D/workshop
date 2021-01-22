num=int(input("enter a number: "))
low=int(input("enter lower limit :"))
upp=int(input("enter upper limit :"))
data=""
if (low<upp):
    for i in range(1,(upp+1)):
        res=i**num
        if(res>=low)&(res<=upp):
            data=data+str(i)
    values=len(data)
    print(values)
else:
    print("lower limit should be always less than upper limit")