#!/home/dd/anaconda3/bin/python
"""Create random link shortener URLs. Use long_hash=True to avoid collisions."""
import random, string, types, sh, qrcode, re, uuid, sys, fire
import combine_images


date = "2019/09/15"
version = 'v0.1.3'
author = "https://github.com/taext"
feedback_welcome = "gh@v1d.dk"
whats_new = "fire CLI, rename to paper_links"

def info():
    for item in [date, version, author, feedback_welcome]:
        print(item)


def build_dict():
    """Builds character set (internal method)"""
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

def cli_print(write_qrcode=True, count=5):
    result = main(bitly=True, write_qrcode=write_qrcode, count=count, long_hash=True)
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

    fire.Fire(main)
    # if len(sys.argv) == 2:
    #     cli_print(count=int(sys.argv[1]))
    # else:
    #     cli_print()
    