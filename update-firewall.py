#!/usr/bin/env python2
# coding=utf-8

import sys
import digitalocean

from env import DIGITALOCEAN_BASE_URL, DIGITALOCEAN_ACCESS_TOKEN


def main(args):
    """
    :type args: list
    """
    print(args)
    print('DIGITALOCEAN_BASE_URL: ' + DIGITALOCEAN_BASE_URL)
    print('DIGITALOCEAN_ACCESS_TOKEN: ' + DIGITALOCEAN_ACCESS_TOKEN)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
