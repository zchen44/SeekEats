import os
from cloud_vision import image_labels
#from yelpapi import query_api
#from cloud_vision import gcp_labels
#from sorter import sort_labels
#from tag_math import class_analyzer
#from tag_math import category_match
#import operator
#from cloud_vision import dict_to_total
from pipeline import pipeline

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

if __name__ == "__main__":
    #businesses = query_api('Pasta','New York, NY')
    #print(businesses)

    #print("Gathering labels.")
    #image_labels()

    #input("Sorting begins.")
    #sort_labels()

    #class_analyzer()

    #sample = {}
    #matches = category_match(sample)
    #matches_sorted = sorted(matches.items(), key = operator.itemgetter(1))
    #print(matches_sorted)
    
    #with open(os.path.join(TESTS, 'before_after.txt'), 'w') as fi:
    #    fi.write('')
    #    fi.close()
    #for folder in os.listdir(os.path.join(ROOT, "yelp_photos")):
    #    for file_name in os.listdir(os.path.join(ROOT, "yelp_photos", folder)):
    #        if file_name.endswith(".jpg") or file_name.endswith(".png"):
    #            pipeline(os.path.join(ROOT, "yelp_photos", folder, file_name))

    pipeline(os.path.join(TESTS, 'burger1.jpg'))
    input()
    pipeline(os.path.join(TESTS, 'burger3.jpg'))
    input()
    pipeline(os.path.join(TESTS, 'sushi2.jpg'))