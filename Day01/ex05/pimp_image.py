import numpy as np
import matplotlib.pyplot as plt
import sys
from load_image import ft_load


def ft_invert(img: np.array) -> np.array:
    """
    Invert the colors of an image.

    Args:
        img (np.array): A NumPy array representing the input image.

    Returns:
        np.array: A NumPy array representing the inverted image,
        or None if an error occurs.
    """
    try:
        n_img = 255 - img.copy()
        return n_img
    except Exception as e:
        print('Error:', e)
        return None


def ft_red(img: np.array) -> np.array:
    """
    Convert an image to red scale by keeping only the red channel.

    Args:
        img (np.array): A NumPy array representing the input image.

    Returns:
        np.array: A NumPy array representing the red-scaled image,
        or None if an error occurs.
    """
    try:
        n_img = img.copy() * [1, 0, 0]
        return n_img
    except Exception as e:
        print('Error:', e)
        return None


def ft_green(img: np.array) -> np.array:
    """
    Convert an image to green scale by keeping only the green channel.

    Args:
        img (np.array): A NumPy array representing the input image.

    Returns:
        np.array: A NumPy array representing the green-scaled image,
        or None if an error occurs.
    """
    try:
        n_img = img.copy()
        n_img[:, :, 0] = 0
        n_img[:, :, 2] = 0
        return n_img
    except Exception as e:
        print('Error:', e)
        return None


def ft_blue(img: np.array) -> np.array:
    """
    Convert an image to blue scale by keeping only the blue channel.

    Args:
        img (np.array): A NumPy array representing the input image.

    Returns:
        np.array: A NumPy array representing the blue-scaled image,
        or None if an error occurs.
    """
    try:
        n_img = img.copy()
        n_img[:, :, 0] = 0
        n_img[:, :, 1] = 0
        return n_img
    except Exception as e:
        print('Error:', e)
        return None


def ft_gray(img: np.array) -> np.array:
    """
    Convert an RGB image to grayscale using the average method.

    Args:
        img (np.array): A NumPy array representing the input image.

    Returns:
        np.array: A NumPy array representing the grayscale image,
        or None if an error occurs.
    """
    try:
        gray_scale = (img[:, :, 0] / 3 + img[:, :, 1] / 3 + img[:, :, 2] / 3)
        n_img = img.copy()
        n_img[:, :, 0] = gray_scale
        n_img[:, :, 1] = gray_scale
        n_img[:, :, 2] = gray_scale
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
            axes[i].axis('off')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print('Error:', e)


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalide number of arguments')
        img = ft_load(sys.argv[1])
        imgs: list[np.array] = []
        imgs.append(ft_invert(img))
        imgs.append(ft_red(img))
        imgs.append(ft_green(img))
        imgs.append(ft_blue(img))
        imgs.append(ft_gray(img))
        displayImages(imgs)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
