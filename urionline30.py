a,b,c = map(float,input().split())
if (b+c)>a and (a+c)>b and (a+b)>c:
    area = a+b+c
    print("Perimetro = %.1f"%area)
else:
    trap = (c*(a+b))/2
    print("Area = %.1f"%trap)