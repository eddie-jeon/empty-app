from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound, TextAsset
import random, time
from ggame import LineStyle, Color

blocklist = []
secondslist = []

#All time sprites
second15 = Sprite(TextAsset("15"), (0, 45))
second14 = Sprite(TextAsset("14"), (0, 65))
second13 = Sprite(TextAsset("13"), (0, 85))
second12 = Sprite(TextAsset("12"), (0, 105))
second11 = Sprite(TextAsset("11"), (0, 125))
second10 = Sprite(TextAsset("10"), (0, 145))
second9 = Sprite(TextAsset("9"), (0, 165))
second8 = Sprite(TextAsset("8"), (0, 185))
second7 = Sprite(TextAsset("7"), (0, 205))
second6 = Sprite(TextAsset("6"), (0, 225))
second5 = Sprite(TextAsset("5"), (0, 245))
second4 = Sprite(TextAsset("4"), (0, 265))
second3 = Sprite(TextAsset("3"), (0, 285))
second2 = Sprite(TextAsset("2"), (0, 305))
second1 = Sprite(TextAsset("1"), (0, 325))
second0 = Sprite(TextAsset("0"), (0, 345))
secondslist.append(second15)
secondslist.append(second14)
secondslist.append(second13)
secondslist.append(second12)
secondslist.append(second11)
secondslist.append(second10)
secondslist.append(second9)
secondslist.append(second8)
secondslist.append(second7)
secondslist.append(second6)
secondslist.append(second5)
secondslist.append(second4)
secondslist.append(second3)
secondslist.append(second2)
secondslist.append(second1)
secondslist.append(second0)

#All the colored blocks
black1= Color(0x000000, 1)
black2 = Color(0x292929, 1)
black2 = Color(0x404040, 1)
black3 = Color(0x545454, 1)
black4 = Color(0x6E6E6E, 1)
black5 = Color(0x7A7A7A, 1)
black6 = Color(0x8C8C8C, 1)
black7 = Color(0xB0B0B0, 1)
black8 = Color(0xCFCFCF, 1)
black9 = Color(0xE3E3E3, 1)
black10 = Color(0xF5F5F5, 1)
black11 = Color(0xFCFCFC, 1)
thinline1 = LineStyle(1, black1)
thinline2 = LineStyle(1, black2)
thinline3 = LineStyle(1, black3)
thinline4 = LineStyle(1, black4)
thinline5 = LineStyle(1, black5)
thinline6 = LineStyle(1, black6)
thinline7 = LineStyle(1, black7)
thinline8 = LineStyle(1, black8)
thinline9 = LineStyle(1, black9)
thinline10 = LineStyle(1, black10)
thinline11 = LineStyle(1, black11)
rectangle1 = RectangleAsset(50, 50, thinline1, black1)
rectangle2 = RectangleAsset(50, 50, thinline2, black2)
rectangle3 = RectangleAsset(50, 50, thinline3, black3)
rectangle4 = RectangleAsset(50, 50, thinline4, black4)
rectangle5 = RectangleAsset(50, 50, thinline5, black5)
rectangle6 = RectangleAsset(50, 50, thinline6, black6)
rectangle7 = RectangleAsset(50, 50, thinline7, black7)
rectangle8 = RectangleAsset(50, 50, thinline8, black8)
rectangle9 = RectangleAsset(50, 50, thinline9, black9)
rectangle10 = RectangleAsset(50, 50, thinline10, black10)
rectangle11 = RectangleAsset(50, 50, thinline11, black11)
blocklist.append(Sprite(rectangle1, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle2, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle3, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle4, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle5, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle6, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle7, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle8, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle9, (random.randint(0, 1678), random.randint(0, 772))))
blocklist.append(Sprite(rectangle10, (random.randint(0, 1678), random.randint(0, 772))))
rect11 = Sprite(rectangle11, (random.randint(0, 1678), random.randint(0, 772)))
blocklist.append(rect11)


starttime = time.time()
print(starttime)
secondssincestart = 0

#Timer
def step():
    global secondslist
    global secondssincestart
    timenow = time.time()
    secondssincestart = int(timenow-starttime)
    secondslist[secondssincestart].visible = True

#Win/Lose message
youwin = TextAsset("Congrats, you win!!")
youlose = TextAsset("Sorry, but you lose ... :(")
for s in secondslist:
    s.visible = False
for s in blocklist:
    s.visible = False
blocklist[0].visible = True

wintext = Sprite(youwin, (0, 0))
wintext.visible = False
losetext = Sprite(youlose, (0, 365)
blockcount = 0

#Mouse clicks
def mouseClick(event):
    global blockcount
    thesprite = blocklist[blockcount]
    if blockcount >= len(blocklist):
        return
    if event.x >= blocklist[blockcount].x and event.y >= blocklist[blockcount].y and event.x <= blocklist[blockcount].x + 50 and event.y <= blocklist[blockcount].y + 50:
        if event.x >= rect11.x and event.y >= rect11.y and event.x <= rect11.x + 50 and event.y <= rect11.y + 50:
            wintext.visible = True
        
        blocklist[blockcount].visible = False
        blockcount = blockcount + 1
        blocklist[blockcount].visible = True
        
myapp = App()
myapp.listenMouseEvent('click', mouseClick)
myapp.run(step)
