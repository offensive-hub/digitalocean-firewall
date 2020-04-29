# [DigitalOcean] Update Backend Firewalls with CloudFlare IPs

A little script that update DigitalOcean firewalls with right CloudFlare IPs

### Manual installation

 1) `git clone git@github.com:offensive-hub/cloudflare-update-firewall`
 2) `cd cloudflare-update-firewall`
 3) `sudo pip install -U -r requirements.txt`
 4) `cp .env.example .env`
 5) Write right Digital Ocean Access Token in file `.env`
 6) Now you can run the script with: `./update-firewall.py`

### Authors

* [Fabrizio Fubelli](https://fabrizio.fubelli.org)

### Thanks to

* [python-digitalocean](https://github.com/koalalorenzo/python-digitalocean)
