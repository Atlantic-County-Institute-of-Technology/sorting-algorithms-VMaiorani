import random

# Gets a random numbers
numbers = [random.randint(1, 100) for i in range(10)]
n = len(numbers)
def print_sort(numbers):
    for i in range(n-1):
        Min_inx = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[Min_inx]:

                Min_idx = j
        numbers[i], numbers[Min_inx] = numbers[Min_inx], numbers[i]


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]

    print("Original array: ", end="")
    print_array(arr)

    print_sort(numbers)

    print("Sorted array: ", end="")
    print_array(arr)
