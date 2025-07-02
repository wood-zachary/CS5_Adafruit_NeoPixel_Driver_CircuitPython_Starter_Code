import board
import busio
from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.neopixel import NeoPixel, GRBW

_I2C_ADDR = 0x60
_PIXEL_PIN = 15
_NUM_PIXELS = 10
_BRIGHTNESS = 0.1

def setup() -> NeoPixel:
    i2c = busio.I2C(board.SCL, board.SDA)
    ss  = Seesaw(i2c, addr=_I2C_ADDR)
    strip = NeoPixel(ss, _PIXEL_PIN, _NUM_PIXELS,brightness=_BRIGHTNESS,pixel_order=GRBW)

    return strip