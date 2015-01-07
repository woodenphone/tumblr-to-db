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



def add_http(url):
    """Ensure a url starts with http://..."""
    if "http://" in url:
        return url
    elif "https://" in url:
        return url
    else:
        #case //derpicdn.net/img/view/...
        first_two_chars = url[0:2]
        if first_two_chars == "//":
            output_url = "https:"+url
            return output_url
        else:
            logging.error(repr(locals()))
            raise ValueError


def deescape(html):
    # de-escape html
    # http://stackoverflow.com/questions/2360598/how-do-i-unescape-html-entities-in-a-string-in-python-3-1
    deescaped_string = HTMLParser.HTMLParser().unescape(html)
    return deescaped_string


def get(url):
    #try to retreive a url. If unable to return None object
    #Example useage:
    #html = get("")
    #if html:
    assert_is_string(url)
    deescaped_url = deescape(url)
    url_with_protocol = add_http(deescaped_url)
    #logging.debug( "getting url ", locals())
    gettuple = getwithinfo(url_with_protocol)
    if gettuple:
        reply, info = gettuple
        return reply
    else:
        return


def getwithinfo(url):
    """Try to retreive a url. If unable to return None objects
    Example useage:
    html = get("")
        if html:
    """
    attemptcount = 0
    while attemptcount < GET_MAX_ATTEMPTS:
        attemptcount = attemptcount + 1
        if attemptcount > 1:
            delay(GET_RETRY_DELAY)
            logging.debug( "Attempt "+repr(attemptcount)+" for URL: "+repr(url) )
        try:
            save_file(os.path.join("debug","get_last_url.txt"), url, True)
            r = br.open(url, timeout=100)
            info = r.info()
            reply = r.read()
            delay(GET_REQUEST_DELAY)
            # Save html responses for debugging
            #print info
            #print info["content-type"]
            if "html" in info["content-type"]:
                #print "saving debug html"
                save_file(os.path.join("debug","get_last_html.htm"), reply, True)
            else:
                save_file(os.path.join("debug","get_last_not_html.txt"), reply, True)
            # Retry if empty response and not last attempt
            if (len(reply) < 1) and (attemptcount < GET_MAX_ATTEMPTS):
                logging.error("Reply too short :"+repr(reply))
                continue
            return reply,info
        except urllib2.HTTPError, err:
            logging.debug(repr(err))
            if err.code == 404:
                logging.debug("404 error! "+repr(url))
                return
            elif err.code == 403:
                logging.debug("403 error, ACCESS DENIED! url: "+repr(url))
                return
            elif err.code == 410:
                logging.debug("410 error, GONE")
                return
            else:
                save_file(os.path.join("debug","HTTPError.htm"), err.fp.read(), True)
                continue
        except urllib2.URLError, err:
            logging.debug(repr(err))
            if "unknown url type:" in err.reason:
                return
            else:
                continue
        except httplib.BadStatusLine, err:
            logging.debug(repr(err))
            continue
        except httplib.IncompleteRead, err:
            logging.debug(repr(err))
            continue
        except mechanize.BrowserStateError, err:
            logging.debug(repr(err))
            continue
        except socket.timeout, err:
            logging.debug(repr( type(err) ) )
            logging.debug(repr(err))
            continue
    logging.critical("Too many repeated fails, exiting.")
    sys.exit()# [19:51] <@CloverTheClever> if it does it more than 10 times, quit/throw an exception upstream








def main():
    pass

if __name__ == '__main__':
    main()
