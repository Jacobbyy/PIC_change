from PIL import Image
from removebg import RemoveBg

# 修改照片背景色
rmbg = RemoveBg('EuPqCjvXK93bcS1QujiKfiZF', 'error.log')
rmbg.remove_background_from_img_file('pic1.jpg') # 此处运行完，会自动生成一个去除背景的图片，名称为"旧文件名_no_bg.png",这一步相当于抠图

# 将抠出的图读取进来
no_bg_image_name = 'pic1.jpg' + "_no_bg.png"
no_bg_image = Image.open(no_bg_image_name)
x, y = no_bg_image.size

# 创建一个新的红底的图片背景，可以在color中传入任何想要的背景颜色
new_image = Image.new('RGBA', no_bg_image.size, color='Red')

# 将抠出的图和红色背景图片合并
new_image.paste(no_bg_image, (0, 0, x, y), no_bg_image)
new_image.save('change_color_red.png')