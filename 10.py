import math
n=int(input("give a num "))
flag=False
for i in range(2,int(math.sqrt(n))):
    if(n%i==0):
        flag=True
        break
if(flag==1):
    print("not Prime")
else:
    print("prime")
