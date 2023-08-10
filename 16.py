a=str(input())
a.lower()
count_v=0
for i in a:
    if(i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
        count_v+=1
print("vowels :",count_v,"consonants :",len(a)-count_v)
