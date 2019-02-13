## Toyota Agent
import sys
import machine
from time import sleep_ms
from machine import Pin
import neopixel

from machine import Pin,ADC
from time import sleep_ms

adc = ADC(Pin(35))
adc.atten(ADC.ATTN_11DB)

flag = 0
timer = machine.Timer(0)

MAXLEN = 60
PIN = 14
neo = neopixel.NeoPixel(Pin(PIN), MAXLEN)

frflag = 0
flflag = 0
flcount = 0
frcount = 0
flowothers = 0.8
flownums = [2,1.8,1.6,1.4,1.2,1]


def Change(timer):
    global flag
    flag = 1

timer.init(period=50, mode=machine.Timer.PERIODIC, callback=Change)



def CDS():
    global adc
    ave = 0
    cnt = 0
    sum = 0
    while True:
        val = adc.read()
        print(val)
        cnt +=1
        sum += val
        ave = sum / cnt
        sleep_ms(50)
        if ave - val > 100:
            print("GO!")
            break

def blacken():
    for x in range(MAXLEN):
        neo[x]=(0,0,0)
    neo.write()

def modeN(neo,color,half):
    for x in range(MAXLEN):
        neo[x]= color
    if half == "1":
        for x in range(0,MAXLEN,2):
            neo[x] = (0,0,0)

    neo.write()

# def modeFL(neo,color,startNum,endNum):
#     global flcount
#     global flflag
#     global flowothers
#     global flownums
#     colorNum = endNum - startNum + 1
#
#     if flflag == 0:
#         flcount = 0
#         flflag = 1
#         frflag = 0
#
#
#     neo.fill((0,0,0))
#     bgcolor = tuple([int(i * flowothers) for i in color])
#     color0 = tuple([int(i * flownums[0]) for i in color])
#     color1 = tuple([int(i * flownums[1]) for i in color])
#     color2 = tuple([int(i * flownums[2]) for i in color])
#     color3 = tuple([int(i * flownums[3]) for i in color])
#
#     for i in range(startNum,endNum):
#         neo[i] = bgcolor
#
#     neo[startNum+(frcount%colorNum)] = color0
#     if endNum-(frcount%colorNum)+1 <= endNum:
#         neo[endNum-(frcount%colorNum)-1] = color1
#     if endNum-(frcount%colorNum)+2 <= endNum:
#         neo[endNum-(frcount%colorNum)-2] = color2
#     if endNum-(frcount%colorNum)+3 <= endNum:
#         neo[endNum-(frcount%colorNum)-3] = color3
#
#     flcount += 1
#     print("FRON!")
#
#     neo.write()
def modeFL(neo,color,startNum,endNum,half):
    global flcount
    global flflag
    global flowothers
    global flownums
    colorNum = endNum - startNum + 1

    if flflag == 0:
        flcount = 0
        flflag = 1
        frflag = 0
        # print("FRON!")

    neo.fill((0,0,0))
    bgcolor = tuple([int(i * flowothers) for i in color])
    color0 = tuple([int(i * flownums[0]) for i in color])
    color1 = tuple([int(i * flownums[1]) for i in color])
    color2 = tuple([int(i * flownums[2]) for i in color])
    color3 = tuple([int(i * flownums[3]) for i in color])
    color4 = tuple([int(i * flownums[4]) for i in color])
    color5 = tuple([int(i * flownums[5]) for i in color])

    for i in range(startNum,endNum):
        neo[i] = bgcolor

    neo[endNum-(flcount%colorNum)] = color0
    if endNum-(flcount%colorNum)+1 <= endNum:
        neo[startNum-(flcount%colorNum)+1] = color1
    if endNum-(flcount%colorNum)+2 <= endNum:
        neo[startNum-(flcount%colorNum)+2] = color2
    if endNum-(flcount%colorNum)+3 <= endNum:
        neo[startNum-(flcount%colorNum)+3] = color3
    if endNum-(flcount%colorNum)+4 <= endNum:
        neo[startNum-(flcount%colorNum)+4] = color4
    if endNum-(flcount%colorNum)+5 <= endNum:
        neo[startNum-(flcount%colorNum)+5] = color5
    for i in range(startNum-1):
        neo[i] = (0,0,0)
    if endNum != 59:
        for i in range(endNum+1,60):
            neo[i] = (0,0,0)
    else:
        pass

    flcount += 1
    if half == "1":
        for x in range(0,MAXLEN,2):
            neo[x] = (0,0,0)
    neo.write()

def modeFR(neo,color,startNum,endNum,half):
    global frcount
    global frflag
    global flowothers
    global flownums
    colorNum = endNum - startNum + 1

    if frflag == 0:
        frcount = 0
        frflag = 1
        flflag = 0
        # print("FRON!")

    neo.fill((0,0,0))
    bgcolor = tuple([int(i * flowothers) for i in color])
    color0 = tuple([int(i * flownums[0]) for i in color])
    color1 = tuple([int(i * flownums[1]) for i in color])
    color2 = tuple([int(i * flownums[2]) for i in color])
    color3 = tuple([int(i * flownums[3]) for i in color])
    color4 = tuple([int(i * flownums[4]) for i in color])
    color5 = tuple([int(i * flownums[5]) for i in color])


    for i in range(startNum,endNum):
        neo[i] = bgcolor

    neo[startNum+(frcount%colorNum)] = color0
    if startNum+(frcount%colorNum)-1 >= startNum:
        neo[startNum+(frcount%colorNum)-1] = color1
    if startNum+(frcount%colorNum)-2 >= startNum:
        neo[startNum+(frcount%colorNum)-2] = color2
    if startNum+(frcount%colorNum)-3 >= startNum:
        neo[startNum+(frcount%colorNum)-3] = color3
    if startNum+(frcount%colorNum)-4 >= startNum:
        neo[startNum+(frcount%colorNum)-4] = color4
    if startNum+(frcount%colorNum)-5 >= startNum:
        neo[startNum+(frcount%colorNum)-5] = color5

    frcount += 1
    if half == "1":
        for x in range(0,MAXLEN,2):
            neo[x] = (0,0,0)

    neo.write()

def modeP(neo,color,startNum,endNum,half):
    for x in range(MAXLEN):
        if x <startNum or x > endNum:
            neo[x] = (0,0,0)
        elif x<= endNum and x >= startNum:
            neo[x] = color
    if half == "1":
        for x in range(0,MAXLEN,2):
            neo[x] = (0,0,0)
    neo.write()

def CSVread(filename):
    global flag
    global neo
    global flflag
    global frflag
    Red = (120,0,0)
    Yellow = (90,90,0)
    # Ao = (10,30,20)
    off = (0,0,0)
    Purple = (60,0,120)
    White = (60,60,60)
    Orange = (120,60,0)

    timing = None
    pattern = None
    color = None
    iro = None

    startNum = 0
    endNum = 0
    dir = None
    half = None
    print(filename)

    with open(filename,'r') as file:
        for l in file:#1gyou zutu miru
            l = l.rstrip('\n')
            l = l.rstrip('\r')#hen na yatu toru (l ha str)
            Data = l.split(",")

            #1gyou 1cell zutu miru
            for index, cell in enumerate(Data):
                if index == 0:
                    timing = int(cell)
                elif index == 1:
                    if cell == "R":
                        color = Red
                    elif cell =="W":
                        color = White
                    elif cell =="Y":
                        color = Yellow
                    elif cell =="P":
                        color = Purple
                    elif cell =="O":
                        color = Orange
                    else:
                        color = Ao
                elif index == 2:
                    pattern = cell
                elif index == 3:
                    if pattern == "n":
                        pass
                    else:
                        startNum = int(cell)
                elif index == 4:
                    if pattern == "n":
                        pass
                    else:
                        endNum = int(cell)
                elif index == 5:
                    dir = cell
                elif index == 6:
                    half = cell
                else:
                    pass


            if pattern == "n":
                modeN(neo,color,half)
            elif pattern == "f" and dir =="r":
                modeFL(neo,color,startNum,endNum,half)
            elif pattern == "f" and dir =="l":
                modeFR(neo,color,startNum,endNum,half)
            elif pattern == "p":
                modeP(neo,color,startNum,endNum,half)
            else:
                pass

            # print(index)
            while True:
                if flag == 1:
                    flag = 0
                    break
CDS()

CSVread('kyorokurai.csv')
blacken()

CDS()

CSVread('mono.csv')
blacken()

CDS()

CSVread('nukarekurai.csv')
blacken()

CDS()

CSVread('dozokurai.csv')
blacken()

CDS()

CSVread('shasenkurai.csv')
blacken()

CDS()

CSVread('iretekurai.csv')
blacken()


CDS()

CSVread('singokurai.csv')
blacken()



sleep_ms(1000)

sys.exit()
machine.reset()
