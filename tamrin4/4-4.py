import array 

fib = array.array('i')

n = int (input("Enter N : "))

a=1 
b=1 
fib.append(a)
fib.append(b)

for i in range(2,n):
    c=a+b 
    fib.append(c)
    a=b 
    b=c 
print("****************")
print("Fibonachi Seri : ")
for i in range(n):
    print(fib[i])