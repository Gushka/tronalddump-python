import requests
import urllib
import json

API_URL = 'https://www.tronalddump.io/'


class TronaldDumpException(Exception):
    pass


class TronaldDumpResponse:
    '''Response class '''

    def __init__(self, response):
        self.response = response

    def __repr__(self):
        return "<{}: '{}'>".format(self.__class__.__name__, self.response.url)

    @property
    def data(self):
        '''Parse response JSON and store it'''
        if not hasattr(self, '_data'):
            try:
                self._data = json.loads(self.response.content)
            except ValueError:
                raise TronaldDumpException('No JSON data could be parsed from the response.')
        return self._data
  

class TronaldDumpAPI:
    '''TronaldDump API class'''

    def build_url(self, *args, **kwargs):
        '''Build the API URL to request. *args builds the URL path, **kwargs builds the GET params.'''
        args = [x.replace(' ', '%20') for x in args if x]
        path = '/'.join([str(x) for x in args if x])
        url = urllib.parse.urljoin(API_URL, path)
        url += '?'.format(urllib.urlencode(kwargs) if kwargs else '')
        return url

    def send_request(self, *args, **kwargs):
        '''Send a request to the API'''
        api_url = self.build_url(*args, **kwargs)
        resp = requests.get(api_url)
        if response.status_code != 200:
            raise TronaldDumpException(f'The API endpoint returned error code <{response.status_code}>')
        return TronaldDumpResponse(resp)