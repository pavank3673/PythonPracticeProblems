def print_array(ar):
    for i in range(m):
        for j in range(n):
            print(ar[i][j], end=' ')
        print()

m = int(input("Enter rows : "))
n = int(input("Enter columns :"))

arr = []
for i in range(m):
    arr.append([0] * n)

for x in range(m):
    for y in range(n):
        arr[x][y] = int(input(f"Enter {x} row {y} column value : "))

print_array(arr)