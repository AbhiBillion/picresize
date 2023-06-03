import os
from PIL import Image

current_working_directory = os.getcwd()
print(current_working_directory)
"""
create two folders with the name "org" and "res" 
"""
source_folder = current_working_directory+"\\org\\"
result_folder = current_working_directory+"\\res\\"
for image in os.listdir(source_folder):
    img = Image.open(os.path.join(source_folder, image))
    img = img.resize((150, 150))
    img = img.rotate(270)
    img.save(os.path.join(result_folder, image))