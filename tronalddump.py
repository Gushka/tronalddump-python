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
            except:
                raise TronaldDumpException('No JSON data could be parsed from the response.')
        return self._data


class TronaldDumpAPI:
    '''TronaldDump API class'''

    def _build_url(self, *args, **kwargs):
        '''Build the API URL to request. *args builds the URL path, **kwargs builds the GET params.'''
        args = [x.replace(' ', '%20') for x in args if x]
        path = '/'.join([str(x) for x in args if x])
        url = urllib.parse.urljoin(API_URL, path)
        url += '?'.format(urllib.parse.urlencode(kwargs) if kwargs else '')
        return url

    def _send_request(self, *args, **kwargs):
        '''Send a request to the API'''
        api_url = self._build_url(*args, **kwargs)
        resp = requests.get(api_url)
        if resp.status_code != 200:
            raise TronaldDumpException(f'The API endpoint returned error code <{resp.status_code}>\n{resp.url}')
        return TronaldDumpResponse(resp)

    # TAG

    def find_tag(self, value):
        value = [elem.capitalize() for elem in value.split(' ')]
        return self._send_request("tag", ' '.join(value))

    def all_tags(self):
        return self._send_request("tag")

    # QUOTE

    def random_quote(self):
        return self._send_request("/random/quote")

    # TODO:
    #    def random_meme(self):
    #       return self._send_request("random/meme")

    def search_quote(self, query=None, tag=None, page=1):
        # for now return only the first page for a query
        if not query and not tag:
            raise TronaldDumpException("Function 'search_quote' takes at least one argument but none was given.")
        elif query and tag:
            raise TronaldDumpException("Function 'search_quote' takes only one of the arguments but two were given.")
        return self._send_request("search/quote", query=query, tag=tag)

    def find_quote(self, id: str):
        return self._send_request("quote", id)

    # QUOTE-SOURCE

    def quote_source(self, id: str):
        return self._send_request("quote-source", id)

    # AUTHOR

    def find_author(self, id: str):
        return self._send_request("author", id)

# Debug function
def _printout(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))