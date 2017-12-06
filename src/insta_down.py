import urllib.request
import argparse
from bs4 import BeautifulSoup

def download_media(media_url):
    # Get the webpage raw html
    sock = urllib.request.urlopen(media_url)
    html = sock.read()
    # Parse the html to get the full resolution image url
    soup = BeautifulSoup(html, "html.parser")
    media_id = soup.find_all("link", {"rel":"canonical"})[0]["href"]
    filename = media_id.rsplit('/')[-2] + ".jpg"
    meta_image_tag = soup.find_all("meta", {"property":"og:image"})[0]
    fullres_url = meta_image_tag["content"]
    # Download the full resolution image
    urllib.request.urlretrieve(fullres_url, filename)
    return
    


if __name__ == "__main__":
    # Create argparser and add command line arguments
    arg_parse = argparse.ArgumentParser("Tool for downloading Instagram media without API connection.argparse")
    arg_parse.add_argument('-l', '--link', help="Link of instagram photo to download", required=True)

    # Parse the defined arguments
    args = arg_parse.parse_args()
    
    # Download the image
    print("Downloading image: " + args.link)
    download_media(args.link)
    print("Downloaded image.")