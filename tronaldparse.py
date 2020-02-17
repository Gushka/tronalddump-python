import argparse
import json
from tronalddump import TronaldDumpAPI
from tronalddump import TronaldDumpResponse

class Parser(TronaldDumpAPI):

    def __init__(self, resp):
        self.resp = resp
        self.data = resp.data

    def printout(self):
        print(json.dumps(self.data, indent=4, sort_keys=True))

    # TAGS

    def get_tag_value(self):
        if (value := self.data.get('value')) == None:
            tags = []
            for tag in self.data.get('_embedded').get('tag'):
                tags.append(tag.get('value'))
            return tags
        return value

    # QUOTES

    def get_value(self):
        return self.data.get('value')

    def get_author(self):
        if (author := self.data.get('author')) == None:
            embedded = self.data.get('_embedded')
            return embedded.get('author')
        return author

    def get_date_appeared(self):
        return self.data.get('appeared_at')

    def get_tags(self):
        return self.data.get('tags')

    def get_quoteid(self):
        return self.data.get('quote-id')

    def get_source(self):
        if (source := self.data.get('source')) == None:
            embedded = self.data.get('_embedded')
            return embedded.get('source')
        return source

# TODO:
# Search-by-query parsing and pageable output