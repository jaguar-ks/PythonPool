import numpy as np
from PIL import Image
# import sys


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
        arr = np.array(img)
        print('The shape of the image is:', arr.shape)
        print(arr)
        return arr
    except Exception as e:
        print('Error:', e)
        return None

# if __name__ == '__main__':
#     ft_load(sys.argv[1])
