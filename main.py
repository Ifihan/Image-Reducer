from PIL import Image
import os
import sys

img_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for image in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{image}')
    clean = os.path.splitext(image)[0]
    img.thumbnail((500, 500))
    img.save(f'{output_folder}{clean}.png', 'png')
    print('all done')