#!/usr/bin/env python3

__author__ = 'Jan Nash'
__version__ = "0.1"
__license__ = "BSD-3-Clause"

VERSION = "%s v" + __version__

import os
import logging


class Template():
    def __init__(self, xcode_version, platform, os_version, template_type):
        self.xcode_version = xcode_version
        self.platform = platform
        self.os_version = os_version
        self.template_type = template_type

    def __repr__(self):
        return "Template('{}', '{}', '{}', '{}')".format(
            self.xcode_version, self.platform, self.os_version, self.template_type)

    @property
    def path_relative_to_template_folder(self):
        return 


AVAILABLE_TEMPLATES = [
    Template('10.1 (10B61)', 'macOS', '10.14', 'command_line_tool'),
]


def download_template(template: Template):
    pass


def parse_args():
    """
    Parses command-line arguments and returns the parsed namespace-object.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            'xcode-project-setup - a tool to quickly setup an xcode project '
            'together with a useful development environment'),
        epilog='Use %(prog)s {command} -h to get help on individual commands')

    parser.add_argument(
        '-v', '--version', 
        action='version', version='%(prog)s ' + VERSION)

    parser.add_argument(
        '-d', '--debug',
        action='store_true', default=False, dest='debug',
        help='Set logging level to DEBUG')

    parser.add_argument(
        '--available-templates',
        action='store_true', dest='available_templates',
        help='Prints all available templates and exits')

    parser.add_argument(
        '-n', '--name',
        action='store', dest='project_name',
        help=(
            'The name of the Xcode project that will be created. This will also be '
            'used as the name for the gemset of the development environment'))

    parser.add_argument(
        '--xcode-version',
        action='store', dest='xcode_version',
        help=(
            'The version of Xcode with which the template was created'))

    return parser.parse_args()


def main(cmd_args):
    if cmd_args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if cmd_args.available_templates:
        print(''.join(['{}) {}\n'.format(i, template) for i, template in enumerate(AVAILABLE_TEMPLATES, start=1)]))


if __name__ == '__main__':
    cl_args = parse_args()
    main(cl_args)
