a = float(input())
if a >= 0.00 and a <= 2000.00:
    print("Isento")
elif a >= 2000.01 and a <= 3000.00:
    x = (a-2000)*.08
    print("R$ %.2f"%x)
elif a >= 3000.01 and a <= 4500.00:
    x = (a-3000)*.18+ (1000.00*.08)
    print("R$ %.2f"%x)
else:
    x = (a-4500)*.28+ (1500*.18)+(1000.00*.08)
    print("R$ %.2f"%x)