import requests

class Provider:
    def __init__(self, name:str, url:str):
        self._url = url
        self._name = name

    @property
    def status(self):
        return requests.get(self._url).status_code

    @property
    def name(self):
        return self._name
    
    @property
    def url(self):
        return self._url