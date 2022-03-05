a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if(a>b)&(a>c):
    print("a is greater than b and c")
elif(b>c)&(b>a):
    print("b is greater than a and c")
else:
    print("c is greater than b and a")