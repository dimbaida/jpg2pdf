from PIL import Image
from pathlib import Path

path_png = Path("/Users/dim/Dropbox/=Photos/ALBUMS/ALBUM 2022/")
path_pdf = Path("/Users/dim/Dropbox/=Photos/ALBUMS/ALBUM 2022/doc.pdf")

p = Path(path_png).glob('*')
images = [Image.open(x).convert('RGB') for x in sorted(p) if x.is_file() and x.suffix == '.png']
images[0].save(path_pdf, save_all=True, append_images=images[1:])
