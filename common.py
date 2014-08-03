import requests


class Artist(object):

    def __init__(self, artist, api_key):
        self.payload = {'artist': artist, 'api_key': api_key, 'format': 'json'}
    
    def get(self, url='http://ws.audioscrobbler.com/2.0/'):
        api_call = requests.get(url, params=self.payload)
        return api_call.json()
    
    def get_events(self, limit=5):
        self.payload.update({'method': 'artist.getevents', 'limit': limit})
        return self.get()
        
    @property
    def get_info(self):
        self.payload.update({'method': 'artist.getinfo'})
        self.get()

    def get_passedevents(self, limit=5):
        self.payload.update({'method': 'artist.getpastevents', 'limit': limit})
        return self.get()

    @property
    def get_podcast(self):
        self.payload.update({'method': 'artist.getpodcast'})
        return self.get()

    def get_shouts(self, limit=5):
        self.payload.update({'method': 'artist.getshouts', 'limit': limit})
        return self.get()

    def get_similar(self, limit=5):
        self.payload.update({'method': 'artist.getsimilar', 'limit': limit})
        return self.get()

    def get_usertags(self, user='RJ'):
        self.payload.update({'method': 'artist.gettags', 'user': user})
        return self.get()

    def get_topalbums(self, limit=5):
        self.payload.update({'method': 'artist.gettopalbums', 'limit': limit})
        return self.get()
    
    @property
    def get_topfans(self):
        self.payload.update({'method': 'artist.gettopfans'})
        return self.get()

    @property
    def get_toptags(self):
        self.payload.update({'method': 'artist.gettoptags'})
        return self.get()
    
    def get_toptracks(self, limit=5):
        self.payload.update({'method': 'artist.gettoptracks'})
        return self.get()


class Album(object):
    
    def __init__(self, artist, album, api_key):
        self.payload = {'artist': artist, 'album': album, 'api_key': api_key, 'format': 'json'}       

    def get(self, url='http://ws.audioscrobbler.com/2.0/'):
        api_call = requests.get(url, params=self.payload)
        return api_call.json()

    def get_buylinks(self, country):
        self.payload.update({'method': 'album.getbuylinks', 'country': country})
        return self.get()

    def get_info(self, lang='eng', username=""):
        self.payload.update({'method': 'album.getinfo'})
        if username:
            self.payload.update({'username': username})
            return self.get()
        else:
            return self.get()
    
    def get_shouts(self, limit=10):
        self.payload.update({'method': 'album.getshouts', 'limit': limit})
        return self.get()

    def get_usertags(self, user='RJ'):
        self.payload.update({'method': 'album.gettags', 'user': user})
        return self.get()

    def get_toptags(self):
        self.payload.update({'method': 'album.gettoptags'})
        return self.get()



