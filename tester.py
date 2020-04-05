import extractBits
import byteTranslator
from isolateBits import analyze
from isolateBits import amplify


# extractBits.getBits("Images/DogDog.png", "bits/dogdog.csv", 100000, [0, 0])
# byteTranslator.toChars("bits/dogdog.csv")
# byteTranslator.toImage("bits/dogdog.csv","extractedimg/dogdog.png",100,100)
# From messing around with different image dimensions, 80*62 produces something really interesting

# analyze("Images/AlbumCover.png", "FirstHalfOutput/ACplot.png")
# amplify("Images/AlbumCover.png", "SecondHalfOutput/ACamp.png")
def protocol(filename, bitRange=None, amp = False):
    print("working on " + filename + " with bitRange " + str(bitRange))
    if bitRange is None:
        bitRange = [0, 0]
    addon = str(bitRange[0]) + "to" + str(bitRange[1])
    extractBits.getBits("Images/" + filename + ".png", "bits/" + filename + addon + ".csv", 8000, bitRange,3000, True, False)
    byteTranslator.toChars("bits/" + filename + addon + ".csv", "extractedchr/" + filename + addon + ".txt")
    byteTranslator.toImage("bits/" + filename + addon + ".csv", "extractedimg/" + filename + addon + ".png", 200, 200)
    if (amp):
        amplify("Images/" + filename + ".png", "amplified/" + filename + ".png",0)

for i in range(0,2):
    for j in range(i,2):
        protocol('Gadget_tiny', [i, j])
        i = i

#protocol('AlbumCover',[0,0],True)
