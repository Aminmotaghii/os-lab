h = float (input("Enter Height (Meter) : "))
w = float (input("Enter Weight (KiloGeram) : "))
BMI = w/(h*h)
print("BMI = %.1f"%BMI)
if BMI < 18.5 :
    print("UnderWeight")
elif BMI<25 :
    print("Normal")
elif BMI<30 :
    print("OverWeight")
elif BMI<35 :
    print("Obese")  
else :
    print("Extermely Obese")
