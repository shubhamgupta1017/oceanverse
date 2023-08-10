def gcd(b,a):
    if(b==0):
        return a
    return gcd(min(b,a%b),max(b,a%b))

a=int(input("give 1st num "))
b=int(input("give 2nd num "))
print(gcd(min(a,b),max(a,b)))
