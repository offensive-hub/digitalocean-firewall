"""
*********************************************************************************
*                                                                               *
* digitalocean_firewall.py -- DigitalOcean Firewall class.                      *
*                                                                               *
*********************************************************************************
"""

import jsonpickle

# noinspection PyPackageRequirements
import digitalocean


class DigitalOceanFirewall(digitalocean.Firewall):
    def __init__(self, *args, **kwargs):
        super(DigitalOceanFirewall, self).__init__(*args, **kwargs)
        DigitalOceanFirewall.__fix_rules(self.inbound_rules)
        DigitalOceanFirewall.__fix_rules(self.outbound_rules)

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
            "firewalls/%s" % self.id,
            type=digitalocean.baseapi.PUT,
            params=params
        )

        if data:
            self._set_firewall_attributes(data)

        return self

    @staticmethod
    def __fix_rules(rules):
        """
        By default, some rule object values are wrong.
        This method fix those values.
        :type rules: list
        """
        for rule in rules:
            if rule.get('protocol') == 'icmp':
                # if protocol is 'icmp', according with documentation on
                # https://developers.digitalocean.com/documentation/v2/#update-a-firewall,
                # the ports is None
                rule['ports'] = None
            if rule.get('ports') == '0':
                # ports = 0 means 'all' ports
                rule['ports'] = 'all'
