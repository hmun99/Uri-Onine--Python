note = float(input())
print("NOTAS:")

print("{} nota(s) de R$ 100.00".format(int(note/100)))
x = note%100

print("{} nota(s) de R$ 50.00".format(int(x/50)))
x = x%50

print("{} nota(s) de R$ 20.00".format(int(x/20)))
x = x%20

print("{} nota(s) de R$ 10.00".format(int(x/10)))
x = x%10

print("{} nota(s) de R$ 5.00".format(int(x/5)))
x = x%5

print("{} nota(s) de R$ 2.00".format(int(x/2)))
x = x%2

print("MOEDAS:")

print("{} moeda(s) de R$ 1.00".format(int(x)))
x = x%1

print("{} moeda(s) de R$ 0.50".format(int(x/0.5)))
x = x% 0.50

print("{} moeda(s) de R$ 0.25".format(int(x/0.25)))
x = x% 0.25

print("{} moeda(s) de R$ 0.10".format(int(x/0.10)))
x = x% 0.10

print("{} moeda(s) de R$ 0.05".format(int(x/0.05)))
x = x% 0.05

print("{} moeda(s) de R$ 0.01".format(int(x/0.01)))
