import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from scipy.ndimage import zoom
import sys


def zoom_img(img: np.ndarray, factor: int) -> np.ndarray:
    try:
        pass
    except Exception as e:
        print('Error:', e)
        return None


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalid number of arguments')
        img = ft_load(sys.argv[1])
        zoomed = zoom_img(img, factor=2)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)