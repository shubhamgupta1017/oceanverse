a=int(input("give a year "))
if(a%4==0):
    if(a%100==0):
        if(a%400==0):
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("Leap Year")
else:
    print("not Leap Year")
