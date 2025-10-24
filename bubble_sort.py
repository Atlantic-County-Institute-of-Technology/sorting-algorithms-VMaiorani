import random
import time

# x = 1
# y = 100


# numbers = [random.randint(x, y) for i in range(10)]
# print("Initial Order: " + str(numbers))

def bubble_sort(numbers):
    total_loops = 0
    total_actions = 0
    start_time = time.time()
    for i in range(len(numbers)-1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
                total_actions += 1
        total_loops += 1
    end_time = time.time()
    elapsed_time = end_time - start_time
    rounded_time = round(elapsed_time, 4)
    return numbers, total_loops, total_actions, rounded_time
# print(rounded_time)
# print(numbers)