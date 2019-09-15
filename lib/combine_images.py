import sys, os, re
from PIL import Image

def main(filename='combined.jpg'):

  filenames = os.listdir()
  filenames2 = []
  for item in filenames:
      m = re.search('\.png$', item)
      if m:
          filenames2.append(item)
  #print(filenames2)

  images = list(map(Image.open, filenames2))
  widths, heights = zip(*(i.size for i in images))

  total_width = sum(widths)
  max_height = max(heights)

  new_im = Image.new('RGB', (total_width, max_height))

  x_offset = 0
  for im in images:
    new_im.paste(im, (x_offset,0))
    x_offset += im.size[0]

  new_im.save(filename)

if __name__ == "__main__":
  # use filename argument if passed
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    main(filename=filename)
  else:
    main()