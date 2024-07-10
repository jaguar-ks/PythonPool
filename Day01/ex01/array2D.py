import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a list of elements from the given start index to the given end index.

    Args:
        family (list): The list of elements to be sliced.
        start (int): The start index of the slice.
        end (int): The end index of the slice.

    Returns:
        list: The sliced list of elements.

    Raises:
        ValueError: If the list is empty.
        ValueError: If the start index is greater than the end index.
    """
    try:
        if not family:
            raise ValueError("The list is empty.")
        r = np.array(family)
        print('My shape is:', r.shape)
        if start < 0:
            start = r.shape[0] + start
        if end < 0:
            end = r.shape[0] + end
        if start > end:
            raise ValueError("The start index is greater than the end index.")
        print('My new shape is:', r[start:end].shape)
        return r[start:end].tolist()
    except Exception as e:
        print(f"Error: {e}")

# family = [[1.80, 78.4],
# [2.15, 102.7],
# [2.10, 98.5],
# [1.88, 75.2]]
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))
