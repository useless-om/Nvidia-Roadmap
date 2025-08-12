a=input("enter the degree to convert c/f :")
b=float(input("enter the value:"))
if a=="c" :
    b=round((9*b)/5 +32,3)
    print(f"the temperature in farenheit is {b}")
else :
     b = round((b-32)*5/9,3)
print(f"the temperature in celcius is {b}")

