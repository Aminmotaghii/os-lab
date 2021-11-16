class Rational:
  def __init__(mysillyobject, s, m):
    mysillyobject.soorat = s
    if(m!=0):
        mysillyobject.makhraj = m
    else:
        print("Error")
        

  def addRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.makhraj + p1.makhraj*p2.soorat , "/" , p1.makhraj*p2.makhraj)
  def subRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.makhraj - p1.makhraj*p2.soorat , "/" , p1.makhraj*p2.makhraj)
  def mulRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.soorat , "/" , p1.makhraj*p2.makhraj)  
  def divRational(p1,p2):
    print("Kasr1 + Kasr2 = " ,p1.soorat*p2.makhraj ,"/" , p1.makhraj*p2.soorat )    

k1 = Rational(3,4)
k2 = Rational(7,11)
k1.addRational(k2)
print()

k1.subRational(k2)
print()

k1.mulRational(k2)
print()

k1.divRational(k2)
print()


