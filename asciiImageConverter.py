import sys, argparse
import numpy as np
import math
import time 

from PIL import Image
 
# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/
 

gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
 

gscale2 = '@%#*+=-:. '
# gscale2 =  "@#S%?*+;:, "
 
def getAverageL(image):
 

    im = np.array(image)
    w,h = im.shape
 

    return np.average(im.reshape(w*h))
 
def convertImageToAscii(image, w, scale , moreLevels):

    global gscale1, gscale2
 

    # image = Image.open(fileName).convert('L')
    image = image.convert("L")

    W, H = image.size[0], image.size[1]
    # print("input image dims: %d x %d" % (W, H))
 
    cols = int(W/w)
    h = w*scale
    rows = int(H/h)
     
    # print("cols: %d, rows: %d" % (cols, rows))

    # print("tile dims: %d x %d" % (w, h))
 

    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
 

    aimg = []

    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        # correct last tile
        if j == rows-1:
            y2 = H
 
        aimg.append("")
 
        for i in range(cols):

            x1 = int(i*w)
            x2 = int((i+1)*w)
 
            if i == cols-1:
                x2 = W

            lg1 = len(gscale1)-1
            lg2 = len(gscale2)-1

            img = image.crop((x1, y1, x2, y2))
 
            avg = int(getAverageL(img))
 
            if moreLevels:
                gsval = gscale1[int((avg*lg1)/255)]
            else:
                gsval = gscale2[int((avg*lg2)/255)]
 
            aimg[j] += gsval
     
    return aimg
 

def main():

    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)

    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--w', dest='w', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')
 

    args = parser.parse_args()
   
    imgFile = args.imgFile
 

    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile
 

    if args.scale:
        scale = float(args.scale)
 
    if args.w:
        w = int(args.w)

    t1 = time.time()

    image = Image.open(imgFile)
 
    print('generating ASCII art...')
    aimg = convertImageToAscii(image, w, scale, args.moreLevels)
 
    f = open(outFile, 'w')
 
    for row in aimg:
        f.write(row + '\n')
 
    f.close()
    print("ASCII art written to %s" % outFile)
    t2 = time.time()
    print(f"Time for generate ascii {t2 - t1}")
 
if __name__ == '__main__':
    main()