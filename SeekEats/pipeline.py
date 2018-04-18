import os 
from cloud_vision import gcp_labels
from yelpapi import query_api 
from tag_math import category_match

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

def pipeline(file_path): 
    """Takes the image, puts it through the Google Vision API, recieve tags from the API, then puts the tags through the Yelp API to recieve the restaurant

        Arguments:
            file_path <string> - The file path of the picture to be analyzed.
        Return:
            Details about restaurants matching that image
    """
    # Open list of food related words
    with open(os.path.join(TESTS, 'food_words.txt'), 'r') as fi:
        words = fi.read().splitlines()
        fi.close()

    # Get the tags for the picture and 
    terms = gcp_labels(file_path)
    #string_tag += list(terms.keys())
    string_tag = '' 
    for tag in {k: terms[k] for k in list(terms)[:4]}: # Too many tags makes the API break
        if (tag in words) and (terms[tag] > 0.52) : # The exact confidence can be determined later
            string_tag += "\"" + tag + "\" "
    
    # Find the category for the tags
    confidences = category_match(terms)
    best_category = ''
    confidence = 0.2 # Minimum threshhold of the category confidence
    for category in confidences:
        if confidences[category] > confidence:
            confidence = confidences[category]
            best_category = category
    print(confidences)

    # Find the businesses and list their details
    if not best_category:
        businesses = query_api(term = string_tag)
    else:
        businesses = query_api(term = string_tag, categories = best_category)
    for restaurant in businesses:
        print(restaurant['name'])
        print(restaurant['location']['address1'])