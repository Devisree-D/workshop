name=input("enter a string :") #test
dict={}
for i in name:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
data=sorted(dict,key=dict.get,reverse=True)
print(data[0])