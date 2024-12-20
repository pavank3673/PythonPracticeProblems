n = int(input("Enter the harmonic value n : "))
if n == 0:
    print("Ensure n not equal to zero")
else:
    nth_harmonic = 0.0;
    for i in range(1, n + 1):
        nth_harmonic += (1 / i)
    print(f"The nth harmonic value {nth_harmonic}")