m = int (input("Enter m : "))
n = int (input("Enter n : "))
for i in range(1,m+1):
    for j in range(1,n+1):
        print("%4d"%(i*j),end=" ")
    print()    