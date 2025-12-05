import fridge.grocery as G
from fridge.tui import run_tui
# gon have to import argp here
# honestly just import processes for project
import sys

def main():
    grocery = G.startup()
    # either run tui in a loop or just do what args ask
    if len(sys.argv) == 1:
        while True:
            run_tui(grocery)
    else:
        print("would have run argparser")

if __name__ == "__main__":
    main()
