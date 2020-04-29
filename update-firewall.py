#!/usr/bin/env python2
# coding=utf-8

import digitalocean

from env import DIGITALOCEAN_BASE_URL, DIGITALOCEAN_ACCESS_TOKEN, \
    CLOUDFLARE_IPS_V4_URL, CLOUDFLARE_IPS_V6_URL


def main():
    if DIGITALOCEAN_ACCESS_TOKEN is None:
        raise ValueError('DIGITALOCEAN_ACCESS_TOKEN environment cannot be None!')

    print('DIGITALOCEAN_BASE_URL: ' + DIGITALOCEAN_BASE_URL)
    print('DIGITALOCEAN_ACCESS_TOKEN: ' + DIGITALOCEAN_ACCESS_TOKEN)
    print('CLOUDFLARE_IPS_V4_URL: ' + CLOUDFLARE_IPS_V4_URL)
    print('CLOUDFLARE_IPS_V6_URL: ' + CLOUDFLARE_IPS_V6_URL)

    return


if __name__ == '__main__':
    main()
