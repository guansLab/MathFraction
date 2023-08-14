#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image, ImageOps
import os

def invert_image_colors(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Invert the colors
    inverted_image = ImageOps.invert(image)
    
    return inverted_image

def process_directory(input_directory, output_directory):
    # Walk through the input directory tree
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                # Construct the full file path
                input_path = os.path.join(root, file)
                
                # Construct the corresponding output path
                relative_path = os.path.relpath(root, input_directory)
                output_path_root = os.path.join(output_directory, relative_path)
                if not os.path.exists(output_path_root):
                    os.makedirs(output_path_root)
                output_path = os.path.join(output_path_root, file)
                
                # Invert the image colors and save the result
                inverted_image = invert_image_colors(input_path)
                inverted_image.save(output_path)

# Specify the path to your directory and output directory
input_directory = 'fraction-generator-main/generated_fractions'
output_directory = 'converted_generated_fractions'
process_directory(input_directory, output_directory)

