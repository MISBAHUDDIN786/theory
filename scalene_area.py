a=int(input("enter the length of first side of triangle"))
b=int(input("enter the length of second side of triangle"))
c=int(input("enter the length of third side of triangle"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("area of triangle",area)