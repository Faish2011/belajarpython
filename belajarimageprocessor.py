from PIL import Image, ImageFilter

filename = 'Leonardo M60A3 (Italy).jpeg'

with Image.open (filename) as img:
    img.load ()
# cropped_image = img.crop ((222, 100, 1200, 1000))
# flipped_image = img.transpose (Image.FLIP_LEFT_RIGHT)
# rotated_img = img.rotate (90)

# rotated_img = img.rotate (90, expand = True)
# rotated_img.show ()


gray_image = img.convert ("L")
gray_image.show ()

edges = gray_image.filter (ImageFilter.FIND_EDGES)
edges.show ()
# img.show ()
# cropped_image.show ()
# flipped_image.show ()











































