class Complex:
  def __init__(mysillyobject, h, m):
    mysillyobject.hagigi = h
    mysillyobject.mohoomi = m
    if(m>0):
        print("Complex = " ,h," + ",m , "i")
    else:
        print("Complex = " ,h," - ",m , "i")
    print()    
        
  def addComplex(p1,p2):
    print("Complex1 + Complex2 = " ,p1.hagigi + p2.hagigi , " + (" , p1.mohoomi + p2.mohoomi,")i")
  def subComplex(p1,p2):
    print("Complex1 - Complex2 = " ,p1.hagigi + p2.hagigi , " - (" , p1.mohoomi + p2.mohoomi,")i")
  def mulComplex(p1,p2):
      a=p1.hagigi
      b=p1.mohoomi
      c=p2.hagigi
      d=p2.mohoomi
      print("Complex1 - Complex2 = " ,a*c-b*d , " + (" , a*d+b*c,")i")

k1 = Complex(3,4)
k2 = Complex(7,11)
k1.addComplex(k2)
print()

k1.subComplex(k2)
print()

k1.mulComplex(k2)
print()


