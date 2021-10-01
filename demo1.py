from PIL import Image
# 修改照片尺寸
def change_size(file_in, file_out, width, height):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)
change_size('pic1.jpg','change_size.jpg',406,495)