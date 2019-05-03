# contains the main functionality of the application

from directories import *
from basic_info import *
from nmap import *
from whois import *
from robots import *


root_dir = "RogueTests"
create_dir(root_dir)

def basic_scan(name, url):
    """gives user a rough overview of the diagnostics of their web app"""
    domain = domain_name(url)
    ip = ip_address(url)
    nm = nmap("-F", ip)
    robots = robots_txt(url)
    who = whois(domain)
    scan_output(name, url, domain, nm, robots, who)


def scan_output(name, url, domain, nmap, robots, whois):
    """creates each file for test results in correlation with the specific tests being run"""
    test_dir = root_dir + "/" + name
    create_dir(test_dir)
    write_file(test_dir + "/url.txt", url)
    write_file(test_dir + "/nmap.txt", nmap)
    write_file(test_dir + "/domain.txt", domain)
    write_file(test_dir + "/robots.txt", robots)
    write_file(test_dir + "/whois.txt", whois)


def main():
    url = input("Please type the url you wish to operate upon: ")
    name = input("Please give a name for the test set: ")
    print("Scanning...")
    basic_scan(name, url)
    print("Test Directory created")


main()
