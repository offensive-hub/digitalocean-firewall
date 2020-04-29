"""
*********************************************************************************
*                                                                               *
* cloudflare.py -- CloudFlare class.                                            *
*                                                                               *
*********************************************************************************
*                                                                               *
* This script search all firewalls with at least one "Inbound Rule" with type   *
* HTTP or HTTPS and then update that by accepting only CloudFlare IPs.          *
*                                                                               *
*********************************************************************************
"""

import requests

from app.env import CLOUDFLARE_IPS_V4_URL, CLOUDFLARE_IPS_V6_URL
from app.frontend.abstract_frontend import AbstractFrontend


class CloudFlare(AbstractFrontend):
    @staticmethod
    def get_ips():
        """
        :rtype: list
        """
        if CloudFlare.__ips is not None:
            return CloudFlare.__ips
        CloudFlare.__ips = []
        for url in CloudFlare.__ip_urls:
            CloudFlare.__ips += requests.get(url).text.split()
        return CloudFlare.__ips

    __ip_urls = (
        CLOUDFLARE_IPS_V4_URL,
        CLOUDFLARE_IPS_V6_URL
    )

    __ips = None
