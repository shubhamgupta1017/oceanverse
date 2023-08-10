a=str(input("Give a string "))
flag=False
for i in range(len(a)//2):
    if(a[i]!=a[-i-1]):
        flag=True
        break
if(flag):
    print("no")
else:
    print("yes")
