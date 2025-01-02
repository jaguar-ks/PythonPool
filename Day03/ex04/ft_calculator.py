import numpy as np

class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
    Calculates the dot product of two vectors.

    Args:
        V1 (list[float]): The first vector.
        V2 (list[float]): The second vector.

    Returns:
        None. Prints the dot product of the two vectors.
        """
        print("Dot product is:", np.dot(V1, V2))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
    Adds two vectors and prints the result.

    Parameters:
        V1 (list[float]): The first vector.
        V2 (list[float]): The second vector.

    Returns:
        None
        """
        print("Add Vector is:", np.add(V1, V2).tolist())

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
    Subtracts two vectors element-wise and prints the result.

    Args:
        V1 (list[float]): The first vector.
        V2 (list[float]): The second vector.

    Returns:
        None
        """
        print("Sous Vector is:", np.subtract(V1, V2).tolist())

# if __name__ == "__main__":
#     v1 = [5.0, 10.0, 2.0]
#     v2 = [2.0, 4.0, 3.0]
#     calculator.dotproduct(v1, v2)
#     calculator.add_vec(v1, v2)
#     calculator.sous_vec(v1, v2)
