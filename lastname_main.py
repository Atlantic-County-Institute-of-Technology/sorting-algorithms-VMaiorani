
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
      from bubble_sort import rounded_time

elif SortSelect == 2:
      from insertion_sort import numbers
      from insertion_sort import total_loops
      from insertion_sort import total_actions
      from insertion_sort import rounded_time

elif SortSelect == 3:
      from selection_sort import numbers
      from selection_sort import total_loops
      from selection_sort import total_actions
      from selection_sort import rounded_time

elif SortSelect == 4:
      print("you have selected configuration you can select from the following options to change how each sort will change.")
      print("----Options----\n"
            "1. Minimum range\n"
            "2. Maximum range\n")

else:
      print("that's not an option pls try again")

# What will be printed after the selection process
print(f"---------------------------------------------------------------\n"
      f"Sorted order: {numbers}\n"
      f"Total loops: {total_loops}\n"
      f"Total Sorting Actions: {total_actions}\n"
      f"Total Elapsed Time: {rounded_time}\n"
      f"---------------------------------------------------------------" )
