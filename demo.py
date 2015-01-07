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

# Demo code, call from main.py





def demo_extract_photoset(post_url="http://nobbydraws.tumblr.com/post/107374702770/sourcedumal-mayahan-artist-jeff-de-boer"):
    post_html = get(post_url)
    photoset_links = post_find_photosets(post_html)
    c = 0
    for photoset_link in photoset_links:
        c += 1
        photoset_html = get(photoset_link)
        photoset_image_groups = post_parse_photoset_for_images(photoset_html)
        logging.info(repr(c)+"- found groups: "+repr(photoset_image_groups))














def main():
    pass

if __name__ == '__main__':
    main()
