#!/usr/bin/python

import argparse
from pathlib import Path
from sys import stderr, stdout
import os

class CatError(Exception):
    pass

class Logger:
    def __init__(self, verbosity=False):
        self.verbose = verbosity

    def error(self, message):
        print(f'ERROR: {message}')

logger = Logger()

'''
    Read the selected text file 

    Example:
    your/path/file.txt
'''
def readFile(src: Path):

    '''
        if the given path is a directory
        ERROR the path is a directory
    '''
    if src.is_dir():

        logger.error(f'The path {src}: is a directory')

    else:

        with open(src, 'r') as f:
            for lines in f:
                print(lines, end='')

def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='cat',
        description='cat command implementation in python',
        epilog='Example: your/path/file.txt'
    )

    parser.add_argument(
        'source',
        type=Path,
        help='Source file'
    )

    return parser.parse_args()

def main():

    args = cli()

    try:

        readFile(args.source)

    except CatError as e:

        logger.error(e)

        exit(1)

    except KeyboardInterrupt:

        logger.error('\nInterrupt')

'''
    Start the program
'''
if __name__ == '__main__':
    main()
