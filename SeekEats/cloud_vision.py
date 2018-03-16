import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
#file_name = 'picture.jpg'

def gcp_labels(file_name):
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
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