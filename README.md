# paper_links

**paper_links** is a Python Linux CLI to create random (unused) link shortener URLs and QR codes from one or all of 5 link shortener providers.

## What's the idea?
The idea is that these QR codes containing unused links can be printed now and then used as links at a later time, using the appropriate link shortener provider and choosing the custom link option. 

They are links that can be physically printed now and defined later *by the user of the printed material*.

Imagine a notebook that already has a qrcode on each page for you to use in your note-taking endevours.

Or a report that already has a qrcode for you to add a link to a ressource.

Or a t-shirt. Or a roll of stickers.

<br>

## Usage

Run the script with the argument `1` to get a single bit.ly link:

    $ paper_links 1

    https://bit.ly/daSjviC

Specify which provider to use by setting the argument to `True`. 

Options are `bitly`, `tinycc`, `tinyurl`, `isgd` and `soogd`:

    $ paper_links --bitly=True --tinycc=True

    https://bit.ly/fZyHLbq
    https://tiny.cc/JSwnQq

Use the `--count=` argument to specify multiple results:

    $ paper_links --tinycc=True --count=3

    https://tiny.cc/Eses2F
    https://tiny.cc/CC9ba9
    https://tiny.cc/K1NtgX

Use the argument `--long_hash=True` to get longer URL hashes (to minimize collisions with existing URLs):

    paper_links --bitly=True --long_hash=True

    https://bit.ly/ExCLy96Uqnil      # 12 digits vs. 7 digits

Use the argument `write_qrcode=True` to write individual QR code `.png`'s and a horizontally combined `.jpg`:

    paper_links --bitly=True --count=3 --write_qrcode=True

    https://bit.ly/Cb3tHujtPcJS
    https://bit.ly/t7qKrdfqVpS5
    https://bit.ly/2VgHfwQZkCDa

![qrcode](horizontally_combined.jpg)
