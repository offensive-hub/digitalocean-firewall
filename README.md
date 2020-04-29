# ![](https://cloud.digitalocean.com/favicon.png) Update DigitalOcean Firewalls with CloudFlare IPs

A little script to update **DigitalOcean** firewalls with right **CloudFlare** IPs.

This is useful to protect your backends against direct **DoS** and **DDoS** attacks on ports **80** and **443**.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/DigitalOcean_logo.svg/150px-DigitalOcean_logo.svg.png)
![](https://upload.wikimedia.org/wikipedia/en/6/65/Cloudflare_logo.png)

## Table of Contents

- [Warning](#-warning-)
- [How to install](#how-to-install)
- [Example](#example)
- [Make cron](#make-cron)

### ![](https://raw.githubusercontent.com/offensive-hub/digitalocean-firewall/master/resources/danger_icon.png?v=1) Warning ![](https://raw.githubusercontent.com/offensive-hub/digitalocean-firewall/master/resources/danger_icon.png?v=1)

All **Inbound Rules** with `type = HTTP` or `type = HTTPS` of each **Firewall**  will be overwritten.


### How to install

 1) `git clone https://github.com/offensive-hub/digitalocean-firewall.git`
 2) `cd digitalocean-firewall`
 3) `sudo apt-get install python-pip && sudo pip install -U -r requirements.txt`
 4) `cp .env.example .env && chmod 600 .env`
 5) Write right [Digital Ocean Access Token](https://www.digitalocean.com/docs/apis-clis/api/create-personal-access-token/) in **.env** file

### Example

 1) Create an **Inbound Rule** with type **HTTP** or **HTTPS** as following:
    ![](https://raw.githubusercontent.com/offensive-hub/digitalocean-firewall/master/resources/cloudflare_ips_empty.jpg)
 2) Execute `./update-firewalls.py` to update these DigitalOcean Inbound Rules.
 3) Now you have two **Inbound Rules** containing the following **Sources**:
    ![](https://raw.githubusercontent.com/offensive-hub/digitalocean-firewall/master/resources/cloudflare_ips_done.jpg)

### Make cron

It would be useful to make a **cron**, which update the firewalls every **X** time.

If you want that, follow these instructions:

 1) `crontab -e`
 2) Paste the following code at the end of file:
    ```
    # [00:00] Update DigitalOcean Firewalls with CloudFlare IPs
    0 0 * * * /path/to/digitalocean-firewall/update-firewalls.py
    ```
 3) Edit `/path/to/` with your real **path**
 4) Now your server will automatically update DigitalOcean Firewalls every day at midnight! :)


### Authors

* [Fabrizio Fubelli](https://fabrizio.fubelli.org)

### Thanks to

* [python-digitalocean](https://github.com/koalalorenzo/python-digitalocean)
