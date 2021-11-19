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
# - new URL and https support provided by spdyn.de
# - added token functionality
# Update 2021-11-19 -- Volker Heuermann
# - updated to work with python3
# - added a file so only update with new IP

import urllib
import os
from requests import get
from os import path

url_ip     = "https://api.ipify.org"
url_update = "https://update.spdyn.de/nic/update?%s"
ip_file    = "ipfile"

def dns_update(params, ip):
    url = url_update % params
    response = urllib.request.urlopen(url)
    body = response.read().decode()

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
    # get ip address
    ip = get(url_ip).text

    writemode = 'x'
    filename = os.path.join(os.path.dirname(__file__), ip_file)

    if path.isfile(filename):
        old_ip_file = open(filename, 'r')
        old_ip = old_ip_file.read()
        old_ip_file.close()
        if old_ip == ip:
            return
        writemode = 'w'

    old_ip_file = open(filename, writemode)
    old_ip_file.write(ip)
    old_ip_file.close()

    if len(argv) == 4:
        # get args
        hostname = argv[1]
        user     = argv[2]
        passwd   = argv[3]

        # update ip address
        if hostname and user and passwd:
            # parameters for username/password based update
            params = urllib.parse.urlencode({'hostname': hostname, 'myip': ip, 'user': user, 'pass': passwd})
            return dns_update(params, ip)
        else:
            return False

    elif len(argv) == 3:
        # get args
        hostname = argv[1]
        token    = argv[2]

        # update ip address with token
        if hostname and token:
            # parameters for token based update
            params = urllib.parse.urlencode({'hostname': hostname, 'myip': ip, 'user': hostname, 'pass': token})
            return dns_update(params, ip)
        else:
            return False
    else:
        print ('')
        print ("\tUSAGE:         " + __file__ + ' <hostname> <user> <passwd>')
        print ("\tUSAGE w/token: " + __file__ + ' <hostname> <token>')
        print ('')
        return None

if __name__ == '__main__':
    import sys
    main(sys.argv)
