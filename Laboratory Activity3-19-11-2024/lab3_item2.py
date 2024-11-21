def checkifperfect(number):
    divisors = sum(i for i in range(1, number) if number % i == 0)
    return number == divisors

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if checkifperfect(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")