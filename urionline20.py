n = int(input())
h = n/3600
x = n%3600
m = x/60
s = x%60
print("{}:{}:{}".format(int(h),int(m),(s)))