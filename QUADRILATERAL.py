t=int(input())
lst=[]
for i in range(t):
    d,c=map(int,input().split())
    A1,A2,A3=map(int,input().split())
    B1,B2,B3=map(int,input().split())
    sumA=A1+A2+A3
    sumB=B1+B2+B3
    amt1=sumA+sumB+c
    amt2=sumA+sumB+c+d
    amt3=sumA+sumB+d+d
    if sumA>=150 and sumB>=150:
            if amt1<amt2 and amt1<amt3:
                 lst.append("yes")
            else:
                 lst.append("no")
            continue
    elif sumA>=150 and sumB<150:
            if amt2<amt3:
                 lst.append("yes")
            else:
                lst.append("no")  
            continue
    elif sumA<150 and sumB<150:
               lst.append("no")
for j in range(len(lst)):
    print(lst[j])
            
   

    
