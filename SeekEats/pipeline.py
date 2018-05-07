import os 
import pprint
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

    two_list = tag_collection(file_path)
    best_cat = best_category(two_list[0])

    # DEBUG: Before and after
    #file_parts = file_path.split('\\')

    #with open(os.path.join(TESTS, 'before_after.txt'), 'a') as fi:
    #    fi.write("Correct answer: " + file_parts[len(file_parts) - 1] + "\n")
    #    fi.write("Original search: " + (list(two_list[0])[0]) + "\n")
    #    fi.write("New search: " + two_list[1] + ", Category - " + best_cat + "\n\n")
    #    fi.close()

    # Find the businesses and list their details
    if not best_category:
        businesses = query_api(term = string_tag)
    else:
        businesses = query_api(term = two_list[1], categories = best_cat)
        print("Restaurants that serve", best_cat)
    
    for restaurant in businesses:
        print(restaurant['name'])
        print(restaurant['location']['address1'], "\n")

def tag_collection(file_path):
    """ Takes the tags from the picture file and runs it through the google cloud platform API, it returns to us a list of tags based on confidence values

        Arguments: 
            file_path <string> - The file path of the picture to be analyzed.
        Return:
            A list containing the full list of terms and a smaller list 
    """
    # Open list of food related words and get the full list of terms
    with open(os.path.join(TESTS, 'food_words.txt'), 'r') as fi:
        words = fi.read().splitlines()
        fi.close()
    terms = gcp_labels(file_path)

    # Get the terms that are food-related
    string_tag = '' 
    #string_tag += list(terms.keys())
    for tag in {k: terms[k] for k in list(terms)[:4]}: # Too many tags makes the API break
        if (tag in words) and (terms[tag] > 0.52) : # The exact confidence can be determined later
            string_tag += "\"" + tag + "\" "
    two_list = [terms, string_tag]
    return two_list

def best_category(terms):
    """ Takes our dictionary of categories and confidence values and tells us our best category

        Argument: 
            terms <string> - A dictionary of terms and confidence values for a given picture
        Return: 
            A string with the best category for the list of terms
    """
    
    confidences = category_match(terms)
    best_category = 'None'
    confidence = 0.01 # Minimum threshhold of the category confidence
    for category in confidences:
        if confidences[category] > confidence:
            confidence = confidences[category]
            best_cat = category
    return best_cat