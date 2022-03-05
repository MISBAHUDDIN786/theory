units=int(input("enter the numer of units"))
if(units<=50):
    bill=units*50
    bill = bill / 100
    print("tne amount of bill you have to pay in rupees is:",bill)
elif(units<=150):
    bill=((units-100)*50)+((units-50)*75)
    bill = bill / 100
    print("tne amount of bill you have to pay in rupees is:",bill)
elif(units<=250):
    bill=((units-250)*50)+((units-150)*75)+((units-150)*120)
    bill = bill / 100
    print("tne amount of bill you have to pay in rupees is:",bill)
elif(units>=250):
    bill=(50*50)+(100*75)+(100*120)+((units-250)*150)
    bill = bill / 100
    print("tne amount of bill you have to pay in rupees is:",bill)