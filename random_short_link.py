import random, string, types, sh, qrcode, re, uuid, sys
import combine_images

def build_dict():
    characterDict = {}

    for i, character in enumerate(string.ascii_lowercase):
        characterDict[i] = character
    for i, character in enumerate(string.ascii_uppercase):
        characterDict[i+26] = character
    for i, ciffer in enumerate(range(0,10)):
        characterDict[i+26+26] = ciffer
    return characterDict

def get_rand_char():

    characterDict = build_dict()

    random_character = random.randint(0,len(characterDict)-1)
    return random_character

def main(count=1, bitly=False, tinycc=False, tinyurl=False, isgd=False, soogd=False, all_urls=False, qrcode=False):
    """Returns random bitly, tinycc, tinyurl, isgd or soogd URL(s), optionally writes qrcode image file(s)."""
    
    characterDict = build_dict()

    result = []
    if bitly or all_urls:
        for i in range(0, int(count)):
            start_url = 'https://bit.ly/'
            for i in range(0,7):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if tinycc or all_urls:
        for i in range(0, count):
            start_url = 'https://tiny.cc/'
            for i in range(0,6):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if tinyurl or all_urls:
        for i in range(0, count):
            start_url = 'https://tinyurl.com/'
            for i in range(0,8):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if isgd or all_urls:
        for i in range(0, count):
            start_url = 'https://is.gd/'
            for i in range(0,6):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if soogd or all_urls:
        for i in range(0, count):
            start_url = 'https://soo.gd/'
            for i in range(0,4):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)

    if qrcode:
        for item in result:
            py_write_qr(item)

    return(result)

def cli_print(qrcode=True, count=5):
    result = main(bitly=True, qrcode=qrcode, count=count)
    for item in result:
        print(item)

def py_write_qr(image_name):

    uid = uuid.uuid4()
    randStr = uid.hex[:4]
    img = qrcode.make(image_name)
    m = re.search('/([^/]+?)/.+?$', image_name)
    filename = m.group(1) + "_" + randStr + '.png'
    img.save(str(filename))
    
    combine_images.main(filename='horizontally_combined.jpg')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        cli_print(count=sys.argv[1])
    else:
        cli_print()
    
