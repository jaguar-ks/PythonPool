from S1E9 import Character, Stark

class Baratheon(Character):
    """
    Represents a character from the Baratheon family.
    Inherits from the Character class.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
    Initializes a Baratheon object.

    Args:
        first_name (str): The first name of the Baratheon.
        is_alive (bool, optional): Indicates if the baratheon is alive. Defaults to True.
        """
        self.family_name = "Baratheon"
        self.hair = "dark"
        self.eyes = "brown"
        self.first_name = first_name
        self.is_alive = is_alive
    
    def changeHealthState(self):
        """
    Toggle the health state of the object.

    This method changes the value of the `is_alive` attribute to its opposite value.
    If the object is currently alive, it will be marked as dead, and vice versa.
        """
        self.is_alive = not self.is_alive



class Lannister(Character):
    """
    Represents a character from the Lannister family.
    Inherits from the Character class.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
    Initializes a Lannister object.

    Args:
        first_name (str): The first name of the Lannister.
        is_alive (bool, optional): Indicates if the Lannister is alive. Defaults to True.
        """
        self.family_name = "Lannister"
        self.hair = "light"
        self.eyes = "blue"
        self.first_name = first_name
        self.is_alive = is_alive
    
    def changeHealthState(self):
        """
    Toggle the health state of the object.

    This method changes the value of the `is_alive` attribute to its opposite value.
    If the object is currently alive, it will be marked as dead, and vice versa.
        """
        self.is_alive = not self.is_alive
    
    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True) -> "Lannister":
        """
    Create a new Lannister object.

    Args:
        first_name (str): The first name of the Lannister.
        is_alive (bool, optional): Whether the Lannister is alive or not. Defaults to True.

    Returns:
        Lannister: The newly created Lannister object.
        """
        return cls(first_name, is_alive)

# if __name__ == '__main__':
#     Robert = Baratheon("Robert")
#     print(Robert.__dict__)
#     print(Robert.__str__)
#     print(Robert.__repr__)
#     print(Robert.is_alive)
#     Robert.die()
#     print(Robert.is_alive)
#     print(Robert.__doc__)
#     print("---")
#     Cersei = Lannister("Cersei")
#     print(Cersei.__dict__)
#     print(Cersei.__str__)
#     print(Cersei.is_alive)
#     print("---")
#     Jaine = Lannister.create_lannister("Jaine", True)
#     print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
