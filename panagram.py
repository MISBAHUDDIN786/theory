str=input("enter the string")
i=0
count=0
for i in range(ord('a'),ord('z')+1):
    r=str.find(chr(i))
    
    if (r==-1):
        print("not panagram")
        break
    else:
        count=count+1
if (count==26):
    print("panagram")
    
        
