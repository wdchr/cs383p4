import csv
import numpy as np
import imageio


# infile = str of image to read from
# outfile = str of csv file to write to
# numToRead = number of pixels to read from the source image
# bitrange = range of bits to read from each channel 0 = LSB, 7 = MSB
def getBits(inFile, outFile, numToRead, bitRange=[0, 0], skip = 0, BGR = False, TBLR = False):
    img = imageio.imread(inFile)
    height, width, _ = img.shape
    print("Height:", height, "Width:", width, "Channels:", _)
    # mask = 0
    # for n in range(bitRange[0], bitRange[1] + 1):
    #    mask += pow(2, n)
    extracted = [""] * numToRead
    count = 0
    mode = [0,1,2]
    if (BGR):
        mode = [2,0,1]
    if (not TBLR):
        for r in range(height):
            for c in range(width):
                for color in mode:
                    for k in range(bitRange[0], bitRange[1] + 1):
                        if count < numToRead+skip and count >= skip:
                            extracted[count - skip] = str(int((img[r, c, color] & pow(2, k)) and True))
                        count += 1
    if (TBLR):
        for c in range(width):
            for r in range(height):
                for color in mode:
                    for k in range(bitRange[0], bitRange[1] + 1):
                        if count < numToRead+skip and count >= skip:
                            extracted[count - skip] = str(int((img[r, c, color] & pow(2, k)) and True))
                        count += 1
    extstr = "".join(extracted)
    byteVals = []
    for i in range(0, len(extstr), 8):
        byteVals.append(extstr[i:i + 8])
    with open(outFile, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(byteVals)
