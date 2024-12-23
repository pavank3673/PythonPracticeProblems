from random import randint


def generate_random_number(value):
    count = 0
    flag = False
    while(flag == False):
        random_number = randint(1, 1000)
        count += 1
        if value == random_number:
            flag = True
    return count

n = input("Enter n distinct coupon numbers : ")
distinct_numbers = n.split()

random_count = 0

for i in range(len(distinct_numbers)):
    distinct_numbers[i] = int(distinct_numbers[i])
    random_count += generate_random_number(distinct_numbers[i])

print(random_count)
