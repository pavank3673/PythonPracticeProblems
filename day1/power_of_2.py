from sys import argv

n = int(argv[1])
if n < 0 or n >= 31:
    print("Range of n between 0 and 31")
else: 
    for i in range(n + 1):
        print(f"2 ^ {i} = {2 ** i}")