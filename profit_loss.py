cp=int(input("enter the cost price(CP)"))
sp=int(input("enter the selling price(SP)"))
if(sp>cp):
    print("prifit")
    amt=sp-cp
    print("profit of rupees",amt)
    per=(amt/cp)*100
    print("percentage of profit",per)
else:
    print("losss")
    amt = cp-sp
    print("loss of rupees", amt)
    per = (amt / cp) * 100
    print("percentage of loss", per)