from PIL import Image
from os import listdir
import numpy as np

def preprocess_image(input_image_path, output_image_path, image_size, save = False, resize = True):
     
    image = Image.open(input_image_path)
    resized_image = image.resize(tuple(reversed(image_size)), Image.BICUBIC) if resize else image
    
    image_data = np.array(resized_image, dtype='float32')
    image_data /= 255.
    image_data = np.expand_dims(image_data, 0)  # Add batch dimension.
    
    #print(image_data.shape)
    
    if (save): resized_image.save(output_image_path)
        
    return image_data
    
    
def take_n_resize_images(input_path, output_path = "", image_size=(28,28), num_examples=None, num_channels=3, save = False, resize = True, start = 0):

    if num_examples == None: num_examples = len(listdir(input_path))
    images = np.zeros((num_examples,
                       image_size[0],
                       image_size[1],
                       num_channels))

    for i,file in enumerate(listdir(input_path)):
        if i < start: continue
        if i == start+num_examples: break
        images[i-start] = preprocess_image(input_path +'/'+file, 
                                     output_path +'/'+file, 
                                     image_size,
                                     save,
                                     resize)


    return images