"""
*********************************************************************************
*                                                                               *
* digitalocean_manager.py -- DigitalOcean Manager class.                        *
*                                                                               *
*********************************************************************************
"""

# noinspection PyPackageRequirements
import digitalocean

from app.backend.digitalocean import DigitalOceanFirewall


class DigitalOceanManager(digitalocean.Manager):
    """
    DigitalOcean Manager Class
    """
    def get_all_firewalls(self):
        """
        This function returns a list of DigitalOceanFirewall objects.
        """
        data = self.get_data("firewalls")
        firewalls = list()
        for jsoned in data['firewalls']:
            firewall = DigitalOceanFirewall(**jsoned)
            firewall.token = self.token
            in_rules = list()
            for rule in jsoned['inbound_rules']:
                in_rules.append(digitalocean.InboundRule(**rule))
            firewall.inbound_rules = in_rules
            out_rules = list()
            for rule in jsoned['outbound_rules']:
                out_rules.append(digitalocean.OutboundRule(**rule))
            firewall.outbound_rules = out_rules
            firewalls.append(firewall)
        return firewalls
