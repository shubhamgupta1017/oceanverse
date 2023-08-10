def c_prime(a):
    global l
    for i in l:
        if(a%i==0):
            return
    l.append(a)
    print(a)
n=int(input())
l=[]
for i in range(2,n+1):
    c_prime(i)

