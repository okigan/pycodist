#!/usr/bin/env python3
import asyncio

from pycodist import *
from multiprocessing import Pool


def mktemp():
    import tempfile
    return tempfile.mktemp()


def download(url):
    import requests
    response = requests.get(url)
    t = mktemp()
    with open(t, "wb") as f:
        for block in response.iter_content(1024):
            f.write(block)

    return t


def thumb_install():
    print("install packages/modules needed for thumb functionality")


@dist(install=thumb_install)
def thumb(url):
    image_file = download(url)
    from wand.image import Image

    thumb_filename = mktemp()

    with Image(filename=image_file) as img:
        print(img.size)
        img.resize(int(img.width * 0.25), int(img.height * 0.25))
        img.save(filename=thumb_filename)

    return thumb_filename


def sleep(sec):
    import time
    print("Sleeping for ", sec)
    time.sleep(sec)
    return sec


async def main():
    sleep_time = [1, 2, 3]
    s = distmap(sleep, sleep_time)

    for _ in s:
        print(_)

    images = ["https://placekitten.com/200/300",
              "https://placekitten.com/300/400"]

    thumbs = distmap(thumb, images)

    for t in thumbs:
        print(t)


if __name__ == "__main__":
    asyncio.run(main())
