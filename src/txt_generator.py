
import random
import string


def generateLargeFile() -> None:
    filename = "largefile.txt"
    size = 1024 * 1024

    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])

    with open(filename, 'w') as f:
        f.write(chars)
