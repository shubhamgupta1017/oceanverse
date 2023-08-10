a=0
b=1
n=int(input("give a number "))
print(0)
print(1)
for i in range(2,n):
    temp=b
    b+=a
    a=temp
    print(b)
