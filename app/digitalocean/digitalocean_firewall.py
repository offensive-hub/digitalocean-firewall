"""
*********************************************************************************
*                                                                               *
* digitalocean_firewall.py -- DigitalOcean Firewall class.                      *
*                                                                               *
*********************************************************************************
*                                                                               *
* This script search all firewalls with at least one "Inbound Rule" with type   *
* HTTP or HTTPS and then update that by accepting only CloudFlare IPs.          *
*                                                                               *
*********************************************************************************
"""

import jsonpickle

# noinspection PyPackageRequirements
import digitalocean


class DigitalOceanFirewall(digitalocean.Firewall):
    """
    DigitalOcean Firewall Class
    """
    def update(self):
        inbound = jsonpickle.encode(self.inbound_rules, unpicklable=False)
        outbound = jsonpickle.encode(self.outbound_rules, unpicklable=False)
        params = {
            'name': self.name,
            'droplet_ids': self.droplet_ids,
            'inbound_rules': jsonpickle.decode(inbound),
            'outbound_rules': jsonpickle.decode(outbound),
            'tags': self.tags
        }

        data = self.get_data(
            'firewalls/',
            type=digitalocean.baseapi.PUT,
            params=params
        )

        if data:
            self._set_firewall_attributes(data)

        return self
