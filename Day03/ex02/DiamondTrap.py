from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    """
    Represents a king character.
    """

    def set_eyes(self, color: str):
        """
    Set the color of the eyes for the DiamondTrap.

    Args:
        color (str): The color of the eyes.

    Returns:
        None
        """
        self.eyes = color
    
    def set_hairs(self, color: str):
        """
    Set the color of the DiamondTrap's hair.

    Parameters:
        color (str): The color of the hair.

    Returns:
        None
        """
        self.hair = color

    def get_eyes(self) -> str:
        """
    Returns the value of the 'eyes' attribute.

    Returns:
        str: The value of the 'eyes' attribute.
        """
        return self.eyes
    
    def get_hairs(self) -> str:
        """
    Returns the hair attribute of the DiamondTrap object.

    Returns:
        str: The hair attribute of the DiamondTrap object.
        """
        return self.hair

if __name__ == "__main__":
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)
