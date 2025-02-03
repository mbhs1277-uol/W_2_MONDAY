def get_ordered_list(lst=None):
    """
    Returns an ordered (sorted) list of integers.
    
    If lst is provided, it returns the sorted version of that list.
    If lst is None, it requests the user to input a list of integers (comma-separated),
    then parses and returns the sorted list.
    """
    if lst is None:
        user_input = input("Enter a list of integers separated by commas: ")
        # Convert the input string into a list of integers
        lst = [int(x.strip()) for x in user_input.split(",")]
    return sorted(lst)





