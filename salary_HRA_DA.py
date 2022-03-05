a=int(input("enter your salary"))
if(a<10000):
    salary=((80/100)*a)+((90/100)*a)
    print("salary after adding your HRA and DA",salary)
elif(a>10000 and a<=20000):
    salary=((85/100)*a)+((90/100)*a)
    print("salary after adding your HRA and DA",salary)
elif(a>20000):
    salary=((95/100)*a)+((95/100)*a)
    print("salary after adding your HRA and DA",salary)


