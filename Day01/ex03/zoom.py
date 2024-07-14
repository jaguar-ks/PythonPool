from load_image import ft_load
import numpy as np
import sys
from scipy.ndimage import zoom
import matplotlib.pyplot as plt
from PIL import Image



def zoom_image(image_np, zoom_factor):
    if image_np.ndim == 2:  # Grayscale image
        h, w = image_np.shape
        zoomed_image = image_np[int(h*(1-1/zoom_factor)//2):int(h*(1+1/zoom_factor)//2),
                                int(w*(1-1/zoom_factor)//2):int(w*(1+1/zoom_factor)//2)]
    elif image_np.ndim == 3:  # Color image
        h, w, d = image_np.shape
        zoomed_image = image_np[int(h*(1-1/zoom_factor)//2):int(h*(1+1/zoom_factor)//2),
                                int(w*(1-1/zoom_factor)//2):int(w*(1+1/zoom_factor)//2),
                                :]
    else:
        raise ValueError("Unsupported image format")
    
    zoomed_image = Image.fromarray(zoomed_image)
    zoomed_image = zoomed_image.resize((w, h), Image.Resampling.BILINEAR)
    zoomed_image = np.array(zoomed_image)
    
    return zoomed_image

def display_images(original_image, zoomed_image):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(original_image, cmap='gray' if original_image.ndim == 2 else None)
    ax[0].set_title('Original Image')
    ax[0].axis('off')

    ax[1].imshow(zoomed_image, cmap='gray' if zoomed_image.ndim == 2 else None)
    ax[1].set_title('Zoomed Image')
    ax[1].axis('off')

    plt.show()

if __name__ == '__main__':
    try:
        img = ft_load(sys.argv[1])
        if img is None or img.size == 0:
            raise Exception('Error: Image not loaded or empty')
        
        zoom_factor = 0.5  # Adjust the zoom factor as needed
        new_img = zoom_image(img, zoom_factor)
        print('New shape after slicing:', new_img.shape)
        display_images(img, new_img)
    except Exception as e:
        print('Error:', e)