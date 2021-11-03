import os
import array 
flag=1;
while(flag==1):
    print("1) Show items")
    print("2) Add item")
    print("3) Change item")
    print("4) Delete items")
    print("5) Search item")
    print("6) Buy ")
    print("7) Exit")
    print("************")
    ch=int(input(" Enter Choice : "))
    if(ch==1):
        f = open("database.csv", "r")
        for x in f:
            print(x) 
        f.close()   
    elif(ch==2):
        f = open("database.csv", "a")
        
        s = input("Enter new item : (Code,Name,Price,No) : ") 
        f.write(s+"\n")
        f.close()   
    elif(ch==3):
        f1 = open("database.csv", "r")
        f2 = open("temp.csv","w")
        s1 = (input("Shomareh Kala ra vared konid : "))
        s2 = (input("Mojoodi jadid ra vared konid : "))
        s3 = (input("Gimat jadid ra vared konid : "))
        for x in f1:
            items = x.split(",")
            if(s1==items[0]):
                items[2]=s2
                items[3]=s3+"\n"
                x=items[0]+","+items[1]+","+items[2]+","+items[3]
                print(items)
            f2.write(x)
    
        f1.close()
        f2.close()
        os.remove("database.csv")
        os.rename("temp.csv","database.csv")
    elif(ch==2):
        f = open("database.csv", "a")
        
        s = input("Enter new item : (Code,Name,Price,No) : ") 
        f.write(s+"\n")
        f.close()   
    elif(ch==4):
        f1 = open("database.csv", "r")
        f2 = open("temp.csv","w")
        s1 = (input("Shomareh Kala ra baray HZAF vared konid : "))
        for x in f1:
            items = x.split(",")
            if(s1!=items[0]):
                f2.write(x)
    
        f1.close()
        f2.close()
        os.remove("database.csv")
        os.rename("temp.csv","database.csv")
    elif(ch==5):
        f1 = open("database.csv", "r")
        s1 = (input("Nam-e Kala ra baray JOSTEJOO vared konid : "))
        yaft=0
        for x in f1:
            items = x.split(",")
            if(s1==items[1]):
                print("Kala peydad shod")
                yaft=1
                for i in items:
                    print(i)
        if(flag==0):
            print("Yaft Nashod")
    
        f1.close()
    elif(ch==6):
        
        sum_factor=0
        codes = []
        sharh = []
        fy = array.array('i')
        print("******************************")
        print(" * * *   Kharid Kala   * * * ")
        tedad = int(input("Tedad Aglam Kharidari ra vared konid : "))
        for k in range(tedad):
            f1 = open("database.csv", "r")
            s1 = input("Code kala ra vared konid : ")
            codes.append(s1)
            s2 = input("Tedad kala ra vared konid : ")
    
            for x in f1:
                items = x.split(",")
                if(s1==items[0]):
                    sp=int(s2)*int(items[2])
                    fy.append(sp)
                    sum_factor=sum_factor+sp
                    sharh.append(items[1])
            f1.close()
        print()
        print()
        print("*******************************")
        print("              Factor           ")
        print("*******************************")
        print("Code   Name   Gimat kol")
        for i in range(tedad):
            print(codes[i],"  ",sharh[i] ," ",fy[i])
        print("-------------------------------")  
        print("Sum = " , sum_factor)
        print("*******************************")
        print()
        print()
        
    elif(ch==7):
        flag=0


