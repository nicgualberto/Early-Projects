print("\n=== \033[1;37mTRIANGLE ANALYZER\033[m ===")

reta1 = float(input("Type first side of the triangle: "))
reta2 = float(input("The second: "))
reta3 = float(input("Third: "))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    print("\033[1;34mIt's possible to form a triangle!\033[m")
else:
    print("\033[1;31mIt isn't possible to form a triangle!\033[m ")
    
print("\033[1;37mTRIANGLE CLASIFICATION\033[m")
if reta1 == reta2 == reta3:
    print("It's a equilateral triangle!")
elif (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1) or (reta1 == reta3 and reta1 != reta2):
    print("It's a isoceles triangle!")
else:
    print("It's a scalene triangle! ")
