import random
x = int (input("Enter x : "))
argam = 0
y=x

while (x > 0):
  x = x//10
  argam = argam + 1

x=y
s=0
for k in range(argam):
    r = x%10
    s = s + pow(r,argam)
    x = x//10
    



if(s==y):
    print("Yes")
else:
    print("No")