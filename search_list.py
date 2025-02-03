from ordered_list import get_ordered_list

def search_ordered_list(lst, target):
    """
    Searches for the target integer in an ordered version of the list.
    
    Parameters:
      - lst: A list of integers.
      - target: The integer value to search for.
      
    This function:
      1. Calls get_ordered_list() to sort the provided list.
      2. Uses binary search to check whether 'target' occurs in the sorted list.
      
    Returns:
      - True if target is found in the list.
      - False otherwise.
    """
    # Order the list by calling the helper function.
    sorted_lst = get_ordered_list(lst)
    
    # Perform a binary search on the sorted list.
    low, high = 0, len(sorted_lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return True  # Found the target
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False  # Target not found