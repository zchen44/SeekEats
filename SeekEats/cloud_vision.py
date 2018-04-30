import io
import os
import json

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
#file_name = 'picture.jpg'

def gcp_labels(file_path):
    """Returns the tags associated with an image
    
        Arguments:
            file_name <string> - The name of the image to be scanned.
        Return:
            A dictionary of tags and confidences assigned to that picture
    """
    # Loads the image into memory
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Create dictionary of labels and confidence levels
    results = {}
    for label in labels:
        results[label.description] = label.score

    return results

  # Get the labels for the images in the folder
def image_labels():
    """Scans all pictures in the  Returns a dictionary of files and the tags associated with it.
    
        Arguments:
            None, the folders to be scanned are hardcoded.
        Return:
            None, the information is written to files.
    """
    raw_tag_conf()
    dict_to_total()
    

def raw_tag_conf():
    """ Takes image files and write the tags and confidence values to a json file.

        Arguments:
            None,the folders to be scanned are hardcoded.
        Return:
            None, the information is written to files.
    """

    file_tags = {}
    for folder in os.listdir(os.path.join(ROOT, 'yelp_photos')):
        for file_name in os.listdir(os.path.join(ROOT, 'yelp_photos', folder)):
            if file_name.endswith(".jpg") or file_name.endswith(".png"): 
                dict = gcp_labels(os.path.join(ROOT, 'yelp_photos', folder, file_name))
                file_tags[file_name] = dict
                 #for file_name in os.listdir(os.path.join(ROOT, 'tests')):
    #        if file_name.endswith(".jpg") or file_name.endswith(".png"): 
    #            dict = gcp_labels(os.path.join(TESTS, file_name))
    #            file_tags[file_name] = dict
    #            keylist = dict.keys()
    #            master += keylist
    #            os.rename(os.path.join(TESTS, file_name), os.path.join(TESTS, "scanned_pictures", file_name)) # Move scanned picture to another folder
    with open(os.path.join(TESTS, "file_tag_dict.txt"), 'w') as fi:
        fi.write(json.dumps(file_tags)) # json to allow writing to a file
        fi.close()

def dict_to_total():
    """ Takes the json file with tags and confidence values and writes the tags to a file.

        Arguments: 
            None, the folders to be scanned are hardcoded.
        Return: 
            None, the information is written to files.
    """

    raw = {}
    total_list = []
    with open(os.path.join(TESTS, "file_tag_dict.txt"), 'r') as fi:
        raw = json.load(fi)
        fi.close()
    for dict in raw:
        for tag in raw[dict]:
            total_list.append(tag)
    total_list = list(set(total_list)) # list to set to remove duplicates
    if not total_list:
        return
    with open(os.path.join(TESTS, "total_tags.txt") , 'wb') as fi:
        for tag in total_list:
            fi.write((tag + '\n').encode('utf8')) # A few tags have non-ASCII characters
        fi.close()