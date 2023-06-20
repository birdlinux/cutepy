import os
import re
import platform

from time import sleep


class Loader:

    def spinner(text, time, pattern):
        for i in range(int(time)):
            print(pattern[i % len(pattern)] + " " + text, end="\r")
            sleep(0.3)


class RGB:

    reset = "\033[0m"
    
    def print(r, g, b):
        return "\033[38;2;{};{};{}m".format(r, g, b)


class HEX:

    reset = "\033[0m"

    @staticmethod
    def print(hex_value):
        r, g, b = tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))
        return f"\033[38;2;{r};{g};{b}m"


class Clear:

    def sys():
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


class Color:

    def palette():
        for i in range(8):
            print(f"\033[48;5;{i}m   \033[0m", end="")

        print ("")
        for i in range(8, 16):
            print(f"\033[48;5;{i}m   \033[0m", end="")
        print("")


# Loading
# spinners = ["|", "/", "-", "\\"]
# Loader.spinner("Loading", 4, spinners)

# RGB printing
# x = RGB.print(252, 145, 83)
# print(f"Hello {x}RGB{RGB.reset} test {x}aa")

# HEX printing
# x = HEX.print("fc9153")
# print(f"Hello {x}RGB{RGB.reset} test {x}aa{RGB.reset}")

# Terminal clearance
# Clear.sys()

# Color palette
# Color.palette()
