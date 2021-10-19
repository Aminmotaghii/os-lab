import random
import array 

x= array.array('i')

n = int (input("Enter Number of Array Items : "))
for i in range(n):
    x.append(int(input("Enter Array Item : ")))

flag=1 
for i in range(1,n,1):
    if(x[i]<x[i-1]):
        flag=0
        break
    
if(flag==0):
    print("No")
else:
    print("Yes")
 
    