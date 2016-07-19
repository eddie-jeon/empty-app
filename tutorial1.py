from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three primary colors with no transparency (alpha = 1.0)
red = Color(0xF2527B, 0.7)
yellow = Color(0xEDF55F, 0.7)
blue = Color(0x64BBF5, 0.7)
black = Color(0x000000, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(50, 50, thinline, red)
rectangle2 = RectangleAsset(50, 50, thinline, blue)
rectangle3 = RectangleAssets(50, 50, thinline, yellow)

# Now display a rectangle
Sprite(rectangle, (200, 160))
Sprite(rectangle2, (225, 180))
Sprite(rectangle3, (245, 145))

myapp = App()
myapp.run()