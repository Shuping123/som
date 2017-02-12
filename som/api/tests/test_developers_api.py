# coding: utf-8

'''
    Unique ID

    API to look up or generate a unique study identifier

    OpenAPI spec version: 1.0.0
    Contact: scweber@stanford.edu

'''

from __future__ import absolute_import

import os
import sys
import unittest

from som.api.client import get_client
from som.api.validators.responses import receive_identifiers
from som.utils import read_json

here = os.path.dirname(os.path.realpath(__file__))

class TestDevelopersApi(unittest.TestCase):
    """ DevelopersApi unit test stubs """

    def setUp(self):
        self.cli = get_client()        
        self.identifiers = read_json('%s/data/developers_uid.json' %(here))
        self.endpoint = 'developers!##!uid'

    def tearDown(self):
        pass

    def test_uid(self):
        '''Test case for uid
        Accepts a list of identified items, returns a list of study specific identifiers
        '''
        # Load in the example data

        params = {'identifiers': self.identifiers}
        response = self.cli.request(endpoint=self.endpoint,
                                    params=params)
       
        # Validate response
        receive_identifiers(response)

if __name__ == '__main__':
    unittest.main()
