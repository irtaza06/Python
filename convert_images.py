import subprocess
from PIL import Image

imagenames = subprocess.check_output("ls  *.ext | sed 's:/$::'", shell=True, text=True).splitlines()

for image in imagenames:
    new_name = f'{image[:-4]}.newext'
    load_img = Image.open(image)
    load_img.save(new_name)
    
