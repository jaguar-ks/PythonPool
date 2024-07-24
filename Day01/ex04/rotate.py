from load_image import ft_load
import sys
import numpy as np
from matplotlib import pyplot as plt
# from skimage import color


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


def rotateImage(img: np.ndarray) -> np.ndarray:
    """
    Rotates the given image by 90 degrees clockwise.

    Args:
        img (np.ndarray): The input image as a NumPy array.

    Returns:
        np.ndarray: The rotated image as a NumPy array.

    Raises:
        None.

    """
    try:
        n_img = [[img[j][i] for j in range(len(img))]
                 for i in range(len(img[0]))]
        return n_img
    except Exception as e:
        print('Error:', e)
        return None


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('Invalid number of arguments')
        img = ft_load(sys.argv[1])
        # img = color.rgb2gray(img)
        n_img = rotateImage(img)
        displayImages([img, n_img])
    except Exception as e:
        print('Error:', e)
        sys.exit(1)
