#!/usr/bin/env python3
"""
Author : capalvin <capalvin@localhost>
Date   : 2021-11-29
Purpose: Rock the Casbah
"""

import random
import argparse
import sys
import PIL
from PIL import Image
import io
import pathlib


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('picture', help='A picture file', metavar='FILE')
    parser.add_argument('-o',
                        '--output',
                        help='An output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    # -------------------------------------------------------------------------------------------------------------------------------
    args = get_args()
    pic = args.picture
    outFile = args.output

    # -------------------------------------------------------------------------------------------------------------------------------
    imagine = Image.open(pic)
    colors = imagine.getpixel((random.randint(0, 150), random.randint(0, 150)))
    print("RGB Pixel Colors:", colors)
    # -----------------------------------------------------------------------------------------------------------------------------------
    if colors[0] + colors[1] + colors[2] >= 550 or colors[2] > colors[
            1] and colors[2] > colors[0] and (colors[0] + colors[1] >=
                                              colors[2]):
        print("Season Prediction: Winter")
        sp = "Season Prediction: Winter"
    elif colors[0] > colors[1] and colors[0] > colors[2]:
        print("Season Prediction: Fall")
        sp = "Season Prediction: Fall"
    elif colors[1] > colors[0] and colors[1] > colors[2] and (
            colors[2] + colors[0] <= colors[1]):
        print("Season Prediction: Spring-Summer")
        sp = "Season Prediction: Spring-Summer"
    elif colors[2] > colors[1] and colors[2] > colors[0]:
        print("Season Prediction: Summer-Spring")
        sp = "Season Prediction: Summer-Spring"
    if outFile != sys.stdout:
        outFile.write("RGB Pixel Colors: " + str(colors) + '\n' + sp + '\n')
    else:
        pass


# --------------------------------------------------
if __name__ == '__main__':
    main()
