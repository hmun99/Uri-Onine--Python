a,b,c,d = list(map(float, input().split()))
y = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / (2 + 3 + 4 + 1)
print("Media: %.1f"%y)
if y >= 7.0 :
  print("Aluno aprovado.")
elif y >= 5.0:
     x = float(input())
     print("Aluno em exame.")
     print("Nota do exame: %.1f"%x)
     z = (x+y) / 2
     if (z >= 5.0):
      print("Aluno aprovado.")
      print("Media final: %.1f"%z)
     elif z <= 4.9:
      print("Aluno reprovado.")
      print("Media final: %.1f"%z)
else:
    print("Aluno reprovado.\n")

