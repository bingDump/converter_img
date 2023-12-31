from PIL import Image
import os
import glob


path = glob.glob('New_folder/*')
extention_from = 'webp'
extention_to  = 'jpg'

def convert_images(from_ext, to_ext):
    count = 0
    for item in path:
        if from_ext in item:
            file_image = Image.open(item).convert('RGB')
            file_image.save(item.replace(from_ext, to_ext))
            count += 1
        else:
            continue
    
    print(f"{count}\tfiles already coverted to .{extention_to}")
    remove_images(from_ext) 

def remove_images(file_ext):
    count =  0
    confirmation = input(f"Confirm .{file_ext} will be removed?  ").lower()
    if confirmation in ['yes','ya','y']:  
        for item in path:
            if file_ext in item:
                # Remove the file from the directory
                os.remove(item)
                count += 1
        print(f"  {count}\tfiles removed")
    else:
        print("\tNo file removed")

convert_images(extention_from,  extention_to)
