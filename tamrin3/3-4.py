import random
x = int (input("Enter x : "))
p=1 
i=1
while(p<x):
   p*=i 
   i+=1

if(p==x):
    print("Yes")
else:
    print("No")