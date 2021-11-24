class TimeClock:
  def __init__(mysillyobject, d, s):
    mysillyobject.dagige = d
    mysillyobject.sanieh = s
    mysillyobject.saat = 0
    print("Time = " , "0",":",d , ":" , s)

  def addTime(p1,p2):
    st=0
    ss=p1.sanieh + p2.sanieh
    dd=p1.dagige + p2.dagige
    if(ss>=60):
        dd+=1
        ss-=60
    if(dd>=60):
        st=1
        dd-=60
    print("Time1 + Time2 = " ,st,":",dd,":",ss)
    
  def subTime(p1,p2):
    if(p1.dagige<p2.dagige):
        temp=p1
        p1=p2
        p2=temp
    st=0
    ss=p1.sanieh - p2.sanieh
    dd=p1.dagige - p2.dagige
    if(ss<0):
        dd-=1
        ss+=60
    print("| Time1 - Time2 | = " ,st,":",dd,":",ss)
    
  def Time_Second(p):
        s=p.dagige*60+p.sanieh
        print("Time = ",s ,"Second(s)")
        
  def Second_Time(p1,p2):
        ss=p2%60
        dd=int(p2/60)
        print( "0",":",dd , ":" , ss)
    
k1 = TimeClock(20,45)
k1.Time_Second()
print("------------------------")

k2 = TimeClock(35,20)
print("------------------------")

k1.addTime(k2)
print("------------------------")

k1.subTime(k2)
print("------------------------")

sec_example=1426
print("Seconds = ",sec_example , " that is : " )
k1.Second_Time(sec_example)

