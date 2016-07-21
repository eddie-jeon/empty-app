from ggame import App, RectangleAsset, ImageAsset, SoundAsset, Sprite, Sound
from ggame import LineStyle, Color

# A ball! This is already in the ggame-tutorials repository
ball_asset = ImageAsset("orb-150545_640.png")
ball = Sprite(ball_asset, (0, 0))
ball.fxcenter = 0.6
ball.fyxenter = 0.6
ball.scale = 0.05

# Handle the mouse movement
def mouseMove(event):
    ball.x = event.x
    ball.y = event.y

myapp = App()
myapp.listenMouseEvent('mousemove', mouseMove)
myapp.run()
