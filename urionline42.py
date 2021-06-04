a,b = input().split()
b = int(b)
c,d,e = map(int,input().split(":"))

a1,b1 = input().split()
b1 = int(b1)
c1,d1,e1 = map(int,input().split(":"))

s1 = ((b*86400)+(c*3600)+(d*60)+e)
s2 = ((b1*86400)+(c1*3600)+(d1*60)+e1)
s = s2-s1
if s<0:
 s = s+86400
x = s//86400
m = s%86400
y = m//3600
n = m%3600
w = n//60
z = n%60
print("%d dia(s)"%x)
print("%d hora(s)"%y)
print("%d minuto(s)"%w)
print("%d segundo(s)"%z)