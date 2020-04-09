import csv
import png
import io

def testForHeader(inFile):
  bList = []
  with open(inFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
      for b in row:
        bList.append(b)
  cList = []
  for b in bList:
    # print("b",b)
    cList.append(chr(int(b, 2)))
  if (bList[0] == "00000000" and bList[1] == "00000000" or bList[2] == "00000000" and bList[3] == "00000000"):
    print("**********************************************")
    print("**********************************************")
    print("**********************************************")
    print("Possible Header found in "+inFile)
    print("**********************************************")
    print("**********************************************")
    print("**********************************************")
    return True
  return False

def toChars(inFile, outFile):
  bList = []
  with open(inFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    for row in csv_reader:
      for b in row:
        bList.append(b)
  cList = []
  for b in bList:
    #print("b",b)
    cList.append(chr(int(b, 2)))

  output = io.open(outFile, 'w',encoding="utf-8")
  output.write("".join(cList))
  output.close()

def toImage(inFile,outFile, width=0, height=0):
  bList = []#List of bytes from the csv file
  with open(inFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    for row in csv_reader:
      for b in row:
        bList.append(int(b, 2))


  #print("check 0")
  if len(bList)<(3*width*height):
    print("Warning, data extended")
    print("Expected", 3*width*height, "values, recieved", len(bList))
    while len(bList)<(3*width*height):#if there is not enough data for the specified image size, pad with 0s
      bList.append(0)
  if len(bList)>(3*width*height):
    print("Warning, data truncated")
    print("Expected", 3*width*height, "values, recieved", len(bList))
    while len(bList)>(3*width*height):
      del bList[-1]
  #print("check 1")
  p = []#list of tuples for each row i.e. p = [(r,g,b,r,g,b,...),(r,g,b,r,g,b,...),...]
  for i in range(0,len(bList),width*3):
    #print(i)
    t = [bList[i+k] for k in range(width*3)]
    p.append(tuple(t))
  #print("check 2")
  f = open(outFile,"wb")
  w = png.Writer(width,height,greyscale = False)
  w.write(f,p)
  #print("check 3")
  f.close()
  return 0