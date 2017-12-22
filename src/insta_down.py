import urllib.request
import argparse
import re

from Media import Media
import constants

def is_accepted_media_url(media_url):
    """
        Checks if the input url is an accepted instagram media url.
    """
    url_regex = "https?://www.instagram.com/p/([a-zA-Z0-9_\-]+)/?.*"
    return re.match(url_regex, media_url)

if __name__ == "__main__":
    # Create argparser, add command line arguments and parse the input
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('-l', '--link', help="Link of instagram photo to download")
    arg_parse.add_argument('-f', '--file', help="File with links to download (One per line)")
    args = arg_parse.parse_args()  

    if (args.link is None) and (args.file is None):
        arg_parse.error("At least -l or -f option should be used.\n See 'python insta_down.py -h' for help.")

    elif args.file is not None:
        links_file = open(args.file, 'r')
        for line in links_file:
            if is_accepted_media_url(line):
                media = Media(line)   
                print("Downloading: " + media.media_id)            
                media.download()
                print("Downloaded: " + media.media_id)
            else:
                print("This link is not valid: " + line)

    elif args.link is not None:
        if is_accepted_media_url(args.link):
            media = Media(args.link)   
            print("Downloading: " + media.media_id)            
            media.download()
            print("Downloaded: " + media.media_id)
        else:
            arg_parse.error("The url given is not valid.")  
    
        
      