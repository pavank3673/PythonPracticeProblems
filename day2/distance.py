from sys import argv
import math

x = int(argv[1])
y = int(argv[2])

distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

print(f"distance {distance}")

