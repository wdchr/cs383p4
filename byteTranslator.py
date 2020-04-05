import csv
import png
import io

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

  ##this part reads the header and sets the dimensions if unspecified when called (in real images he'll give us, header won't be in this format so this code is pretty useless LOL)
  h = bList[0:4]
  w = bList[4:8]
  #print(h,w)
  widthtest = 0
  heighttest = 0
  #numbers are stored BigEndian, calculate the 32 bit int and remove the header from the bytelist
  for i in range(4):
      del bList[0]
      del bList[0]
      widthtest += pow(2,(3-i))*w[i]
      heighttest += pow(2,(3-i))*h[i]
  #print("w=",widthtest,"h=",heighttest)
  if width == 0:
    width = widthtest
  if height == 0:
    height = heighttest
  #print(width,height)

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

  p = []#list of tuples for each row i.e. p = [(r,g,b,r,g,b,...),(r,g,b,r,g,b,...),...]
  for i in range(0,len(bList),width*3):
    #print(i)
    t = [bList[i+k] for k in range(width*3)]
    p.append(tuple(t))

  f = open(outFile,"wb")
  w = png.Writer(width,height,greyscale = False)
  w.write(f,p)
  f.close()
  return 0