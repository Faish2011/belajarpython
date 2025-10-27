from PIL import Image, ImageDraw, ImageFont

# image = Image.new (mode = 'RGB', size = (500, 500))
font = ImageFont.truetype ('arial', 100)

gambar = Image.new ('RGB', (1080, 1920), color = (0, 77, 64))

draw = ImageDraw.Draw (gambar)

# text_font = ImageFont.truetype ('arial', 40)
# draw = ImageDraw.Draw (image)


draw.text (
    xy = (100, 100),
    text = "HAH",
    font = font,
    fill = (255, 255, 255),
    anchor = 'mm',
    # font = text_font
)

gambar.show ()






































