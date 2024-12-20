year = input("Enter year : ")
if len(year) < 4:
    print("Ensure it is a 4 digit number")
else:
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap year")
    else:
        print(f"{year} is not a Leap year")