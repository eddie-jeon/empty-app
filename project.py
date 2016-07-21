from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound
import random
from ggame import LineStyle, Color

blocklist = []

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



    
Sprite(rectangle1, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle2, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle3, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle4, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle5, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle6, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle7, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle8, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle9, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle10, (random.randint(0, 1678), random.randint(0, 772)))
Sprite(rectangle11, (random.randint(0, 1678), random.randint(0, 772)))

for s in blocklist:
    s.visible = False
    
blocklist[0].visible = True

blockcount = 0

blocklist[blockcount].visible = False
blockcount = blockcount + 1
blocklist[blockcount].visible = True

myapp = App()
myapp.run()
