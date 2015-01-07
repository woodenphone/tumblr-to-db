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
    #
    post_ids_regex = """data\-post\-id\=['"](\d+)['"]"""
    post_ids = re.findall(post_ids_regex, page_html, re.IGNORECASE|re.DOTALL)
    return post_ids


def archive_find_next_page_url(base_url,page_html):
    """foo"""
    #
    next_page_link_regex = """<a\s+id=["']next_page_link["']\s+href=["'](/archive\?before_time=\d+)["']>"""
    next_page_link_search = re.search(next_page_link_regex, page_html, re.IGNORECASE|re.DOTALL)
    next_page_sublink = next_page_link_search.group(1)
    next_page_url = base_url+next_page_sublink
    return next_page_url


def archive_check_if_end_of_posts(page_html):
    """Check if we have reached the end of the archive pages.
    Return True if we have, False otherwise."""
    # <div id="no_posts_yet">No posts yet.</div>
    # <div\s+id=["']no_posts_yet["']>\s*No posts yet.\s*</div>
    next_page_link_regex = """<div\s+id=["']no_posts_yet["']>\s*No posts yet.\s*</div>"""
    next_page_link_search = re.search(next_page_link_regex, page_html, re.IGNORECASE|re.DOTALL)
    if next_page_link_search:
        return True
    else:
        return False


def archive_get_post_list(user,max_pages=100):
    """foo"""
    all_post_ids = []
    base_url = "http://"+user+".tumblr.com"
    first_archive_url = base_url+"/archive"
    next_page_link = first_archive_url
    # Loop over archive pages
    last_page_post_ids = []
    counter = 0
    while (counter <= max_pages):
        counter += 1
        logging.info("Scanning archive page for post ids, page # "+repr(counter))
        logging.debug("next_page_link:"+repr(next_page_link))
        page_html = get(next_page_link)
        # Check if we've reached the end; if so, stop.
        end_reached = archive_check_if_end_of_posts(page_html)
        if end_reached:
            logging.info("Last page of archive listing reached, stopping scan")
            break
        this_page_post_ids = archive_parse_for_post_ids(page_html)
        logging.debug("this_page_post_ids:"+repr(this_page_post_ids))
        # Stop if two pages have the same data
        if this_page_post_ids == last_page_post_ids:
            logging.info("Last pages IDs are the same as this ones!")
            break
        all_post_ids += this_page_post_ids
        next_page_link = archive_find_next_page_url(base_url,page_html)
        last_page_post_ids = this_page_post_ids
        continue
    # Sanity check post list
    if len(all_post_ids) != len(set(all_post_ids)):
        logging.error("Duplicate posts in archive page listing results!")
        assert False
    return all_post_ids
# End archive page functions




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


