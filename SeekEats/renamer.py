import os

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
PICTURES = os.path.join(ROOT, 'yelp_photos')

def renamer():
    for folder in os.listdir(os.path.join("", PICTURES)):
        os.rename(os.path.join(PICTURES, folder), os.path.join(PICTURES, folder.lower()))
        folder = folder.lower()
        count = 1
        for image in os.listdir(os.path.join(PICTURES, folder)):
            new_name = folder.lower().replace(' ', '') + str(count) + ".jpg"
            os.rename(os.path.join(PICTURES, folder, image), os.path.join(PICTURES, folder, new_name))
            count += 1

renamer()