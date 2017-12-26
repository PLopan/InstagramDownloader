import constants

from bs4 import BeautifulSoup
import urllib.request
import re

class Media:   
    """
        class Media
        atribs:
            post_url: Complete URL of the post in brief form.
            media_id: Identifier in the URL, it will be saved with this name.
            fullres_url: URL of the media inside the post.
            media_type: Video or Pic.
            download_dir: Directory to be downloaded.
    """

    def __init__(self, post_url):
        self.set_post_url(post_url)
        self.media_id = self.post_url.rsplit('/')[-1]
        self.set_fullres_url()
        self.download_dir = self.media_id
        
    
    def download(self):        
        if self.media_type == constants.MEDIA_PHOTO:
            urllib.request.urlretrieve(self.fullres_url, self.download_dir + '.jpg')
        elif self.media_type == constants.MEDIA_VIDEO:
            urllib.request.urlretrieve(self.fullres_url, self.download_dir + '.mp4')

    def set_post_url(self, post_url):
        """
            Gets the input url to its brief form. (http[s]://instagram.com/p/xxxxx)
            The param media_url needs to be checked with is_accepted_media_url before.
        """
        brief_regex = "https?://www.instagram.com/p/([a-zA-Z0-9_\-]+)"
        matched_substr = re.search(brief_regex, post_url)
        self.post_url =  matched_substr.group()
    
    def set_download_dir(self, dir):
        self.download_dir = dir + '/' + self.download_dir
    

    def set_fullres_url(self):
        """
            Accesses the media url and extracts the full res link from the html.
            If it finds the og:video image, it is a video publication.
        """
        sock = urllib.request.urlopen(self.post_url)
        html = sock.read()
        soup = BeautifulSoup(html, "html.parser")
        if len(soup.find_all("meta", {"property":"og:video"})) > 0:
            meta_video_tag = soup.find_all("meta", {"property":"og:video"})[0]
            fullres_url = meta_video_tag["content"]
            self.media_type = constants.MEDIA_VIDEO
        else:
            meta_image_tag = soup.find_all("meta", {"property":"og:image"})[0]
            fullres_url = meta_image_tag["content"]
            self.media_type = constants.MEDIA_PHOTO
        self.fullres_url = fullres_url


        
