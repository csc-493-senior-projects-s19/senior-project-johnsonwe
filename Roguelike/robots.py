# finds and reports out webcrawling specifications for the given app

import requests


def robots_txt(url):
    """finds and records the rules for webscrapers on a given page"""
    if url.endswith("/"):
        path = "http://" + url  # adds necessary information to given url for operation
    else:
        path = "http://" + url + "/"
    response = requests.get(path + "robots.txt")
    return(str(response.content))
