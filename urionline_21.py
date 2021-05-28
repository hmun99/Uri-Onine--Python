n = int(input())
year = n/365
print("{} ano(s)".format(int(year)))
year = n%365
months = year/30
days = year%30
print("{} mes(es)".format(int(months)))
print("{} dia(s)".format(int(days)))