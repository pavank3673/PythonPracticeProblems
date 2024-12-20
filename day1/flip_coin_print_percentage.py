from random import uniform

flip_coin_count = int(input("The number of times to Flip Coin : "))

if flip_coin_count > 0:
    heads_count = 0
    tails_count = 0

    for i in range(flip_coin_count):
        random_no = uniform(0.0, 1.0)
        if random_no < 0.5:
            tails_count+=1
        else:
            heads_count+=1

    print(f"Percentage of Head : {(heads_count / flip_coin_count) * 100}%")
    print(f"Percentage of Tail : {(tails_count / flip_coin_count) * 100}%")

else:
    print("Ensure it is positive integer")