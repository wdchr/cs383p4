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
global header
header = []


def protocol(filename, bitRange=None, amp=False, active=[True, True, True, True], skip=0, BGR=False, TDLR=False):
    # print("working on " + filename + " with bitRange " + str(bitRange))

    global header
    if bitRange is None:
        bitRange = [0, 0]
    addon = str(bitRange[0]) + "to" + str(bitRange[1])
    if active[0]:
        addon += 'R'
    if active[1]:
        addon += 'G'
    if active[2]:
        addon += 'B'
    if TDLR:
        addon += "TDLR"
    if BGR:
        addon += "BGR"
    addon += str(skip)
    # 18874368
    filemod = ''
    # print("Working on " + filename + addon)
    extractBits.getBits("Images" + filemod + "/" + filename + ".png", "bits/" + filename + addon + ".csv", 8000,
                        bitRange, skip,
                        BGR, TDLR, active)
    if (byteTranslator.testForHeader("bits/" + filename + addon + ".csv")):
        header += [filename + addon]
        byteTranslator.toChars("bits/" + filename + addon + ".csv", "extractedchr/" + filename + addon + ".txt")
        byteTranslator.toImage("bits/" + filename + addon + ".csv", "extractedimg/" + filename + addon + ".png", 125, 1)
    if (amp):
        amplify("Images" + filemod + "/" + filename + ".png", "amplified/" + filename + ".png", bitRange[0])


# "AlbumCover","Brothers2", "Brothers_small", "DogDog", "ExtraCredit", "Floof",
#          "FriendlyPupper", "Gadget", "Gadget_medium", "Gadget_small", "Gadget_tiny","GadgetRadiator","Grooming", "LastBastionOfRadiance",
#          "MoJoJoJoCouch", "PupFriends", "PuppyLeash", "StegTest", "TheGrassIsGreener", "TripleThreat", "WideDogIsWide",
#"ExtraCredit", "Floof","Gadget", "Gadget_medium",,"TripleThreat"
unfound = [ "Gadget_small", "Gadget_tiny","LastBastionOfRadiance","StegTest"]
files = ["WinkyFace", "Woof1"]
files2 = ["AlbumCover", "Brothers2", "Brothers_small", "DogDog", "ExtraCredit", "Floof",
          "FriendlyPupper", "Gadget", "Gadget_medium", "Gadget_small", "Gadget_tiny", "GadgetRadiator",
          "Grooming", "LastBastionOfRadiance", "TripleThreat", "WideDogIsWide", "WinkyFace", "Woof1"]

extra = ['broextr', 'broextr2', 'groomcomic', 'mojo', 'temp1']


# extractBits.getBits("Images/MoJoJoJoCouch.png", "bits/MoJoJoJoCouch0to0RGB.csv", 1000000, [0,0], 0, False, True, [1,1,1])
# byteTranslator.toImage("bits/MoJoJoJoCouch0to0RGB.csv", "extractedimg/mojo.png", 190, 168)

# byteTranslator.testForHeader("bits/Brothers_small0to0RGB.csv")
def method1():
    for filename in unfound:
        print(filename)
        for i in range(4):
            for k in range(3):
                for j in range(k, 3):
                    for skip in [3000]:
                        for TDLR in [True, False]:
                            if i == 0:
                                protocol(filename, [k, j], False, [True, True, True], skip, True,
                                         TDLR)
                            protocol(filename, [k, j], False, [i % 3 == 0, i % 2 == 1, i > 1], skip, False, TDLR)
    print("HEADERS:\n", '\n'.join(header))


def method2():
    for filename in files:
        for k in range(2):
            amplify("Images/" + filename + ".png", "amplified/" + filename + str(k) + ".png", k)


def method3():
    for filename in extra:
        for i in range(4):
            for k in range(2):
                protocol(filename, [0, k], False, [i % 3 == 0, i % 2 == 1, i == 2 or i == 3])


for i in range(4):
    for k in range(2):
        for j in range(k, 2):
            break
            # protocol("broextr2", [k, j], False, [i % 3 == 0, i % 2 == 1, i == 2 or i == 3])
for i in range(4):
    # protocol("WinkyFace", [0,1], False, [i % 3 == 0, i % 2 == 1, i == 2 or i == 3])
    # protocol("WideDogIsWide", [0, 0], False, [i % 3 == 0, i % 2 == 1, i == 2 or i == 3])
    # protocol("broextr", [1, 1], False)
    break


# method1()


def method4(filename):
    extractBits.getBits("Images/" + filename + ".png", "bits/" + "temp" + ".csv", 3200000,
                        [0, 0], 64, True, True, [True, True, True])
    byteTranslator.toChars("bits/" + "temp" + ".csv", "extractedchr/temp.txt")
    byteTranslator.toImage("bits/" + "temp" + ".csv", "extractedimg/temp1.png", 382, 281)


def method5(filename):
    for i in range(4):
        for k in range(3):
            for j in range(k, 3):
                for skip in [0, 1000]:
                    for TDLR in [True, False]:
                        if i == 0:
                            protocol(filename, [k, j], False, [True, True, True], skip, True,
                                     TDLR)
                        protocol(filename, [k, j], False, [i % 3 == 0, i % 2 == 1, i > 1], skip, False, TDLR)
    print("HEADERS:\n", '\n'.join(header))


# method4("TheGrassIsGreener")
#for filename in extra:
    #method5(filename)

method1()

# protocol('AlbumCover',[0,0],True)

# toAmplify = "GadgetRadiator"
# for i in range(6):
#    amplify("Images/" + toAmplify + ".png","amplified/"+ toAmplify + str(i) +".png",i)
