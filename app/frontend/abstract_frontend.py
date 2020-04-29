"""
*********************************************************************************
*                                                                               *
* abstract_frontend.py -- Abstract Frontend class.                              *
*                                                                               *
*********************************************************************************
*                                                                               *
* This script search all firewalls with at least one "Inbound Rule" with type   *
* HTTP or HTTPS and then update that by accepting only CloudFlare IPs.          *
*                                                                               *
*********************************************************************************
"""


class AbstractFrontend:
    """
    Abstract frontend
    """

    def __init__(self):
        pass

    @staticmethod
    def get_ips():
        """
        :rtype: list
        """
        raise NotImplementedError("Abstract method get_ips")
