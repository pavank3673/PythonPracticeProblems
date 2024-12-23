from random import randint


def generate_random_number(value):
    count = 0
    flag = False
    while(flag == False):
        random_number = randint(1, value)
        count += 1
        if value == random_number:
            flag = True
    return count

n = input("Enter n distinct coupon numbers : ")
distinct_numbers = set(n.split())

random_count = 0

for ele in distinct_numbers:
    random_count += generate_random_number(int(ele))

print(random_count)