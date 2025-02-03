# Example usage
# Define a list in your code and search for a target value.

from search_list import search_ordered_list

sample_list = [12, 5, 8, 20, 7, 12, 15]
target_number = 55
found = search_ordered_list(sample_list, target_number)
print(f"Is {target_number} in {sorted(sample_list)}? {found}")
   
