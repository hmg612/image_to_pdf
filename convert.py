import os
from PIL import Image
from img2pdf import convert

img_dir = "C:\\Users\\HONG\\Desktop\\image"

img_list = []
for file in os.listdir(img_dir):
    if file.endswith(".png"):
        img_list.append(file)
    elif file.endswith(".jpg"):
        img_list.append(file)

img_path = []
for i in img_list:
    img_path.append("C:\\Users\\HONG\\Desktop\\image\\{}".format(i))


for j in img_path:
    with open("{}.pdf".format(j.split('\\')[-1].split('.')[0]), "wb") as f:
        image = Image.open(j)
        pdf = convert(image.filename)
        f.write(pdf)
        image.close()
        f.close()
