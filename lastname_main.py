from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
import random

MinimumRange = 78
MaximumRange = 100
Range = 20

while True:
    # import random
    (print(MinimumRange))

    print("----chose an option for sorting----\n"
          "1. Bubble sort\n"
          "2. Insertion sort\n"
          "3. Selection sort\n"
          "4. Configuration\n"
          "-----------------------------------")

    SortSelect = int(input("[-] Please select a sort you want to use:"))

    if SortSelect == 1:
        numbers = [random.randint(MinimumRange, MaximumRange) for i in range(Range)]
        numbers, total_loops, total_actions, rounded_time = bubble_sort(numbers)

        print(f"---------------------------------------------------------------\n"
              f"---You selected bubble sort---\n"
              f"Sorted order: {numbers}\n"
              f"Total loops: {total_loops}\n"
              f"Total Sorting Actions: {total_actions}\n"
              f"Total Elapsed Time: {rounded_time}\n"
              f"---------------------------------------------------------------")


    elif SortSelect == 2:
        numbers = [random.randint(MinimumRange, MaximumRange) for i in range(Range)]
        numbers, total_loops, total_actions, rounded_time = insertion_sort(numbers)

        print(f"---------------------------------------------------------------\n"
              f"---You selected insertion sort---\n"
              f"Sorted order: {numbers}\n"
              f"Total loops: {total_loops}\n"
              f"Total Sorting Actions: {total_actions}\n"
              f"Total Elapsed Time: {rounded_time}\n"
              f"---------------------------------------------------------------")

    elif SortSelect == 3:
        numbers = [random.randint(MinimumRange, MaximumRange) for i in range(Range)]
        numbers, lc, sc, elapsed_time = selection_sort(numbers)

        print(f"---------------------------------------------------------------\n"
              f"---You selected selection sort---\n"
              f"Sorted order: {numbers}\n"
              f"Total loops: {lc}\n"
              f"Total Sorting Actions: {sc}\n"
              f"Total Elapsed Time: {elapsed_time}\n"
              f"---------------------------------------------------------------")



    elif SortSelect == 4:
        print(
            "you have selected configuration you can select from the following options to change how each sort will change.")
        print("----Options----\n"
              "1. Minimum range\n"
              "2. Maximum range\n"
              "3. Total Amount of Number sorted"
              "4. Exit \n")
        ConfigSelect = int(input("[-] Please select an option you want to uses: "))
        if ConfigSelect == 1:
            print("---------------You may select your minimum range(default = 1)---------------\n"
                  "---Important things to know---\n"
                  "1. Your input must be a positive integer\n"
                  "2. You input must be less than your maximum range\n"
                  "3. No 67 at all")
        MinimumRange = int(input("[-] Please select the minimum range you would like:"))
        print(MinimumRange)


    else:
        print("that's not an option pls try again")
