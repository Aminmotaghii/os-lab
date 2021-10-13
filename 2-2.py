import random
bc=0
bu=0

while bc<5 and bu<5 :
    su = int (input("1)Sang 2)Kaghaz 3)Gheychi : "))
    sc = random.randint(1,3)
    print("Entekhab Computer = ",sc)
    if( ((su==1) and (sc==3)) or ((su==2) and (sc==1)) or ((su==3) and (sc==2)) ) :
        bu+=1
    elif( ((su==3) and (sc==1)) or ((su==1) and (sc==2)) or ((su==2) and (sc==3)) ) :
        bc+=1

print("Computer = ",bc)        
print("Karbar   = ",bu)
        
