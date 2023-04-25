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


class System:

    def detect():
        if platform.system() == 'Windows':
            return 'Windows'
        elif platform.system() == 'Linux':
            return 'Linux'
        elif platform.system() == 'Darwin':
            return 'macOS'
        elif platform.system() == 'FreeBSD':
            return 'FreeBSD'
        elif platform.system() == 'SunOS':
            return 'Solaris'
        elif platform.system() == 'AIX':
            return 'AIX'
        elif platform.system() == 'Android':
            return 'Android'
        elif platform.system() == 'Cygwin':
            return 'Cygwin'
        elif platform.system() == 'HP-UX':
            return 'HP-UX'
        elif platform.system() == 'IRIX64':
            return 'IRIX64'
        elif platform.system() == 'Java':
            return 'Java'
        elif platform.system() == 'OS/2':
            return 'OS/2'
        elif platform.system() == 'OpenVMS':
            return 'OpenVMS'
        elif platform.system() == 'Tru64':
            return 'Tru64'
        else:
            return 'Unknown'


class Clear:

    def sys():
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')


class Identify:

    def hash(hash):
        if re.match(r'^[a-fA-F0-9]{32}$', hash):
            return "MD5"
        # SHA1
        elif re.match(r'^[a-fA-F0-9]{40}$', hash):
            return "SHA1"
        # SHA256
        elif re.match(r'^[a-fA-F0-9]{64}$', hash):
            return "SHA256"
        # SHA512
        elif re.match(r'^[a-fA-F0-9]{128}$', hash):
            return "SHA512"
        # NTLM
        elif re.match(r'^[a-fA-F0-9]{32}:[a-fA-F0-9]{32}$', hash):
            return "NTLM"
        # LM
        elif re.match(r'^[a-fA-F0-9]{14}:[a-fA-F0-9]{14}$', hash):
            return "LM"
        # MySQL 4.x
        elif re.match(r'^[a-fA-F0-9]{16}$', hash):
            return "MySQL 4.x"
        # MySQL 5.x
        elif re.match(r'^(\$mysql\$\d+\$[a-fA-F0-9]+\$)', hash):
            return "MySQL 5.x"
        # PostgreSQL MD5
        elif re.match(r'^md5[a-fA-F0-9]{32}$', hash):
            return "PostgreSQL MD5"
        # PostgreSQL SCRAM-SHA-256
        elif re.match(r'^SCRAM-SHA-257\$.*$', hash):
            return "PostgreSQL SCRAM-SHA-256"
        # LDAP {SHA}
        elif re.match(r'^\{SHA\}[a-zA-Z0-9+/]{27}=$', hash):
            return "LDAP {SHA}"
        # LDAP {SSHA}
        elif re.match(r'^\{SSHA\}[a-zA-Z0-9+/]{32,}=$', hash):
            return "LDAP {SSHA}"
        # Base64
        elif re.match(r'^[a-zA-Z0-9+/]+={0,2}$', hash):
            return f"Base64"
        # Base32
        elif re.match(r'^[a-zA-Z2-7]+=*$', hash):
            return f"Base32"
        # Base16
        elif re.match(r'^[a-fA-F0-9]+$', hash):
                return f"Base16"
        # Unknown hash
        else:
            return "Unknown hash type"


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

# System detection
# x = System.detect()
# print(x)

# Terminal clearance
# Clear.sys()

# Hash identifier
# x = Identify.hash("a875e3b9476d5d976160b308ace6b62e")
# print(x)

# Color palette
# Color.palette()