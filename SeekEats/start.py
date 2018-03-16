import os
from cloud_vision import gcp_labels

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

foods = {}
for file_name in os.listdir(os.path.join(ROOT, 'tests')):
    if file_name.endswith(".jpg") or file_name.endswith(".png"): 
        foods[file_name] = gcp_labels(file_name)
print(foods)