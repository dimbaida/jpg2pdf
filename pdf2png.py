from pdf2image import convert_from_path
import os

path_pdf = r"D:\Dropbox\Documents\Organisations\4AGames\Offer_Letter_Baidachnyi.pdf"
path_png = r"D:\Dropbox\Documents\Organisations\4AGames\png"
if not os.path.exists(path_png):
    os.mkdir(path_png)

pages = convert_from_path(path_pdf, poppler_path=r"C:\Program Files\poppler-0.68.0\bin")
for i, page in enumerate(pages):
    page.save(os.path.join(path_png, f'page_{str(i+1).zfill(2)}.png'))
