# Made by huge
# Hope this helps someone
# peace

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys

#main.py
#input
#style set

def main():
    myFont = ImageFont.truetype('consola.ttf', 30)
    #SET STYLE SET BELOW:
    if sys.argv[2].isnumeric == False:
        print("Incorrect usage. Style set must be 1, 2, 3, 4 or 5")
        return
    elif int(sys.argv[2]) not in [1, 2, 3, 4, 5]:
        print("Incorrect usage. Style set must be 1, 2, 3, 4 or 5")
        return
    style_set = int(sys.argv[2])
    input_path = sys.argv[1]

    im = Image.open(input_path) 
    pixels = im.getdata()
    width, height = im.size

    newImg = Image.new(mode="RGB", size=(width * 2 + 200, height * 2 + 200))

    Characters = ""
    DrawImg = ImageDraw.Draw(newImg)

    if style_set == 1:
        Characters = ".`:,;'" + '_^"\></-!~=)(|j?}{ ][ti+l7v1%yrfcJ32uIC$zwo96sngaT5qpkYVOL40&mG8*xhedbZUSAQPFDXWK#RNEHBM@'
    elif style_set == 2:
        Characters = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$#'
    elif style_set == 3:
        Characters = ".:-=+*#%@"
    elif style_set == 4:
        Characters = "_:*a8@"
    elif style_set == 5:
        Characters = "_:*8@"
    def GetChar(avg):
        avg = (avg * len(Characters)) // 255
        return Characters[int(avg)]

    def GetAvg(number):
        return pixels[number][0] * 0.3 + pixels[number][1] * 0.59 + pixels[number][2] * 0.11 / 3
    def GetAvgPixel(currentPixelIndex):
        avg1 = GetAvg(currentPixelIndex - width - 1) 
        avg2 = GetAvg(currentPixelIndex - width)
        avg3 = GetAvg(currentPixelIndex - width + 1)

        avg4 = GetAvg(currentPixelIndex - 1)
        avg5 = GetAvg(currentPixelIndex)
        avg6 = GetAvg(currentPixelIndex + 1)

        avg7 = GetAvg(currentPixelIndex + width - 1)
        avg8 = GetAvg(currentPixelIndex + width)
        avg9 = GetAvg(currentPixelIndex + width + 1)

        return (avg1 + avg2 + avg3 + avg4 + avg5 + avg6 + avg7 + avg8 + avg9) / 9

    def GetBigAvg(num):
        Aavg1 = GetAvgPixel(num - width * 3 - 3)
        Aavg2 = GetAvgPixel(num - width * 3)
        Aavg3 = GetAvgPixel(num - width * 3 + 3)

        Aavg4 = GetAvgPixel(num - 3)
        Aavg5 = GetAvgPixel(num)
        Aavg6 = GetAvgPixel(num + 3)

        Aavg7 = GetAvgPixel(num + width * 3 - 3)
        Aavg8 = GetAvgPixel(num + width * 3)
        Aavg9 = GetAvgPixel(num + width * 3 + 3)

        return (Aavg1 + Aavg2 + Aavg3 + Aavg4 + Aavg5 + Aavg6 + Aavg7 + Aavg8 + Aavg9) / 9

    OutPut = ""
    howmanytimes = 0
    for y in range(0, height, 8):
        for x in range(0, width, 8):
            awgawg = 0
            OutPut += GetChar(GetBigAvg(x + y * width))
            if x >= width - 8:
                DrawImg.text((0, 0 + howmanytimes * 17), OutPut, fill=(255, 255, 255), font=myFont)
                OutPut = ""
                howmanytimes += 1
                break

    im.close()
    newImg.save("output.png")
    print("Done")

if __name__ ==  "__main__":
    if len(sys.argv) == 3:
        main()