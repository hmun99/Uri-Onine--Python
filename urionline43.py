c = 0
s = 0
avg = 0
for i in range(0,6):
    x = float(input())
    if x>0:
      s = s+x
      c = c+1
avg = s/c
print("%d valores positivos"%c)
print("%.1f"%avg)