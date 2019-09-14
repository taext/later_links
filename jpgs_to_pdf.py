import os, sys
import img2pdf

def main(filename):
    with open(filename, "wb") as f:
        f.write(img2pdf.convert("horizontally_combined.jpg"))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main("qr.pdf")
