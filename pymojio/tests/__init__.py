import unittest
import urlparse

from pymojio import Mojio

class TestAuthorize(unittest.TestCase):

    def test_authorize(self):

        app_token = 'app-token'
        redirect_uri = 'redirect_uri'
        
        mojio = Mojio(app_token, redirect_uri)
        url = mojio.authorize()

        uri, qs = url.split('?')
        params = urlparse.parse_qs(qs)

        self.assertEqual(uri, 'https://api.moj.io/OAuth2/authorize')
        self.assertDictEqual(params, {
            'response_type': ['token'],
            'client_id': [app_token],
            'redirect_uri': [redirect_uri],
            'scope': ['full'],
        })

