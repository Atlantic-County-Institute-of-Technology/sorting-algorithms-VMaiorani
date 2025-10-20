import random
# import time



# Gets a random numbers
numbers = [random.randint(1, 100) for i in range(10)]
print("Initial order: "+str(numbers))
# start_time = time.time()
def selectionSort(array, size):
    # total_loops = 0
    # total_actions = 0

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    #     total_actions += 1
    # total_loops += 1
    #
    # print(total_loops)
    # print(total_actions)

# end_time = time.time()
# elapsed_time = end_time - start_time
# rounded_time = round(elapsed_time,4)
# print(rounded_time)
size = len(numbers)
selectionSort(numbers, size)