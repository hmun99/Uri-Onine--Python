import math
a,b,c = list(map(float, input().split()))
if (a == 0) | (((b*b)-(4*a*c))<0):
    print("Impossivel calcular")
else:
    r1 = (((-b) + math.sqrt((b*b)-(4*a*c)))/(2*a));
    r2 = (((-b) - math.sqrt((b*b)-(4*a*c)))/(2*a));
    print("R1 = %.5f"%r1)
    print("R2 = %.5f"%r2)

