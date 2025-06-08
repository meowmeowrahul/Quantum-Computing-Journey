import math
while True:
    a=int(input("a"))
    if a==256:
        break
    b=int(input("b"))
    theta1=int(input("theta1"))
    theta2=int(input("theta2"))
    print("Sine",a*math.sin(math.radians(theta1))+b*math.sin(math.radians(theta2)))
    print("Cose",a*math.cos(math.radians(theta1))+b*math.cos(math.radians(theta2)))
    