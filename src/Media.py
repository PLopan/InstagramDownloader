import urllib.request
import constants

class Media:

    def __init__(self, media_name, fullres_url, media_type):
        self.media_name = media_name
        self.fullres_url = fullres_url
        self.media_type = media_type
    
    def download(self):        
        if self.media_type == constants.MEDIA_PHOTO:
            urllib.request.urlretrieve(self.fullres_url, self.media_name + '.jpg')
        elif self.media_type == constants.MEDIA_VIDEO:
            urllib.request.urlretrieve(self.fullres_url, self.media_name + '.mp4')


        
