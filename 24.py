a,b=input("give input like ex 34 C or 24 :- ").split()
if(b=='C'):
    temp=(int(a)*1.8)+32
    b='F'
else:
    temp=(int(a)-32)*5/9
    b='C'
print(temp,b)
