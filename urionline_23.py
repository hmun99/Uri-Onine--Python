a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = a+b
y = c+d
if(b>c & d>a)&(x<y)&(c>0 & d>0)&(a%2 == 0):
    print("Valores aceitos")
else:
    print("Valores not aceitos")