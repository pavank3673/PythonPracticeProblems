from sys import argv
from math import pow

t = int(argv[1])
v = int(argv[2])

if abs(t) > 50 :
    print("absolute temperature should be less than 50")
elif (v > 120 or v < 3):
    print("wind speed range between 3 and 120")
else:
    w = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * pow(v,0.16)

    print(f"wind chill {w}")