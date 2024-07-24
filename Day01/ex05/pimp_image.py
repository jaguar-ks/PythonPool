import numpy as np
import matplotlib.pyplot as plt
import sys
from load_image import ft_load


def ft_invert(img: np.array) -> np.array:
    try:
        pass
    except Exception as e:
        print('Error:', e)
        return None


def ft_red(img: np.array) -> np.array:
    try:
        pass
    except Exception as e:
        print('Error:', e)
        return None


def ft_green(img: np.array) -> np.array:
    try:
        pass
    except Exception as e:
        print('Error:', e)
        return None


def ft_blue(img: np.array) -> np.array:
    try:
        pass
    except Exception as e:
        print('Error:', e)
        return None


def ft_gray(img: np.array) -> np.array:
    try:
        pass
    except Exception as e:
        print('Error:', e)
        return None


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of arguments')
        img = ft_load(sys.argv[1])
        
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
