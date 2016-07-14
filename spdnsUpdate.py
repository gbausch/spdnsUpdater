#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Usage:
# spdnsUpdate.py <hostname> <user> <passwd>
# spdnsUpdate.py <hostname> <token>
#
# Copyright 2013 -- Michael Nowak
#
# Update (2016-07-14) by Gerold Bausch
# - new option to obtain ip address
# - new URL and https support provided by spdny.de
# - added token functionality

import urllib
from requests import get

url_ip     = "https://api.ipify.org"
url_update = "https://update.spdyn.de/nic/update"

def dns_update(params, ip):

    response = urllib.urlopen(url_update, params)
    body = response.read()

    code = body.split(' ', 1)[0]
    if code == 'good':
        return True
    elif code == 'nochg':
        ip_current = body.split(' ', 1)[-1]

        if ip == ip_current:
            return True
        else:
            return False
    else:
        return False

def main(argv):
    if len(argv) == 4:
        # get args
        hostname = argv[1]
        user     = argv[2]
        passwd   = argv[3]

        # get ip address
        ip = get(url_ip).text

        # update ip address
        if hostname and user and passwd:
            # parameters for username/password based update
            params = urllib.urlencode({'hostname': hostname, 'myip': ip, 'user': user, 'pass': passwd})
            return dns_update(params, ip)
        else:
            return False

    elif len(argv) == 3:
        # get args
        hostname = argv[1]
        token    = argv[2]

        # get ip address
        ip = get(url_ip).text

        # update ip address with token
        if hostname and token:
            # parameters for token based update
            params = urllib.urlencode({'hostname': hostname, 'myip': ip, 'user': hostname, 'pass': token})
            return dns_update(params, ip)
        else:
            return False
    else:
        print ''
        print "\tUSAGE:         " + __file__ + ' <hostname> <user> <passwd>'
        print "\tUSAGE w/token: " + __file__ + ' <hostname> <token>'
        print ''
        return None

if __name__ == '__main__':
    import sys
    main(sys.argv)
