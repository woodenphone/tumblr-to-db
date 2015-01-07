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
from archive_page import *



# Post functions



def post_extract_data(user,post_id):
    """foo"""
    assert_is_string(user)
    assert_is_string(post_id)
    # Load post page
    # http://argoth.tumblr.com/post/73342364076
    post_url = "http://"+user+".tumblr.com/post/"+post_id
    post_page_html = get(post_url)





def post_extract_post_from_background(page_html):
    """Find the main inner post section of the page and return just that section"""
    soup = BeautifulSoup(page_html)
    post_inner_html = soup.find("div", "post")
    return post_inner_html





# End post functions





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

#post_list = archive_get_post_list("argoth")
#logging.info("post_list:"+repr(post_list))

post_extract_data(user="argoth", post_id="73342364076")




page_html = get("http://argoth.tumblr.com/post/73342364076")
soup = BeautifulSoup.BeautifulSoup(page_html)
element =  soup.find("div", "post")
logging.debug(repr(element))



