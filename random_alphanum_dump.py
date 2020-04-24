from uuid import uuid4
from time import sleep
'''
Generates a stream of random alphanumeric characters
'''

for i in range(10000):
    sleep(.07)
    output = ''
    for s in range(10):
        output += str(uuid4()).replace('-', '')
    print(output)
