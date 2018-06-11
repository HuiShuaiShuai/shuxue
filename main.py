#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse


opts = argparse.ArgumentParser(add_help=False)
group = opts.add_argument_group('Command')
group.add_argument('add')
group.add_argument('run')
group.add_argument('push')
group = opts.add_argument_group('Option')
group.add_argument('-v', '--version', action='store_true', help='show version and exit')
group.add_argument('-h', '--help', action='store_true', help='show help and exit')


def download(url):
    pass


def main(args):
    print(args)
    opts.print_help()


if __name__ == '__main__':
    main(sys.argv[1:])