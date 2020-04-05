import numpy as np
import imageio
import matplotlib.pyplot as plt


def amplify(inFile, outFile, bit):
    img = imageio.imread(inFile)
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)

    for r in range(height):
        for c in range(width):
            img[r, c][0] = (img[r, c][0] & pow(2, bit)) * 255  # RED
            img[r, c][1] = (img[r, c][1] & pow(2, bit)) * 255  # GREEN
            img[r, c][2] = (img[r, c][2] & pow(2, bit)) * 255  # BLUE

    imageio.imwrite(outFile, img)


def analyze(inFile, outFile):
    img = imageio.imread(inFile)
    height, width, channels = img.shape
    print("Height:", height, "Width:", width, "Number of Channels:", channels)
    clustArray = []
    complete = 0
    for r in range(0, height, 2):
        if (r * 100 // height > complete):
            complete += 1
            print(str(complete) + "% done")  # prints the % done with clusting
        for c in range(0, width, 2):
            if (r + 1 < height and c + 1 < width):
                # print(r,c)
                clust = 0
                # Red Cluster
                clust += (img[r, c][0] & 1)  # RED
                clust += (img[r + 1, c][0] & 1) * 2
                clust += (img[r, c + 1][0] & 1) * 4
                clust += (img[r + 1, c + 1][0] & 1) * 8
                # Green Cluster
                clust += (img[r, c][0] & 1) * 16
                clust += (img[r + 1, c][1] & 1) * 32
                clust += (img[r, c + 1][1] & 1) * 64
                clust += (img[r + 1, c + 1][1] & 1) * 128
                # Blue Cluster
                clust += (img[r, c][2] & 1) * 256
                clust += (img[r + 1, c][2] & 1) * 512
                clust += (img[r, c + 1][2] & 1) * 1024
                clust += (img[r + 1, c + 1][2] & 1) * 2048
                clustArray.append(clust)
    print("clust array created")
    plt.hist(clustArray, 1024)
    plt.savefig(outFile)
