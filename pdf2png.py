from pdf2image import convert_from_path
import os

poppler_path = os.path.join(os.getcwd(), r'poppler-0.68.0\bin')

path_pdf = r"C:\Users\user\Desktop\1.pdf"
path_png = r"C:\Users\user\Desktop\png"

if not os.path.exists(path_png):
    os.mkdir(path_png)

pages = convert_from_path(path_pdf, poppler_path=poppler_path)
for i, page in enumerate(pages):
    page.save(os.path.join(path_png, f'page_{str(i+1).zfill(2)}.png'))
