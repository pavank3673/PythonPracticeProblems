n = int(input("Enter number of integer : "))
arr = [0] * n;

print("Enter integer input array : ")
for i in range(n):
    arr[i] = int(input())

result = []

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                result.append([i, j, k])

print(result)
print(len(result))
