a,b = list(map(int, input().split()))
if a == 1:
    x = b * 4.00
    print("Total: R$ %.2f" % x)
elif a == 2:
    x = b * 4.50
    print("Total: R$ %.2f" % x)
elif a == 3:
    x = b * 5.00
    print("Total: R$ %.2f" % x)
elif a == 4:
    x = b * 2.00
    print("Total: R$ %.2f" % x)
elif a == 5:
    x = b * 1.50
    print("Total: R$ %.2f" % x)