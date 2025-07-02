import board
from src.interact import run

try:
    from setup.rp2040_qt_trinkey import setup
    pixels = setup()
    print("Loaded Trinkey LEDs")
except Exception as e:
    pixels = None
    print(f"Skipping Trinkey LEDs: {e!r}")

run(
    pixels=pixels
)