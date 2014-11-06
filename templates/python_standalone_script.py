#!/usr/bin/env python
# -*- coding: utf-8 -*-

__description__ = ''

# ---------------------------------------------------------------------------
# Standard imports:
import sys
import argparse

# Third party imports

# Local imports

# ---------------------------------------------------------------------------


# TODO: Functions / classes here

def parse_args(argv):
    """ Parse and validate command line arguments """
    parser = argparse.ArgumentParser(description=__description__)
    # TODO: Add arguments here
    # parser.add_argument()

    args = parser.parse_args(argv[1:])
    # TODO: Add validation here
    # if args.blah: parser.error("error")

    return args


def main(argv=[__name__]):
    """ Run this program """
    args = parse_args(argv)
    try:

        # TODO: main code here
        args

    except KeyboardInterrupt:
        sys.exit(-1)

if __name__ == '__main__':
    sys.exit(main(sys.argv) or 0)
