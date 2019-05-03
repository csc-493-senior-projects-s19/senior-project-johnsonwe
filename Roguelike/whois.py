# reports out information about the stakeholders of the given application

import os


def whois(url):
    """runs the 'whois' tool on the given url"""
    command = "whois " + url
    process = os.popen(command)
    results = str(process.read())
    return results
