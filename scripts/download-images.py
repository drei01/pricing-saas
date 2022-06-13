#!/usr/bin/env python3
import argparse
import csv
import logging
import os
import sys
import requests
import re
from pathlib import Path

_outoutDirPath = './images/'

def merge(input_file, extra_args):
    tempdir_path = Path(_outoutDirPath)
    logging.debug(f'Using temporary directory {tempdir_path}.')
    with input_file.open(encoding="utf-8-sig") as csvfile:
        for i, row in enumerate(csv.DictReader(csvfile)):
            filename = re.sub('[^0-9a-zA-Z]+', '', row['Name'].lower())
            url = row['Logo']
            print(url)
            result = requests.get(url, stream=True)
            if result.status_code == 200:
                image = result.raw.read()
                open((tempdir_path/filename).with_suffix('.jpg'),"wb").write(image)


def main():
    # Parse commandline arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-v', '--verbose', action='store_true')
    arg_parser.add_argument('input', type=Path)
    args, extra_args = arg_parser.parse_known_args()
    # Set up logging
    if args.verbose:
        level = logging.DEBUG
    else:
        level = logging.ERROR
    logging.basicConfig(level=level)
     # create the output directory
    try:
        if not os.path.exists(_outoutDirPath):
            os.makedirs(_outoutDirPath)
    except OSError:
        print (f'Error: Creating directory.: {_outoutDirPath}')
    # empty output directory
    for root, dirs, files in os.walk(_outoutDirPath):
        for file in files:
            os.remove(os.path.join(root, file))
    # Return exit value
    merge(args.input, extra_args)
    return 0


if __name__ == '__main__':
    sys.exit(main())
