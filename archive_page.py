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
    """Depreciated! Grab post ids from an archive page HTML"""
    assert False
    post_ids_regex = """data\-post\-id\=['"](\d+)['"]"""
    post_ids = re.findall(post_ids_regex, page_html, re.IGNORECASE|re.DOTALL)
    return post_ids


def archive_parse_for_posts(page_html):
    """Parse archive page HTML and extract pairs of IDs and dates
    Returns list of tuples of strings: [("",""),]"""
    # <div\s+class="post.+data\-post\-id\=['"](\d+)['"].+?<span\s+class=['"]post_date['"]>([^<]+)</span>
    post_info_regex = """<div\s+class="post.+?data\-post\-id\=['"](\d+)['"].+?<span\s+class=['"]post_date['"]>([^<]+)</span>"""
    post_info = re.findall(post_info_regex, page_html, re.IGNORECASE|re.DOTALL)
    return post_info


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
    """Scrape archive listing for a user and collect post IDs and their dates
    Returns a list of tuples of strings: [ ("",""), ]"""
    all_posts = []
    base_url = "http://"+user+".tumblr.com"
    first_archive_url = base_url+"/archive"
    next_page_link = first_archive_url
    # Loop over archive pages
    last_page_posts = []
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
        this_page_posts = archive_parse_for_posts(page_html)
        logging.debug("this_page_posts:"+repr(this_page_posts))
        # Stop if two pages have the same data
        if this_page_posts == last_page_posts:
            logging.info("Last pages data is the same as this ones!")
            break
        all_posts += this_page_posts
        next_page_link = archive_find_next_page_url(base_url,page_html)
        last_page_posts = this_page_posts
        continue
    # Sanity check post list
    if len(all_posts) != len(set(all_posts)):
        logging.error("Duplicate posts in archive page listing results!")
        assert False
    #assert False# This needs changing to find dates for each post!
    logging.debug("all_posts:"+repr(all_posts))
    return all_posts
# End archive page functions






























def main():
    pass

if __name__ == '__main__':
    main()
