def ft_filter(func, lst: list) -> list:
    """
    Filters the elements of a list based on a given function.

    Args:
        func: A function that takes an element of the list as
        input and returns a boolean value.
        lst: The list to be filtered.

    Returns:
        A new list containing only the elements from the original
        list for which the function returns True.
    """
    return [i for i in lst if func(i)]
