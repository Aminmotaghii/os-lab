import random
import array 
a = array.array('i')
n = int (input("Enter N : "))
tedad=0
while(tedad<n):
    x = random.randint(1,1000)
    flag=0 
    for i in range(tedad):
        if(x==a[i]):
            flag=1
    if(flag==0):
        a.append(x)
        tedad+=1
            
for i in range(n):
    print(a[i])
    

