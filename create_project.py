#!/usr/bin/env python3

__author__ = 'Jan Nash'
__version__ = "0.1"
__license__ = "BSD-3-Clause"

VERSION = "%s v" + __version__


def parse_args():
    """
    Parses command-line arguments and returns the parsed namespace-object.
    """
    import argparse
    import os

    parser = argparse.ArgumentParser(version=VERSION)

    parser.add_argument(
        '-d', '--debug',
        action='store_true', default=False, dest='debug',
        help='Set logging level to DEBUG. Beware, it\'s gonna be verbose :).')

    return parser.parse_args()


def main(cmd_args):
    import logging
    
    if cmd_args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    cl_args = parse_args()
    main(cl_args)
