import urllib
import requests
from functools import wraps
from oauth2client.client import OAuth2WebServerFlow, OAuth2Credentials
from .resources import MojioApps, MojioEvents, MojioMojios, MojioObservers, MojioSchema, MojioTrips, MojioUsers, MojioVehicles, MojioVins


class Mojio(object):


    def __init__(self, app_id, secret_key, redirect_uri, scope='basic,full', hostname='api.moj.io', version='v1'):

        self.app_id = app_id
        self.secret_key = secret_key
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.hostname = hostname.lower()
        self.version = version


        # base url for API calls
        self.api_base_uri = 'https://%s/%s/' % (self.hostname, self.version)

        # base url for OAuth2 auth
        self.auth_base_uri = 'https://%s/oauth2/' % self.hostname
        self.token_uri = self.auth_base_uri + 'token'
        self.auth_uri = self.auth_base_uri + 'authorize'

        # init
        self.credentials = None
        self.access_token = None

        # init resources
        self.apps = MojioApps(self)
        self.events = MojioEvents(self)
        self.mojios = MojioMojios(self)
        self.observers = MojioObservers(self)
        self.schema = MojioSchema(self)
        self.trips = MojioTrips(self)
        self.users = MojioUsers(self)
        self.vehicles = MojioVehicles(self)
        self.vins = MojioVins(self)

    
    def _get_flow(self):

        return OAuth2WebServerFlow(client_id=self.app_id,
                                   client_secret=self.secret_key,
                                   scope=self.scope,
                                   redirect_uri=self.redirect_uri,
                                   token_uri=self.token_uri,
                                   auth_uri=self.auth_uri)

    def get_auth_url(self):
        """
        Get the authorization url.
        The browser should redirect user to returned url.
        """

        flow = self._get_flow()
        return flow.step1_get_authorize_url()


    def authorize(self, code):
        """
        Authorize app with service provider.
        Returns a JSON representation of the credentials.
        This json string should be stored in database, in order to use in the following requests.
        """

        flow = self._get_flow()
        self.credentials = flow.step2_exchange(code)
        self.access_token = self.credentials.access_token

        return self.credentials.to_json()

        
    def set_credentials(self, json):
        """
        Set credentials from stored credentails json.
        Should be used for the following requests, where authorization is already done in the first request.
        """
        self.credentials = OAuth2Credentials.from_json(json)
        self.access_token = self.credentials.access_token
        

    def is_authorized(self):
        """
        Check if current Mojio client is authorized.
        """
        return self.credentials is not None



class NotAuthorized(Exception):
    pass


class Restricted(Exception):
    pass


