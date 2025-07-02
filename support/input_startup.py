import time
import usb_cdc

def start_input() -> None:
    time.sleep(0.5)
    while not usb_cdc.console.connected:
        time.sleep(0.1)