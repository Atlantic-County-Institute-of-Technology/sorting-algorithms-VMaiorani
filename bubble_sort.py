import random
import time

total_loops = 0
total_actions = 0
numbers = [random.randint(1, 100) for i in range(10)]
print("Initial Order: " + str(numbers))

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
# print(rounded_time)
# print(numbers)