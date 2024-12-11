import img2pdf
import os

# convert all files ending in .jpg inside a directory
dirname = "C:\\Users\\Patron\\Downloads\\Slides3Cropped"
imgs = []
for fname in os.listdir(dirname):
	print(fname)
	if not fname.endswith(".PNG"):
		continue
	path = os.path.join(dirname, fname)
	if os.path.isdir(path):
		continue
	imgs.append(path)
with open("finalslides3.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))