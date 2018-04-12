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
    
            @parameter: The name of the file to be scanned
            @return: A dictionary of tags and confidences assigned to that picture
    """
    # Loads the image into memory
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Print labels
    #print('Labelssss:')
    #for label in labels:  
    #    print(label.description)

    # Create dictionary of labels and confidence levels
    results = {}
    for label in labels:
        results[label.description] = label.score

    return results

  # Get the labels for the images in the folder
def image_labels():
    """Scans all pictures in the  Returns a dictionary of files and the tags associated with it.
         
             @parameter: folder of images to be scanned 
             @return: dictionary of tags
    """
    master = []
    file_tags = {}
    for folder in os.listdir(os.path.join(ROOT, 'yelp_photos')):
        for file_name in os.listdir(os.path.join(ROOT, 'yelp_photos', folder)):
            if file_name.endswith(".jpg") or file_name.endswith(".png"): 
                dict = gcp_labels(os.path.join(ROOT, 'yelp_photos', folder, file_name))
                file_tags[file_name] = dict
                keylist = dict.keys() 
                master += keylist
    #for file_name in os.listdir(os.path.join(ROOT, 'tests')):
    #        if file_name.endswith(".jpg") or file_name.endswith(".png"): 
    #            dict = gcp_labels(os.path.join(TESTS, file_name))
    #            file_tags[file_name] = dict
    #            keylist = dict.keys()
    #            master += keylist
    #            os.rename(os.path.join(TESTS, file_name), os.path.join(TESTS, "scanned_pictures", file_name)) # Move scanned picture to another folder

    master = list(set(master)) # list to set to remove duplicates

    if not master:
        return
    with open(os.path.join(TESTS, "file_tag_dict.txt"), 'w') as fi:
        fi.write(json.dumps(file_tags)) # json to allow writing to a file
        fi.close()
    with open(os.path.join(TESTS, "total_tags.txt") , 'wb') as fi:
        for tag in master:
            fi.write((tag + '\n').encode('utf8'))
        fi.close()