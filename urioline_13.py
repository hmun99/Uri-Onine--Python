pi = 3.14159
array = [float(x) for x in input().split()]
tri = array[0]*array[2]*.5
cir = pi*array[2]*array[2]
trap = (array[0]+array[1])*.5*array[2]
sqr = array[1]*array[1]
rec = array[0]*array[1]
print("TRIANGULO: %.3f"%tri)
print("CIRCULO: %.3f"%cir)
print("TRAPEZIO: %.3f"%trap)
print("QUADRADO: %.3f"%sqr)
print("RETANGULO: %.3f"%rec)