#!/usr/bin/python
from utils.summarize import summarize
import csv
import shutil
import os
import textwrap
import logging
import argparse
import sys


def parse_args(argv):
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            A command line utility for website summarization.
            -----------------------------------------------
            These are common commands for this app.'''))
    parser.add_argument(
        'action',
        help='This action should be summarize')
    parser.add_argument(
        '--url',
        help='A link to the website url'
    )
    parser.add_argument(
        '--sentence',
        help='Argument to define number of sentence for the summary',
        type=int,
        default=2)
    parser.add_argument(
        '--language',
        help='Argument to define language of the summary',
        default='English')
    parser.add_argument(
        '--path',
        help='path to csv file')

    return parser.parse_args(argv[1:])


def readCsv(path):
    print('\n\n Processing Csv file \n\n')
    sys.stdout.flush()
    data = []
    try:
        with open(path, 'r') as userFile:
            userFileReader = csv.reader(userFile)
            for row in userFileReader:
                data.append(row)
    except:
        with open(path, 'r', encoding="mbcs") as userFile:
            userFileReader = csv.reader(userFile)
            for row in userFileReader:
                data.append(row)       
    return data


def writeCsv(data, LANGUAGE, SENTENCES_COUNT):
    print('\n\n Updating Csv file \n\n')
    sys.stdout.flush()
    with open('beneficiary.csv', 'w') as newFile:
        newFileWriter = csv.writer(newFile)
        length = len(data)
        position = data[0].index('website')
        for i in range(1, length):
            if i == 1:
                _data = data[0]
                _data.append("summary")
                newFileWriter.writerow(_data)
            try:
                __data = data[i]
                summary = summarize(
                    (data[i][position]), LANGUAGE, SENTENCES_COUNT)
                __data.append(summary)
                newFileWriter.writerow(__data)
            except:
                print('\n\n Error Skipping line \n\n')
                sys.stdout.flush()


def processCsv(path, LANGUAGE, SENTENCES_COUNT):
    try:
        print('\n\n Proessing Started \n\n')
        sys.stdout.flush()
        data = readCsv(path)
        writeCsv(data, LANGUAGE, SENTENCES_COUNT)
    except:
        print('\n\n Invalid file in file path \n\n')
        sys.stdout.flush()


def main(argv=sys.argv):
        # Configure logging
    logging.basicConfig(filename='applog.log',
                        filemode='w',
                        level=logging.INFO,
                        format='%(levelname)s:%(message)s')
    args = parse_args(argv)
    action = args.action
    url = args.url
    path = args.path
    LANGUAGE = "english" if args.language is None else args.language
    SENTENCES_COUNT = 2 if args.sentence is None else args.sentence
    if action == 'bulk':
        if path is None:
            print(
                '\n\n Invalid Entry!, please Ensure you enter a valid file path \n\n')
            sys.stdout.flush()
            return
        # guide against errors
        try:
            processCsv(path, LANGUAGE, SENTENCES_COUNT)
        except:
            print(
                '\n\n Invalid Entry!, please Ensure you enter a valid file path \n\n')
            sys.stdout.flush()
        print('Completed')
        sys.stdout.flush()
        if os.path.isfile('beneficiary.csv'):
            return shutil.move('beneficiary.csv', path)
        return
    if action == 'simple':
        # guide against errors
        try:
            summarize(url, LANGUAGE, SENTENCES_COUNT)
        except:
            print(
                '\n\n Invalid Entry!, please Ensure you enter a valid web link \n\n')
            sys.stdout.flush()
        print('Completed')
        sys.stdout.flush()
    else:
        print(
            '\nAction command is not supported\n for help: run python3 app.py -h'
        )
        sys.stdout.flush()
        return


if __name__ == '__main__':
    main()
