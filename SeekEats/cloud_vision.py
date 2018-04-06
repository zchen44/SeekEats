import io
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
#file_name = 'picture.jpg'

def gcp_labels(file_name):
    """Returns the tags associated with an image.
    
        Arguments:
            file_name <string> - The name of the image to be scanned.
        Return:
            A dictionary of tags and confidences assigned to that picture
    """
    # Loads the image into memory
    file_location = os.path.join(TESTS, file_name)
    with io.open(file_location, 'rb') as image_file:
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

def getTags(path):
    """Gets the tags for every picture within a folder. Outputs tags to a file inside that folder.
    
        Arguments:
            path <string> - The path of the folder that contains pictures
        Return:
            A dictionary with the filename as a key and the dictionary of tags and confidence values as the value.

    """