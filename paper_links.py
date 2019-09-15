"""
    - Create random link shortener URLs
    - Use write_qrcode=True for QR code images
    - Use long_hash=True to avoid collisions

"""
import random, string,  qrcode, re, uuid, sys, fire
import combine_images


date = "2019/09/15"
version = 'v0.1.6'
author = "https://github.com/taext"
feedback_welcome = "paper_links@v1d.dk"
download_url = "https://github.com/taext/paper_links/archive/v0.1.6.zip"
documentation_url = "https://github.com/taext/paper_links/blob/master/README.md"
license_mit = "https://github.com/taext/paper_links/blob/master/LICENSE"
whats_new = "update feedback mail"


def info():
    """Print meta-data."""
    for item in [version, date, author, feedback_welcome, documentation_url, download_url]:
        print(item)

def build_dict():
    """Builds character set (internal method)."""
    characterDict = {}

    for i, character in enumerate(string.ascii_lowercase):
        characterDict[i] = character
    for i, character in enumerate(string.ascii_uppercase):
        characterDict[i+26] = character
    for i, ciffer in enumerate(range(0,10)):
        characterDict[i+26+26] = ciffer
    return characterDict

def get_rand_char():
    """Returns a random character from the character set (internal method)."""

    characterDict = build_dict()

    random_character = random.randint(0,len(characterDict)-1)
    return random_character

def main(bitly=False, tinycc=False, tinyurl=False, isgd=False, soogd=False, all_urls=False, count=1, write_qrcode=False, long_hash=False):
    """Returns random bitly, tinycc, tinyurl, isgd or soogd URL(s), optionally writes qrcode image file(s)."""
    
    characterDict = build_dict()

    result = []
    if bitly or all_urls:
        for i in range(0, count):
            start_url = 'https://bit.ly/'
            length = 7
            if long_hash:
                length += 5
            for i in range(0,length):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if tinycc or all_urls:
        for i in range(0, count):
            start_url = 'https://tiny.cc/'
            length = 6
            if long_hash:
                length += 4
            for i in range(0,length):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if tinyurl or all_urls:
        for i in range(0, count):
            start_url = 'https://tinyurl.com/'
            length = 8
            if long_hash:
                length += 5
            for i in range(0,length):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if isgd or all_urls:
        for i in range(0, count):
            start_url = 'https://is.gd/'
            length = 6
            if long_hash:
                length += 4
            for i in range(0,length):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)
    if soogd or all_urls:
        for i in range(0, count):
            start_url = 'https://soo.gd/'
            length = 4
            if long_hash:
                length += 4
            for i in range(0,length):
                random_char = characterDict[get_rand_char()]
                start_url += str(random_char)
            result.append(start_url)

    if write_qrcode:
        for item in result:
            py_write_qr(item)

    return(result)


def py_write_qr(image_name):
    """Write QR code image file (internal method)."""

    uid = uuid.uuid4()
    randStr = uid.hex[:4]
    img = qrcode.make(image_name)
    m = re.search('/([^/]+?)/.+?$', image_name)
    filename = m.group(1) + "_" + randStr + '.png'
    img.save(str(filename))
    
    combine_images.main(filename='horizontally_combined.jpg')


if __name__ == "__main__":

    fire.Fire(main)

    
