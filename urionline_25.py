x = float(input())
if x > 0:
    print("Fora de intervalo")
elif x > 0 & x <= 25 :
    print("Intervalo [0,25]")
elif x >25 & x <=50 :
    print("Intervalo (25,50]")
elif x > 50 & x <= 75 :
    print("Intervalo [50,75]")
elif x >75 & x <= 100 :
    print("Intervalo (75,100]")
