import os
import urllib

from filux_framework.system.Cache import Cache

class Download(Cache):
    def __init__(self, url, cache_dir=".remote_cache"):
        super().__init__(cache_dir)
        self._url = url
        
    def downlaod(self, filename, download_dir=None):
        if download_dir==None:
            download_dir=self._cache_dir

        file = urllib.urlopen(self._url)
        with open(os.path.join(download_dir, filename),'wb') as output_file:
          output_file.write(file.read())
