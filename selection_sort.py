import random

# Gets a random numbers
numbers = [random.randint(1, 100) for i in range(10)]
print("Inital order: "+str(numbers))
def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


size = len(numbers)
selectionSort(numbers, size)