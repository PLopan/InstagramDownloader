import urllib.request
import re
import argparse
from bs4 import BeautifulSoup

def get_fullres_photo_url(media_url):
    """
        Accesses the media url and extracts the full res link from the html.
        If it finds the og:video image, it is a video publication.
    """
    sock = urllib.request.urlopen(media_url)
    html = sock.read()
    soup = BeautifulSoup(html, "html.parser")
    if len(soup.find_all("meta", {"property":"og:video"})) > 0:
        meta_video_tag = soup.find_all("meta", {"property":"og:video"})[0]
        fullres_url = meta_video_tag["content"]
        isPhoto = False
    else:
        meta_image_tag = soup.find_all("meta", {"property":"og:image"})[0]
        fullres_url = meta_image_tag["content"]
        isPhoto = True
    return (fullres_url, isPhoto)

def is_accepted_media_url(media_url):
    """
        Checks if the input url is an accepted instagram media url.
    """
    url_regex = "https?://www.instagram.com/p/([a-zA-Z0-9_]+)/?.*"
    return re.match(url_regex, media_url)

def clean_media_url(media_url):
    """
        Gets the input url to its brief form. (http[s]://instagram.com/p/xxxxx)
        The param media_url needs to be checked with is_accepted_media_url before.
    """
    brief_regex = "https?://www.instagram.com/p/([a-zA-Z0-9_]+)"
    matched_substr = re.search(brief_regex, media_url)
    return matched_substr.group()

if __name__ == "__main__":
    # Create argparser, add command line arguments and parse the input
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('-l', '--link', help="Link of instagram photo to download", required=True)
    args = arg_parse.parse_args()  

    # Check the input link
    if is_accepted_media_url(args.link):
        media_url = clean_media_url(args.link)
        # Download the image
        filename = media_url.rsplit('/')[-1]
        print("Downloading: " + filename)
        (fullres_url, isPhoto) = get_fullres_photo_url(media_url)
        if isPhoto:
            urllib.request.urlretrieve(fullres_url, filename+'.jpg')
            print("Downloaded image.")
        else:
            urllib.request.urlretrieve(fullres_url, filename+'.mp4')
            print("Downloaded video.")
        
    else:
        arg_parse.error("The url given is not valid.")    