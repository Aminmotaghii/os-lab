m = int (input("Enter M : "))
n = int (input("Enter N : "))
bmm=1
for i in range(1,min(m,n)+1,1):
    if((m%i==0)and(n%i==0)):
        bmm=i

print("BMM = ",bmm)   