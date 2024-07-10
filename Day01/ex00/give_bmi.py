import numpy as np


def give_bmi(hight: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI (Body Mass Index) for a given list of
    heights and weights.

    Args:
        hight (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list of BMIs corresponding to the given
        heights and weights.

    Raises:
        ValueError: If the lists are empty or not of the same length.

    """
    try:
        if not hight or not weight:
            raise ValueError("The lists are empty.")
        if len(hight) != len(weight):
            raise ValueError("The lists are not of the same length.")
        hight = np.array(hight)
        weight = np.array(weight)
        bmi = weight / (hight ** 2)
        return bmi.tolist()
    except Exception as e:
        print(f"Error: {e}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if each BMI value in the given list is greater than
    the specified limit.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The limit to compare the BMI values against.

    Returns:
        list[bool]: A list of boolean values indicating whether each BMI
        value is greater than the limit.
    """
    r: list[bool] = []
    for i in bmi:
        r.append(i > limit)
    return r

# height = [2.71, 1.15]
# weight = [165.3, 38.4]
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))
