import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from load_image import ft_load
import sys
import imageio.v3 as iio


def zoom_img(img: np.ndarray, factor: int) -> np.ndarray:
    try:
        f = img
        # iio.imwrite('/Users/faksouss/Desktop/PythonPool/Day01/ex03/face.png', f)
        n_f = sp.ndimage.zoom(f, zoom=(1.5, 1.5, 1.0))
        n_f = n_f[100:900, 100:900]
        plt.imshow(n_f, vmin=0, vmax=255)
        plt.show()
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