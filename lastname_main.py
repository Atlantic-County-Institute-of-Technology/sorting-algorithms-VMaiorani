from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
import random

MinimumRange = 1
MaximumRange = 100
Range = 20

while True:
    # import random
    (print("current Minimum: " + str(MinimumRange)))
    (print("current Max: " + str(MaximumRange)))
    (print("current Range: " + str(Range)))

    # The selection that they can choose from
    print("----chose an option for sorting----\n"
          "1. Bubble sort\n"
          "2. Insertion sort\n"
          "3. Selection sort\n"
          "4. Configuration\n"
          "-----------------------------------")

    SortSelect = int(input("[-] Please select a sort you want to use:"))

    if SortSelect == 1:
        # gets a random list of numbers
        numbers = [random.randint(MinimumRange, MaximumRange) for i in range(Range)]
        # prints the current numbers before the new sorted numbers are added
        print("current order: " + str(numbers))
        # gets information form the bubble sort to allow us to print them out
        numbers, total_loops, total_actions, rounded_time = bubble_sort(numbers)
        # The printed informationa
        print(f"---------------------------------------------------------------\n"
              f"---You selected bubble sort---\n"
              f"Sorted order: {numbers}\n"
              f"Total loops: {total_loops}\n"
              f"Total Sorting Actions: {total_actions}\n"
              f"Total Elapsed Time: {rounded_time}\n"
              f"---------------------------------------------------------------")


    elif SortSelect == 2:
        # gets numbers
        numbers = [random.randint(MinimumRange, MaximumRange) for i in range(Range)]
        # prints the numbers before the sort
        print("current order: " + str(numbers))
        # grabs information from the sort and then allows them to be printed
        numbers, total_loops, total_actions, rounded_time = insertion_sort(numbers)
        # prints the information in their respective category
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
        print("current order: " + str(numbers))
        print(f"---------------------------------------------------------------\n"
              f"---You selected selection sort---\n"
              f"Sorted order: {numbers}\n"
              f"Total loops: {lc}\n"
              f"Total Sorting Actions: {sc}\n"
              f"Total Elapsed Time: {elapsed_time}\n"
              f"---------------------------------------------------------------")



    elif SortSelect == 4:
        print("---selection---\n"
              "1. minimum\n"
              "2. maximum\n"
              "3. range")
        Select = int(input("[-] Please select what you want to use:"))
        if Select == 1:
            while True:
                print("---select a minimum range---")
                MinimumRange = int(input("[-] Please enter the minimum range you want"))
                if MinimumRange >= MaximumRange:
                    print("You Minimum must be less than your current maximum range, which is: " +str(MaximumRange))
                elif MinimumRange <= 0:
                    print("pls enter a non negative number that is greater than zero!!!")
                elif MinimumRange > 999:
                    print("pls enter a number that isn't over 999!!!")
                else:
                    print("Your new minimum range is: " + str(MinimumRange))
                    break
        if Select == 2:
            while True:
                print("---select a Maximum range---")
                MaximumRange = int(input("[-] Please enter the maximum range you want"))
                if MaximumRange <= MinimumRange:
                    print("You Maximum range must be greater than your current minimum range: " + str(MinimumRange))
                elif MaximumRange <= 0:
                    print("pls enter a non negative number that is greater than zero!!!")
                elif MaximumRange > 1000:
                    print("pls enter a number that isn't over 1000!!!")
                else:
                    print("Your new maximum range is: " + str(MaximumRange))
                    break
        if Select == 3:
            while True:
                print("---Select your new range---")
                Range = int(input("[-] Please enter the maximum range you want"))
                if Range < 10:
                    print("Must be greater than 10 at least")
                elif Range > 1000:
                    print("range must be 1000 or less")
                else:
                    print("Your new maximum range is: " + str(MaximumRange))
                    break

            # finish
            # while True:
                    # print("---------------You may select your minimum range(default = 1)---------------\n"
                    #   "---Important things to know---\n"
                    #   "1. Your input must be a positive integer and greater than 0\n"
                    #   "2. You input must be less than your maximum range\n")
                    # print(MinimumRange)
                    # MinimumRange = int(input("[-] Please select the minimum range you would like:"))
                    # while MinimumRange <= 1:
                    #     MinimumRange = int(input("[-] Please select the minimum range you would like:"))
                    # if MinimumRange < 1:
                    #     print("Error please select a number greater than 1")
                    # elif MinimumRange <= 1000:
                    #     print("thank you for selecting a new minimum range of " + str(MinimumRange))
                    #     break
                    # else:
                    #     print("22")
                    # while you don't have a positve amount or no apples

        # print(MinimumRange)
