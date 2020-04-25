import argparse
from time import sleep
import random

"""
Reads text from a file or files and writes it out character by character to stdout.
"""

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--rsmin', type=float,
                    help='shortest amount of time passed before a character can be printed. Must be provided along with --random_speed_max')
parser.add_argument('--rsmax', type=float,
                    help='longest amount of time passed before a character can be printed. Must be provided along with --random_speed_min')
parser.add_argument('--sdir', type=str,
                    help='if reading snippets from a single directory, provide the directory with this and it will '
                         'be applied to all snippets passed in to --files_to_read ')
parser.add_argument('--ftr', type=str, required=True, nargs='+',
                    help='a list of files to read, in order passed')
args, leftover = parser.parse_known_args()

sleep_time = .01
speed_min = sleep_time
speed_max = sleep_time

if args.rsmin and args.rsmax:
    speed_min = args.rsmin
    speed_max = args.rsmax

files_to_read = args.ftr
if args.sdir:
    files_to_read = [args.sdir + file for file in files_to_read]


def main():
    files = files_to_read
    for file in files:
        with open(file, "r") as snippet:
            lines = snippet.readlines()
            for line in lines:
                for char in line:
                    sleep(random.uniform(speed_min, speed_max))
                    print(char, sep='', end='', flush=True)


if __name__ == '__main__':
    main()
