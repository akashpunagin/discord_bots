from pynter.pynter import generate_captioned

def addCaptionToImage(image_path, font_path, caption, output_path):

  im = generate_captioned(
    caption,
    image_path=image_path,
    # size=(1080, 1350),
    font_path=font_path,
    filter_color=(0, 0, 0, 40),
  )
  im.convert('RGB').save(output_path)