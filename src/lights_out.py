import time
import random
from adafruit_seesaw.neopixel import NeoPixel
from support.mytyping import NoReturn
from support.input_startup import start_input

MAGENTA: tuple[int, int, int] = (255, 0, 255)
OFF: tuple[int, int, int] = (0, 0, 0)
TIME: int = 1
RANDOM_MOVES: int = 10


def set_board(board: list[int]) -> None:
  # Your code here!


def toggle(board: list[int], light_idx: int) -> None:
  # Your code here!


def is_possible_move(idx: int, board: list[int]) -> bool:
  # Your code here!


def randomize_board(board: list[int], moves: int) -> None:
  # Your code here!
  

def show_board(board: list[int], strip: NeoPixel) -> None: 
  # Your code here!


def is_solved(board: list[int]) -> bool: 
  # Your code here!


def run_lights_out(strip: NeoPixel) -> NoReturn:
  start_input()
  
  length = len(strip)  # type: ignore[call-arg]
  board = [0] * length
  moves = 0
  
  set_board(board)
  strip.fill(OFF)
  strip.show()

  random.seed(int(time.monotonic_ns()))
  randomize_board(board, RANDOM_MOVES)
  show_board(board, strip)

  print("\n1D Lights Out")
  print(f"Enter an index [0–{length - 1}] to flip that pixel and its neighbors.")

  while True:
    try:
      entry = input().strip()
    except:
      continue

    # Your code here!