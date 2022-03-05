num=int(input("enter your university roll number"))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
print("the sum of last 3 digits",(a+b+c))