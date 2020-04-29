#!/usr/bin/env python2
# coding=utf-8

"""
*********************************************************************************
*                                                                               *
* update-firewall.py -- Update DigitalOcean Firewalls with CloudFlare IPs.      *
*                                                                               *
*********************************************************************************
*                                                                               *
* This script search all firewalls with at least one "Inbound Rule" with type   *
* HTTP or HTTPS and then update that by accepting only CloudFlare IPs.          *
*                                                                               *
*********************************************************************************
"""

# noinspection PyPackageRequirements
import digitalocean
import requests


from env import DIGITALOCEAN_BASE_URL, DIGITALOCEAN_ACCESS_TOKEN, \
    CLOUDFLARE_IPS_V4_URL, CLOUDFLARE_IPS_V6_URL


def get_safe_frontend_ips():
    """
    :rtype: list
    """
    cloudflare_ip_urls = (
        CLOUDFLARE_IPS_V4_URL,
        CLOUDFLARE_IPS_V6_URL
    )
    ips = []
    for url in cloudflare_ip_urls:
        ips += requests.get(url).text.split()
    return ips


def main():
    if DIGITALOCEAN_ACCESS_TOKEN is None:
        raise ValueError('DIGITALOCEAN_ACCESS_TOKEN environment cannot be None!')

    safe_frontend_ips = get_safe_frontend_ips()

    manager = digitalocean.Manager(token=DIGITALOCEAN_ACCESS_TOKEN, end_point=DIGITALOCEAN_BASE_URL)
    firewalls = manager.get_all_firewalls()

    for firewall in firewalls:
        print(dir(firewall))

    return


if __name__ == '__main__':
    main()
