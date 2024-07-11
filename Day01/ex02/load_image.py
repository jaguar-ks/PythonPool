import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    try:
        img = Image.open(path)
        arr = np.array(img)
        print('The shape of the image is:', arr.shape)
        print(arr)
    except Exception as e:
        print('Error:', e)
        return None

# if __name__ == '__main__':
#     ft_load(sys.argv[1])
