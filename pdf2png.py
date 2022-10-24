from pdf2image import convert_from_path
from pathlib import Path

path_pdf = Path("/Users/dim/Dropbox/=Photos/ALBUMS/ALBUM 2022/")
path_png = Path("/Users/dim/Dropbox/=Photos/ALBUMS/ALBUM 2022/")

p = Path(path_pdf).glob('*')
files = [x for x in p if x.is_file() and x.suffix == '.pdf']

for file in files:
    print(file.resolve())
    pages = convert_from_path(file, 500)
    for i, page in enumerate(pages):
        page.save(path_png/(file.stem + '_' + str(i+1).zfill(len(str(i))) + '.png'), 'PNG')
