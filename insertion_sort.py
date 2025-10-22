import random
import time
# from lastname_main import MinimumRange, MaximumRange, Range
total_loops = 0
total_actions = 0

# Gets a random numbers
numbers = [random.randint(1, 100) for i in range(10)]

# every time we are in the total amount of numbers range
start_time = time.time()
for i in range(len(numbers)):
    j = i
    # while the range of numbers is greater than 0 and is less than the range value is less than the one behind it switch the numbers
    while j > 0 and numbers[j-1] > numbers[j]:
        temp = numbers[j]
        numbers[j] = numbers[j-1]
        numbers[j-1] = temp
        j = j-1
        # print(numbers)
        total_actions += 1
    total_loops += 1
#     added extra stuff to track loops, actions, and time to complete the sort
end_time = time.time()
elapsed_time = end_time - start_time
rounded_time = round(elapsed_time, 4)
# print(rounded_time)
# print(numbers)

