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

from app.digitalocean import DigitalOceanManager

from app.env import DIGITALOCEAN_BASE_URL, DIGITALOCEAN_ACCESS_TOKEN, \
    CLOUDFLARE_IPS_V4_URL, CLOUDFLARE_IPS_V6_URL


def __get_safe_frontend_ips():
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


HTTP_PORTS = ['80', '443']
SAFE_FRONTEND_IPS = __get_safe_frontend_ips()


def new_firewall_http_inbound_rules():
    """
    :rtype: list
    """
    inbound_rules = []
    for port in HTTP_PORTS:
        inbound_rules.append(
            digitalocean.InboundRule(
                protocol="tcp",
                ports=port,
                sources=digitalocean.Sources(
                    addresses=SAFE_FRONTEND_IPS
                )
            )
        )
    return inbound_rules


def main():
    if DIGITALOCEAN_ACCESS_TOKEN is None:
        raise ValueError('DIGITALOCEAN_ACCESS_TOKEN environment cannot be None!')

    manager = DigitalOceanManager(
        token=DIGITALOCEAN_ACCESS_TOKEN,
        end_point=DIGITALOCEAN_BASE_URL
    )
    firewalls = manager.get_all_firewalls()

    firewall_http_inbound_rules = new_firewall_http_inbound_rules()

    for firewall in firewalls:
        firewall_inbound_rules = []
        update = False
        print 'Checking Firewall "' + firewall.name + '"...'
        for inbound_rule in firewall.inbound_rules:
            if inbound_rule.ports in HTTP_PORTS:
                # The firewall contain an HTTP/S inbound rule, so it will be updated with
                # CloudFlare IPs
                update = True
            else:
                # Add non-HTTP/S rules to firewall_inbound_rules list
                firewall_inbound_rules.append(inbound_rule)

        if not update:
            print 'Firewall "' + firewall.name + '" checked (not update required)!\n'
            continue

        # Extend firewall_inbound_rules list with right HTTP/S inbound rules
        firewall_inbound_rules.extend(firewall_http_inbound_rules)
        firewall.inbound_rules = firewall_inbound_rules
        print(firewall.name)
        print(firewall.inbound_rules)
        print(firewall.outbound_rules)
        print(firewall.droplet_ids)
        print(firewall.tags)
        print 'Firewall "' + firewall.name + '" updated!\n'


if __name__ == '__main__':
    main()
