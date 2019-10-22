from PIL import Image, ImageFilter

'''
img = Image.open('./pikachu.jpg')
#filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert("L")
filtered_img.save("pik-grey.png", "png")
filtered_img.show()
'''

img = Image.open('./astro.jpg')
'''
This will distort the image based on aspect ration in some cases
new_img = img.resize((400, 400))
new_img.save('astro-thumbnail.jpg')
'''
# To preserve resolution with resizing...
# use .thumbnail instead of .resize
img.thumbnail((400, 400))
img.save('astro-thumbnail-1.jpg')

print(img.size)

