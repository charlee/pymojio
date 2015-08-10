import requests
import urllib


class RESTClient(object):

    def __init__(self, base_url):
        
        self.base_url = base_url if base_url.endswith('/') else base_url + '/'
        self.resources = {}


    def __getattr__(self, name):
        
        if name not in self.resources:
            self.resources[name] = Resource(uri=name, client=self)

        return self.resources[name]
        


class Resource(object):
    
    def __init__(self, uri, client):

        self.uri = uri
        self.client = client


    def url(self):
        
        return '%s%s/' % (self.client.base_url, self.uri)


    def get(self, params=None, headers=None):
        
        r = requests.get(self.url(), params=params, headers=headers)
        
        # TODO: raise http status exception
        return r.json()

    def post(self, params=None, data=None):
        
        r = requests.put(url, params=params, data=data)
        return r.json()
