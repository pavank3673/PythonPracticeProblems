from math import sqrt

a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
c = int(input("Enter c value : "))

delta = (b * b) - (4 * a * c)
root_one = (-b + sqrt(abs(delta))) / (2 * a)
root_two = (-b - sqrt(abs(delta))) / (2 * a)

print(f"root 1 of x {root_one}")
print(f"root 2 of x {root_two}")