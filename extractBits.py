import csv
import numpy as np
import imageio


# infile = str of image to read from
# outfile = str of csv file to write to
# numToRead = number of pixels to read from the source image
# bitrange = range of bits to read from each channel 0 = LSB, 7 = MSB
# skip = # of bits to skip at the start
# BGR enables blue-green-red ordering
# TBLR enables Top down left right reading
# active enables reading from r, g, or b channels
def getBits(inFile, outFile, numToRead, bitRange=[0, 0], skip = 0, BGR = False, TDLR = False, active = [True, True, True]):
    backwards = 0
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
        mode = [2,1,0]
    if (not TDLR):
        for r in range(height):
            for c in range(width):
                if (backwards):
                    r = height-r-1
                    c = width-c-1
                for color in mode:
                    if active[color]:
                        for k in range(bitRange[0], bitRange[1] + 1):
                            if count < numToRead+skip and count >= skip:
                                extracted[count - skip] = str(int((img[r, c, color] & pow(2, k)) and True))
                            count += 1
    if (TDLR):
        for c in range(width):
            for r in range(height):
                for color in mode:
                    if active[color]:
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
