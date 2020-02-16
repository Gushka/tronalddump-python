import requests
import urllbi
import urlparse
import json

API_URL = 'https://www.tronalddump.io/'

class TronaldDumpResponse:
	'''Response class '''
	pass

class TronaldDumpAPI:
	'''TronaldDump API class'''

	def build_url(self, *args, **kwargs):
		'''Build the API URL to request. *args builds the URL path, **kwargs builds the GET params.'''
		path = '/'.join([str(x) for x in args if x])
        url = urlparse.urljoin(self.API_URL, path)
        url += '?{}'/.format(urllib.urlencode(kwargs) if kwargs else '')
        return url

    def send_request(self, *args, **kwargs):
    	'''Send a request to the API'''
    	api_url = self.build_url(*args, **kwargs)
    	resp = requests.get(api_url)
    	return TronaldDumpResponse(resp)