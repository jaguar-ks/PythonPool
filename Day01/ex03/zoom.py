import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from load_image import ft_load
import sys
from skimage import color


def zoom_img(img: np.ndarray, factor: int) -> np.ndarray:
    """
    Zooms in on an image and performs additional operations.

    Args:
        img (np.ndarray): The input image.
        factor (int): The zoom factor.

    Returns:
        np.ndarray: The zoomed and processed image.

    Raises:
        Exception: If an error occurs during the zooming or
        processing of the image.
    """
    try:
        n_img: np.ndarray = sp.ndimage.zoom(img, zoom=(factor, factor, 1.0))
        n_img = n_img[300:1000, 900:1600]
        n_img = color.rgb2gray(n_img)
        return n_img
    except Exception as e:
        print('Error:', e)
        return None


def displayImages(imgs: list[np.ndarray]) -> None:
    """
    Display a list of images.

    Args:
        imgs (list[np.ndarray]): A list of NumPy arrays representing images.

    Returns:
        None
    """
    try:
        fig, axes = plt.subplots(1, len(imgs), figsize=(10, 10))
        for i, img in enumerate(imgs):
            axes[i].imshow(img, cmap='gray')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalid number of arguments')
        img = ft_load(sys.argv[1])
        zoomed = zoom_img(img, factor=1.5)
        print('The shape of the zoomed image is:', zoomed.shape)
        displayImages([img, zoomed])
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
