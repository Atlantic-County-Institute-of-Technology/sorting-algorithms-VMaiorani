import random

# Gets a random numbers
numbers = [random.randint(1, 100) for i in range(10)]

# every time we are in the total amount of numbers range
for i in range(len(numbers)):
    j = i
    # while the range of numbers is greater than 0 and is less than the range value is less than the one behind it switch the numbers
    while j > 0 and numbers[j-1] > numbers[j]:
        temp = numbers[j]
        numbers[j] = numbers[j-1]
        numbers[j-1] = temp
        j = j-1
    print(numbers)

