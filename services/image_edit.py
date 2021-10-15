from PIL import Image, ImageDraw, ImageFont

def addTextToImage(image_path, font_path, text, output_path):

  # get an image
  base = Image.open(image_path).convert("RGBA")

  # make a blank image for the text, initialized to transparent text color
  txt = Image.new("RGBA", base.size, (255,255,255,0))

  # get a font
  fnt = ImageFont.truetype(font_path, 40)
  # get a drawing context
  d = ImageDraw.Draw(txt)

  # draw text, half opacity
  d.text((10,10), text, font=fnt, fill=(252,111,3,128))
  # # draw text, full opacity
  # d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

  out = Image.alpha_composite(base, txt)
  out.save(output_path)