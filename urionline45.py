e = 0
o = 0
p = 0
n = 0
for i in range(0,5):
    x = int(input())
    if x%2 == 0:
     e = e+1
    else:
     o = o+1
    if x > 0:
     p = p+1
    elif x<0:
      n = n+1
print("%d valor(es) par(es)"%e)
print("%d valor(es) impar(es)"%o)
print("%d valor(es) positivo(s)"%p)
print("%d valor(es) negativo(s)"%n)