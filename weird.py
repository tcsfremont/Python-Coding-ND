import sys
n = int(sys.argv[1])

if n % 2 == 1:

    print("weird")

elif n >= 2 and n <= 5:

    print("not weird")

elif n in range(6,21):
    print("weird") 
else:
    print("not weird")

#x % y = remainder(x / y)
