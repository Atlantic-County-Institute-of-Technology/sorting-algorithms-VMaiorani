
print("----chose an option for sorting----\n"
      "1. Bubble sort\n"
      "2. Insertion sort\n"
      "3. Selection sort\n"
      "4. Configuration\n"
      "-----------------------------------")

SortSelect = int(input("[-] Please select a sort you want to use:"))

if SortSelect == 1:
      from bubble_sort import numbers
      from bubble_sort import total_loops
      from bubble_sort import total_actions
      print("Sorted order: " + str(numbers))
      print("total loops: " + str(total_loops))
      print("total sorting actions: " + str(total_actions))


elif SortSelect == 2:
      from insertion_sort import numbers
      print("Sorted order: " + str(numbers))

elif SortSelect == 3:
      from selection_sort import numbers
      print("Sorted order: " + str(numbers))

elif SortSelect == 4:
      print("you have selected configuration you can select from the following options to change how each sort will change.")
      print("----Options----\n"
            "1. Minimum range\n"
            "2. Maximum range\n")

else:
      print("that's not an option pls try again")