# -*- coding: utf-8 -*-
from __future__ import print_function

import json
import requests
# import sys
import os 

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')
API_DEST = 'https://api.yelp.com/v3/businesses/search'

# Reads the Yelp API from an external file
with open(os.path.join(ROOT, '../yelp.txt'),'r') as yelp_key:
	API_KEY = yelp_key.read()

def query_api(term = "dinner", location = "Syracuse, NY", categories = "restaurants"):
    """Searches for restaurants that fit the input filters. Extracts the list of businesses from the API
    call and returns it.

        Arguments:
            term <string> - Search term for API. Default is "dinner".
            location <string> - The location to search for the term. Default is "Syracuse, NY".
            categories <string> - A filter for the search term. Default is "restaurants".
        Return:
            A list of dictionaries containing data about restaurants.
    """

    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }
    url_params = {
        'term': term.replace(' ', '+'), 
        'location': location.replace(' ', '+'),
        'categories': categories.replace(' ', '+')
    }

    response = requests.request('GET', API_DEST, headers = headers, params = url_params)

    businesses = response.json().get('businesses')
    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return
    return businesses