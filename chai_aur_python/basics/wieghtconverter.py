wieght =float(input("enter your weight : "))



while True:
    unit=input("Kilograms or Pounds ?  ( K or L) : ")
    if unit=="K":
        wieght=wieght*2.205
        unit="LBS"
        break
    elif unit=="L":
        wieght=wieght/2.205
        unit="Kgs"
        break
    else:
       print("enter the valid string")
    
print(f"your weight is : {round(wieght,2)} {unit}")