#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     07/01/2015
# Copyright:   (c) User 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import time
import os
import sys
import re
import mechanize
import cookielib
import logging
import urllib2
import httplib
import random
import glob
import ConfigParser
import HTMLParser
import json
import shutil
import pickle
import socket
import hashlib
import string
import argparse
import BeautifulSoup

from utils import *





# Functions to work with the archive pages
def archive_parse_for_post_ids(page_html):
    """foo"""
    post_ids_regex = """data\-post\-id\=['"](\d+)['"]"""
    post_ids = re.findall(post_ids_regex, page_html, re.IGNORECASE|re.DOTALL)
    return post_ids

def archive_find_next_page_url(base_url,page_html):
    """foo"""
    next_page_link_regex = """<a\s+id=["']next_page_link["']\s+href=["'](/archive\?before_time=1405480755)["']>"""
    next_page_link_search = re.search(next_page_link_regex, page_html, re.IGNORECASE|re.DOTALL)
    next_page_sublink = next_page_link_search.group(1)
    next_page_url = base_url+next_page_sublink
    return next_page_url



def archive_get_post_list(user):
    """foo"""
    all_post_ids = []
    base_url = "http://"+user+".tumblr.com"
    first_archive_url = base_url+"/archive"
    next_page_link = first_archive_url
    # Loop over archive pages
    last_page_post_ids = []
    c = 0
    while (c <= 10):
        c += 1
        logging.debug("next_page_link:"+repr(next_page_link))
        page_html = get(next_page_link)
        this_page_post_ids = archive_parse_for_post_ids(page_html)
        logging.debug("this_page_post_ids:"+repr(this_page_post_ids))
        # stop if two pages have the same data
        if this_page_post_ids == last_page_post_ids:
            logging.info("Last pages IDs are the same as this ones!")
            break
        all_post_ids += this_page_post_ids
        next_page_link = archive_find_next_page_url(base_url,page_html)
    return all_post_ids





def main():
    # Setup logging
    setup_logging(os.path.join("debug","tumblr_to_db_log.txt"))
    try:
        global cj
        cj = cookielib.LWPCookieJar()
        setup_browser(cj)
        return
    except Exception, err:
        # Log exceptions
        logging.critical("Unhandled exception!")
        logging.critical(repr( type(err) ) )
        logging.exception(err)
    logging.info( "Program finished.")

if __name__ == '__main__':
    main()



# Testing

post_list = archive_get_post_list("argoth")
logging.info("post_list:"+repr(post_list))
archive_html = get("http://argoth.tumblr.com/archive")
save_file("arc.html",archive_html)
post_ids = archive_parse_for_post_ids(archive_html)
logging.info(post_ids)

