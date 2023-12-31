from PIL import Image
import os
import glob


path = glob.glob('New_folder/*')
extention_from = 'webp'
extention_to  = 'jpg'

file_convert = []

def convert_images(from_ext, to_ext):
    count = 0
    for item in path:
        file_image = Image.open(item).convert('RGB')
        file_image.save(item.replace(from_ext, to_ext))
        count += 1
    print(f"{count}\tfiles already coverted to .{extention_to}")
        

convert_images(extention_from,  extention_to)
