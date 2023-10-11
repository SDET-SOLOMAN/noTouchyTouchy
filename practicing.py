import string
import random

letters = string.ascii_lowercase
random_word = ''.join(random.choice(letters) for x in range(8))

print(random_word)