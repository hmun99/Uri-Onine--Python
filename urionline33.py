a,b = map(int,input().split())
c = b-a
if(c<0):
    c = 24+c
    print("O JOGO DUROU %d HORA(S)"%c)
elif (a == b):
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU %d HORA(S)"%c)
