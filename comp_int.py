pamt=int(input("enter the principle amount"))
r=int(input("enter the annual rate of interest"))
t=int(input("enter the time in yera"))
n=int(input("enter the compound per year"))
intr=pamt*(1+(r/n)**(n*t))
print("simple interest is:",intr)
