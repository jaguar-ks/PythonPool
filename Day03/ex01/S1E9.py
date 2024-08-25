from abc import ABC, abstractmethod


class Character (ABC):
    """
    Abstract class representing a character with a
    first name and health status.

    Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): The health status of the character,
        True if alive, False otherwise.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
    Initializes a new instance of the Character class.

    Args:
        first_name (str): The first name of the object.
        is_alive (bool, optional): Indicates whether the
        object is alive or not. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def changeHealthState(self):
        """
        Abstract method to change the health state.
        This method should be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    Represents a character from the Stark family.
    Inherits from the Character class.
    """

    def changeHealthState(self):
        """
    Changes the health state of the Stark character.
    If the character is alive, it sets the is_alive attribute to False.
    If the character is dead, it sets the is_alive attribute to True.
        """
        self.is_alive = not self.is_alive

    def die(self):
        """
    Kills the Stark character.
        """
        if self.is_alive:
            self.changeHealthState()


# if __name__ == '__main__':
#     Ned = Stark("Ned")
#     print(Ned.__dict__)
#     print(Ned.is_alive)
#     Ned.die()
#     print(Ned.is_alive)
#     print(Ned.__doc__)
#     print(Ned.__init__.__doc__)
#     print(Ned.die.__doc__)
#     print("---")
#     Lyanna = Stark("Lyanna", False)
#     print(Lyanna.__dict__)
