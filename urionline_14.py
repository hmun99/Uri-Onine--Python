x = [int(y) for y in input().split()]
maxA = (x[0]+x[1]+abs(x[0]-x[1]))/2
maxB = (maxA+x[2]+abs(maxA-x[2]))/2
print("%i eh o maior"%maxB)