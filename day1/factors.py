def prime_no(num):
    i = 1
    count = 0
    while(i <= num):
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        return True
    else:
        return False

n = int(input("Number to find the prime factors : "))
if n < 2:
    print("Cannot find factors for number")
else:
    i = 1
    while(i * i <= n):
        if n % i == 0:
            flag = prime_no(i)
            if flag == True:
                print(i)
        i += 1
    



    