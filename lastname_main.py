import bubble_sort

print("----chose an option for sorting----\n"
      "1. Buble sort\n"
      "2. Insertion sort\n"
      "3. Selection sort\n")

SortSelect = int(input("[-] Please select a sort you want to use:"))

if SortSelect == 1:
      from bubble_sort import numbers
      print(numbers)


elif SortSelect == 2:
      from insertion_sort import numbers
      print(numbers)

elif SortSelect == 3:
      print(6)

else:
      print("that's not an option pls try again")