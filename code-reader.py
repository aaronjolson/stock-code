import argparse
from time import sleep
import random

"""
Reads text from a file or files and writes it out character by character to stdout.
"""

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--random_speed_min', type=float,
                    help='shortest amount of time passed before a character can be printed. Must be provided along with --random_speed_max')
parser.add_argument('--random_speed_max', type=float,
                    help='longest amount of time passed before a character can be printed. Must be provided along with --random_speed_min')
parser.add_argument('--files_to_read', type=list,
                    help='a list of files to read, in order, passed as a python list [..]')
args, leftover = parser.parse_known_args()

sleep_time = .01
# speed_min = sleep_time
# speed_max = sleep_time

speed_min = .0001
speed_max = .2

if args.random_speed_min and args.random_speed_max:
    speed_min = args.random_speed_min
    speed_max = args.random_speed_max


def main():
    files_to_read = ['code_snippet1.txt', 'code_snippet2.txt']
    for file in files_to_read:
        with open(file, "r") as snippet:
            lines = snippet.readlines()
            for line in lines:
                for char in line:
                    sleep(random.uniform(speed_min, speed_max))
                    print(char, sep='', end='', flush=True)


if __name__ == '__main__':
    main()
