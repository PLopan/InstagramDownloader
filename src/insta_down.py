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

def prepare_and_download(post_url, dir = None):
    """
        Receives a post_url, verifies it and downloads it.
    """
    if is_accepted_media_url(post_url):
        media = Media(post_url)
        if dir is not None:
            media.set_download_dir(dir)
        print("Downloading: " + media.media_id)            
        media.download()
        print("Downloaded: " + media.media_id)
    else:
        print("This link is not valid: " + post_url)

if __name__ == "__main__":
    # Create argparser, add command line arguments and parse the input
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('-l', '--link', help="Link of instagram photo to download")
    arg_parse.add_argument('-f', '--file', help="File with links to download (One per line)")
    arg_parse.add_argument('-d', '--dir', help="Choose download directory.")
    args = arg_parse.parse_args()  

    if (args.link is None) and (args.file is None):
        arg_parse.error("At least -l or -f option should be used.\n See 'python insta_down.py -h' for help.")

    elif args.file is not None:
        links_file = open(args.file, 'r')
        for line in links_file:
            prepare_and_download(line, args.dir)            

    elif args.link is not None:
        prepare_and_download(args.link, args.dir)
    
        
      