
class calculator:
    """
    A class representing a calculator.

    Attributes:
    - vector: A list of floats representing the vector.

    Methods:
    - __init__(self, vector: list[float]): Initializes the calculator with a vector.
    - __add__(self, object) -> None: Adds a value to each element in the vector.
    - __sub__(self, object) -> None: Subtracts a value from each element in the vector.
    - __mul__(self, object) -> None: Multiplies each element in the vector by a value.
    - __truediv__(self, object) -> None: Divides each element in the vector by a value.

    """

    def __init__(self, vector: list[float]):
        self.vector = vector
    
    def __add__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)
    
    def __sub__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)
    
    def __mul__(self, object) -> None:
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)
    
    def __truediv__(self, object) -> None:
        if object != 0:
            for i in range(len(self.vector)):
                self.vector[i] /= object
            print(self.vector)
        else:
            print("Error: Division by zero")

# if __name__ == "__main__":
#     v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v1 + 5
#     print("---")
#     v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v2 * 5
#     print("---")
#     v3 = calculator([10.0, 15.0, 20.0])
#     v3 - 5
#     v3 / 5
