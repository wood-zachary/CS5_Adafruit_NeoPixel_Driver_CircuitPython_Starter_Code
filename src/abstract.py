"""Collection of abstract classes for use reference.

(For students: don't worry about the code that's in here.
These classes are just providing examples of how to use the sensors and controllers.
The actual implementations of the classes are on the device.)
"""

class LEDController:
    """Abstract LED controller."""

    def fill(self, color: tuple[int, int, int]) -> None:
        """
        Set all LEDs to the given RGB color.
        Args:
            color: (r, g, b) each 0–255.
        Example:
            leds.fill((0,0,0))  # turn off
        """
        raise NotImplementedError