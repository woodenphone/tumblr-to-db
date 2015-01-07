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
    post_retreval_date = datetime.now()
    # Extract stuff
    post_html = post_extract_post_from_background(page_html)
    post_tags = post_extract_tags(page_html)





def post_extract_post_from_background(page_html):
    """Find the main inner post section of the page and return just that section"""
    soup = BeautifulSoup.BeautifulSoup(page_html)
    post_inner_html = soup.find("div", "post")
    return post_inner_html

def post_extract_tags(page_html):
    """Find the tags of a post"""
    # <div class="tags">Tagged: <a href="http://argoth.tumblr.com/tagged/otp-challenge">otp challenge</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/30-day-challenge">30 day challenge</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/analingus">analingus</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/handjob">handjob</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/size-difference">size difference</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/artgoth">artgoth</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/zeke">zeke</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/ashe">ashe</a><span class="tag-commas">, </span><a href="http://argoth.tumblr.com/tagged/nsfw">nsfw</a><span class="tag-commas">, </span>.</div>
    # Extract just the tag section to avoid links in post interfering with regex
    soup = BeautifulSoup.BeautifulSoup(page_html)
    tags_html = soup.find("div", "tags")
    # Use regex because BS is tricky
    # <a href="http://argoth.tumblr.com/tagged/otp-challenge">otp challenge</a>
    # <a\s+href=["'][^"']+tumblr.com/tagged/[^"']+["']>([^<]+)</a>
    find_tags_regex = """<a\s+href=["'][^"']+tumblr.com/tagged/[^"']+["']>([^<]+)</a>"""
    tags = re.findall(find_tags_regex, tags_html, re.IGNORECASE|re.DOTALL)
    return tags

def post_extract_media(page_html):
    """Find all media and return the URLS for downloading"""


def post_find_text(page_html):
    """Extract the text section of a post"""


def post_find_number_of_notes(page_html):
    """Find the number of notes for this post"""


def post_find_notes(page_html):
    """Extract the info from the notes section"""


def post_extract_date(page_html):
    """Find the date of the post"""

def post_extract_page_title(page_html):
    """Find the page title of a post"""
    # <title>blahblahblah...</title>
    # <title>([^<]+)</title>
    find_tags_regex = """<<title>([^<]+)</title>"""
    page_title = re.findall(find_tags_regex, tags_html, re.IGNORECASE|re.DOTALL)
    return page_title


def post_extract_page_description(page_html):
    """Extract the description metadata in the page header"""
    # <meta name="description" content="30 days OTP challenge &ldquo;&bull; Cuddles (naked) &bull; Kiss (naked) &bull; First time &bull; Masturbation &bull; Blow job &bull; Clothed getting off &bull; Dressed/naked (half dressed) &bull; Skype sex &bull; Against the wall &bull; Doggy style &bull;..." />
    # <meta name="description" content="blahblahblah" />
    # <meta\s+name="description"\s+content="([^"']+)"\s+/>
    page_description_regex = """<meta\s+name=["']description["']\s+content=["']([^"']+)["']\s+/>"""
    page_description_search = re.search(page_description_regex, page_html, re.IGNORECASE|re.DOTALL)
    page_description = page_description_search.group(1)
    return page_description


def post_extract_page_keywords(page_html):
    """Extract the keywords metadata in the page"""
    # <meta name="keywords" content="zeke,ashe,nsfw,artgoth,size difference" />
    # <meta\s+name=["']keywords["']\s+content=["']([^"']+)["']\s+/>
    page_keywords_regex = """<meta\s+name=["']keywords["']\s+content=["']([^"']+)["']\s+/>"""
    page_keywords_search = re.search(page_keywords_regex, page_html, re.IGNORECASE|re.DOTALL)
    page_keywords = page_keywords_search.group(1)
    return page_keywords


def post_extract_twitter_keywords(page_html):
    """Extract the keywords metadata in the page"""
    # <!-- TWITTER TAGS --><meta charset="utf-8"><meta name="twitter:card" content="photo" /><meta name="twitter:description" content="30 days OTP challenge &ldquo;&bull; Cuddles (naked) &bull; Kiss (naked) &bull; First time &bull; Masturbation &bull; Blow job &bull; Clothed getting off &bull; Dressed/naked (half dressed) &bull; Skype sex &bull; Against the wall &bull; Doggy style &bull;..." /><meta name="twitter:image" content="http://40.media.tumblr.com/bf10286a9ed43682f437bc52cb0d2669/tumblr_mzew5pUxKb1r3mp9eo1_500.png" /><meta name="twitter:url" content="http://argoth.tumblr.com/post/73342364076" /><meta name="twitter:site" content="tumblr" /><meta name="twitter:app:name:iphone" content="Tumblr" /><meta name="twitter:app:name:ipad" content="Tumblr" /><meta name="twitter:app:name:googleplay" content="Tumblr" /><meta name="twitter:app:id:iphone" content="305343404" /><meta name="twitter:app:id:ipad" content="305343404" /><meta name="twitter:app:id:googleplay" content="com.tumblr" /><meta name="twitter:app:url:iphone" content="tumblr://x-callback-url/blog?blogName=argoth&amp;postID=73342364076&amp;referrer=twitter-cards" /><meta name="twitter:app:url:ipad" content="tumblr://x-callback-url/blog?blogName=argoth&amp;postID=73342364076&amp;referrer=twitter-cards" /><meta name="twitter:app:url:googleplay" content="tumblr://x-callback-url/blog?blogName=argoth&amp;postID=73342364076&amp;referrer=twitter-cards" />
    # <meta name="twitter:description" content="BLAHBLAHBLAH" />
    # <meta\s+name=["']twitter:description["']\s+content=["']([^"']+)["']\s+/>
    twitter_keywords_regex = """<meta\s+name=["']twitter:description["']\s+content=["']([^"']+)["']\s+/>"""
    twitter_keywords_search = re.search(twitter_keywords_regex, page_html, re.IGNORECASE|re.DOTALL)
    twitter_keywords = twitter_keywords_search.group(1)
    return twitter_keywords


def post_extract_facebook_keywords(page_html):
    """Extract the tumblr facebook opengraph keywords metadata in the page"""
    # <meta property="og:description" content="30 days OTP challenge..........&bull;..." />
    # <meta\s+property=["']og:description["']\s+content=["']([^"']+)["']\s+/>
    facebook_keywords_regex = """<meta\s+property=["']og:description["']\s+content=["']([^"']+)["']\s+/>"""
    facebook_keywords_search = re.search(facebook_keywords_regex, page_html, re.IGNORECASE|re.DOTALL)
    facebook_keywords = facebook_keywords_search.group(1)
    return facebook_keywords









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
tag_elements = soup.find("div", "tags", "a")
for current_tag in tag_elements:
    print current_tag.string

logging.debug(repr(tags_html))



