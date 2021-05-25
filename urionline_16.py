import math
x1,y1 = list(map(float, input().split()))
x2,y2 = list(map(float, input().split()))
p1 = (x2-x1)*(x2-x1)
p2 = (y2-y1)*(y2-y1)
p = math.sqrt(p1+p2)

print("%.4f"%p)