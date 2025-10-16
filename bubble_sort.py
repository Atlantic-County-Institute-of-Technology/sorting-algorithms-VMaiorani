import random

total_loops = 0
total_actions = 0
numbers = [random.randint(1, 100) for i in range(10)]
print("Initial Order: " + str(numbers))

for i in range(len(numbers)-1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j+1]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp
            total_actions += 1
    total_loops += 1

print(numbers)
print(total_loops)
print(total_actions)