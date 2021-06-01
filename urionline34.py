a,b,c,d = list(map(int,input().split()))
x = (((c*60)+d)-((a*60)+b))
if x <= 0:
    x = x+(24*60)
y = x//60
z = x%60
print(f"O JOGO DUROU {y} HORA(S) E {z} MINUTO(S)")