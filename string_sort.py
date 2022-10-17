# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-12-2022
# Description: Modified insertion sort to sort list of strings instead of numbers. Returns the list in alphabetical
# order.

def string_sort(string_list):
    """
  Sorts a_list in ascending order
  """
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1
        while pos >= 0 and value < string_list[pos]:
            string_list[pos + 1] = string_list[pos]
            pos -= 1
        string_list[pos + 1] = value
