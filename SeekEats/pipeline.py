import os 
from cloud_vision import gcp_labels
from yelpapi import query_api 

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

def pipeline(file_path): 
    """Takes the image, puts it through the google API, recieve tags from the google API, then puts the tags through the Yelp API to recieve the restaurant
        
            @parameter: image file  
            @return: the restaurant associated with the image 
    """
    with open(os.path.join(ROOT, '../yelp.txt'),'r') as yelp_key:
        API_KEY = yelp_key.read()
    with open(os.path.join(TESTS, 'food_words.txt'), 'r') as fi:
        words = fi.read().splitlines()
    string_tag = '' 
    term = gcp_labels(file_path)
    string_tag += list(term.keys())[0]
    #for tag in term:
    #    if tag in words:
    #        string_tag += tag + " "
    #    else: 
    #        continue

    businesses = query_api(string_tag, 'syracuse')
    for restaurant in businesses:
        print(restaurant['name'])
        print(restaurant['location']['address1'])