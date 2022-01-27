import fitz
import time
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

# Convertir PDF TO IMG-----------------------

#Pongo el Path deL PDF a Convertir
pdffile = input("ingrese path del pdf : ")

doc = fitz.open(pdffile)
page = doc.loadPage(0)  # number of page
pix = page.get_pixmap()
output = "resultado.png"
pix.save(output)

time.sleep(2)


# CONVERTIR IMG TO TXT-----------------------

#Pongo Path de instalacion tesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Pongo el Path de la Imagen a Convertir

#filename = input("ingrese path de la Imagen : ")
#filename='dniDorso_1.png'

filename = output

#Pongo el Path del output txt de salida
outfile = input("ingrese path del txt de output : ")

#outfile='extraccion.txt'

#Escribo en el TXT
f = open(outfile,"w")

#Leo IMG usando el lenguaje español
text = str(((pytesseract.image_to_string(Image.open(filename),lang='spa'))))

f.write(text)
f.close()
print("Terminado!!")

