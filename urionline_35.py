a = float(input())
if(a >= 0 and a <= 400.00):
    x = a*.15
    y = x+a
    print("Novo salario: %.2f"%y)
    print("Reajuste ganho: %.2f" %x)
    print("Em percentual: 15%")
elif(a >= 400.01 and a <= 800.00):
    x = a*.12
    y = x+a
    print("Novo salario: %.2f"%y)
    print("Reajuste ganho: %.2f" %x)
    print("Em percentual: 12%")
elif(a >= 800.01 and a <= 1200.00):
    x = a*.10
    y = x+a
    print("Novo salario: %.2f"%y)
    print("Reajuste ganho: %.2f" %x)
    print("Em percentual: 10%")
elif(a >= 1200.01 and a <= 2000.00):
    x = a*.07
    y = x+a
    print("Novo salario: %.2f"%y)
    print("Reajuste ganho: %.2f" %x)
    print("Em percentual: 7%")
elif(a >= 2000.01):
    x = a*.04
    y = x+a
    print("Novo salario: %.2f"%y)
    print("Reajuste ganho: %.2f" %x)
    print("Em percentual: 4%")
