# performs nmap scan on given ip address

import os


def nmap(options, ip):
    """executes nmap tool upon given ip address"""
    command = "nmap " + options + "  " + ip
    process = os.popen(command)  # opens command line and executes nmap
    results = str(process.read())
    return results
