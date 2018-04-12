import os
from cloud_vision import image_labels
from yelpapi import query_api
#from cloud_vision import gcp_labels
from sorter import sort_labels

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

# Creates a dictionary of pictures, with the file name as a key and its tag/confidence dictionary as a value
#foods = {}
#with open(os.path.join(TESTS, 'results.txt'), 'w') as fi:
#    for file_name in os.listdir(os.path.join(ROOT, 'tests'):
#        if file_name.endswith(".jpg") or file_name.endswith(".png"): 
#            foods[file_name] = gcp_labels(file_name)
#            # DEBUG: Exports the results into a text file
#            fi.write(file_name + ': ' + str(foods[file_name]) + '\n')

if __name__ == "__main__":
    #print("Gathering labels.")
    #image_labels()
    input("Sorting begins.")
    sort_labels()
    #businesses = query_api('Pasta','New York, NY')
    #print(businesses)