avg=0
for i in range(5):
    avg+=int(input())
avg/=5
if(avg>=90):
    print("A")
elif(avg>=80):
    print("B")
elif(avg>=70):
    print("C")
elif(avg>=60):
    print("D")
else:
    print("F")
