#!/usr/bin/env python3
import sys
import argparse
import logging
import csv
import os
import datetime
import shutil
import re
from pathlib import Path

_outoutDirPath = './data/'

def merge(input_file, csv_file, output_file, filename, extra_args):
    tempdir_path = Path(_outoutDirPath)
    logging.debug(f'Using temporary directory {tempdir_path}.')
    with csv_file.open(encoding="utf-8-sig") as csvfile:
        for i, row in enumerate(csv.DictReader(csvfile)):
            row["Date"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            logoName = re.sub('[^0-9a-zA-Z]+', '', row['Name'].lower())
            row["Logo"] = f'/img/tools/customer-portal/{logoName}.jpg'
            tool = re.sub('[^0-9a-zA-Z]+', '', row['Name'].lower())
            tmpname = f'{tool}-{filename}'
            tmppath = (tempdir_path / tmpname).with_suffix(output_file.suffix)
            shutil.copyfile(input_file, tmppath)
            with open(tmppath, 'r') as file :
              filedata = file.read()

            for key in row:
                filedata = filedata.replace(f'{{{{{key}}}}}', str(row[key]))

            with open(tmppath, 'w') as file:
              file.write(filedata)


def main():
    # Parse commandline arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-v', '--verbose', action='store_true')
    arg_parser.add_argument('--csv', type=Path)
    arg_parser.add_argument('-o', '--outfile', type=Path)
    arg_parser.add_argument('input', type=Path)
    arg_parser.add_argument('-filename', type=str)
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
    merge(args.input, args.csv, args.outfile, args.filename, extra_args)
    return 0


if __name__ == '__main__':
    sys.exit(main())