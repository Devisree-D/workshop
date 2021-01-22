string=input("enter the string: ")
first=input("enter the first letter:")
second=input("enter the second letter:")
dict={}
flg=0
for st in string:
    words=string.split(" ")
#print(words)
for wrd in words:
    for wd in wrd:
        if (wd not in dict) :
            dict[wd]=1
        elif(wd==first) & (second in dict):
            flg+=1
            break
        else:
            dict[wd]+=1
if flg==1:
    print(False)
else:
    print(True)

