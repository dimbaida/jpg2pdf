from PIL import Image
from os import listdir
from os.path import isfile, join

path = r"./png"
images = [Image.open(join(path, f)).convert('RGB') for f in sorted(listdir(path)) if isfile(join(path, f))]

images[0].save(join(path, 'test.pdf'), save_all=True, append_images=images[1:])
