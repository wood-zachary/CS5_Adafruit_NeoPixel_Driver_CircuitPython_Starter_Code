from .lights_out import run_lights_out

def run(
    *,
    pixels=None
):
    """
    Runs the selected demo on the Trinkey.

    Args:
        pixels      — LEDController
    """
    run_lights_out(pixels)