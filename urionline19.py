note = int(input())
print(note)
print("{} nota(s) de R$ 100,00".format(int(note/100)))
x = note%100

print("{} nota(s) de R$ 50,00".format(int(x/50)))
x = x%50

print("{} nota(s) de R$ 20,00".format(int(x/20)))
x = x%20

print("{} nota(s) de R$ 10,00".format(int(x/10)))
x = x%10

print("{} nota(s) de R$ 5,00".format(int(x/5)))
x = x%5

print("{} nota(s) de R$ 2,00".format(int(x/2)))
x = x%2

print("{} nota(s) de R$ 1,00".format(int(x/1)))


