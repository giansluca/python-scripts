import itertools
import string
import collections


def encrypt(message, key, multipler=-1) -> str:
    compressed_message = message.lower()
    for item in str(string.punctuation + " "):
        compressed_message = compressed_message.replace(item, "")

    cycler = itertools.cycle(key.lower())
    long_key = "".join([next(cycler) for _ in range(len(compressed_message))])

    coded = []
    for i in range(len(long_key)):
        chiper_letter = compressed_message[i]
        key_letter = long_key[i]

        chipher_index = string.ascii_lowercase.index(chiper_letter)
        key_index = string.ascii_lowercase.index(key_letter)

        lowercase = collections.deque(string.ascii_lowercase)
        lowercase.rotate(multipler * key_index)

        new_alphabet = "".join(list(lowercase))
        new_character = new_alphabet[chipher_index]

        coded.append(new_character)

    return "".join(coded)


def decrypt(message, key, multipler=-1) -> str:
    return encrypt(message, key, 1)


message = "llkjmlmpadkkc"
key = "thisisalilkey"

decoded = decrypt(message, key)
print(decoded)
