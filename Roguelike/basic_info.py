# Defines the basic information of the web app being scanned (domain and ip)

import tld
import socket


def domain_name(url):
    """allows the user to find the domain of the url which they input."""
    new_url = "http://"+url
    domain = tld.get_fld(new_url)
    return domain


def ip_address(url):
    """finds the url of given url"""
    return socket.gethostbyname(url)
