#!/usr/bin/env python3

__author__ = 'Jan Nash'
__version__ = "0.1"
__license__ = "BSD-3-Clause"

VERSION = "%s v" + __version__

import os
import logging



class Template():
    def __init__(self, xcode_version='10.1 (10B61)', platform='macOS', os_version='10.14', template_type='command line tool'):
        self.xcode_version = xcode_version
        self.platform = platform
        self.os_version = os_version
        self.template_type = template_type
        logging.debug('Created Template ')

    def __repr__(self):
        return 'Template({}, {}, {}, {})'.format(self.xcode_version, self.platform, self.os_version, self.template_type)

    @property
    def path_relative_to_template_folder(self):
        return 


def download_template(template: Template):
    pass


def parse_args():
    """
    Parses command-line arguments and returns the parsed namespace-object.
    """
    import argparse

    parser = argparse.ArgumentParser(version=VERSION)

    parser.add_argument(
        '-d', '--debug',
        action='store_true', default=False, dest='debug',
        help='Set logging level to DEBUG. Beware, it\'s gonna be verbose :).')

    return parser.parse_args()


def main(cmd_args):
    if cmd_args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    cl_args = parse_args()
    main(cl_args)
