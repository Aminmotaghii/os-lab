class Rational:
  def __init__(mysillyobject, s, m):
    mysillyobject.soorat = s
    if(m!=0):
        mysillyobject.makhraj = m
        print("Rational = " , s , "/" , m)
        print()
    else:
        print("Error")
    
        
  def PrimeRational(p):
      s=p.soorat;
      m=p.makhraj
      
      if(m!=0):
        bmm=1
        for k in range(2,min(s,m)+1):
            if((s%k==0)and(m%k==0)):
                bmm=k 
        p.soorat = int(s/bmm)        
        p.makhraj = int(m/bmm)    
        
        return p
        
  def printRational(p):
      print("Rational = " , p.soorat , "/" , p.makhraj)
      print()
        
  def addRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.makhraj + p1.makhraj*p2.soorat , "/" , p1.makhraj*p2.makhraj)
    
  def subRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.makhraj - p1.makhraj*p2.soorat , "/" , p1.makhraj*p2.makhraj)
    
  def mulRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.soorat , "/" , p1.makhraj*p2.makhraj)  
    
  def divRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.makhraj ,"/" , p1.makhraj*p2.soorat )    
    

k1 = Rational(2,4)
k3=k1.PrimeRational()
print("Bad az sadeh sazi : ")
k3.printRational()

k2 = Rational(7,11)
k1.addRational(k2)
print()

k1.subRational(k2)
print()

k1.mulRational(k2)
print()

k1.divRational(k2)
print()


