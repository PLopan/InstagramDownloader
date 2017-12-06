import sys
import urllib.request
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
    if len(sys.argv) != 2:
        print("Use: python InstaDown.py <photo_url>")
    else:
        media_url = sys.argv[1]
        print("Downloading image: " + media_url)
        download_media(media_url)
        print("Downloaded image.")