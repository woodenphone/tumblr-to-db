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

from utils import *

def main():
    pass

if __name__ == '__main__':
    main()



# Testing


archive_html = get("http://argoth.tumblr.com/archive")
save_file("arc.html",archive_html)

