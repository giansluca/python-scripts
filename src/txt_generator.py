
import random
import string

filename = "largefile.txt"
size = 1024 * 1024 * 100

chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])

with open(filename, 'w') as f:
    f.write(chars)
