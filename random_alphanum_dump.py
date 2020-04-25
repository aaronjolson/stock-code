from uuid import uuid4
from time import sleep
import random
'''
Generates a stream of random alphanumeric characters
'''

for i in range(10000):
    sleep(.07)  # slows output down a bit, crude way to regulate the output speed
    output = ''
    for s in range(random.randint(4, 17)):  # arbitrary range
        output += str(uuid4()).replace('-', '')

    print(output)  # makes newlines
