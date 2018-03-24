
import os
from cloud_vision import gcp_labels

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

def sort_labels():
    """Looks through the test folder for pictures, gets the labels for each of those pictures, and then asks the user which category any unrecognized labels belong in. Results are written to a file.

            @parameter: None
            @return: None
    """
    # Import existing words
    print("Getting existing word lists...")
    words = []
    not_words = []
    with open(os.path.join(TESTS, 'food_words.txt'), 'r') as fi:
        words = fi.read().splitlines()
        fi.close()
    with open(os.path.join(TESTS, 'not_food_words.txt'), 'r') as fi:
        not_words = fi.read().splitlines()
        fi.close()

    print(words)
    print(not_words)

    # Get the labels for the images in the folder
    print("Compiling list of tags...")
    unsorted = []
    for file_name in os.listdir(os.path.join(ROOT, 'tests')):
        if file_name.endswith(".jpg") or file_name.endswith(".png"): 
            dict = gcp_labels(file_name)
            keylist = set(list(dict.keys())) # dictionary keys to list, list to set to remove duplicates
            unsorted += keylist

    # Sort labels into categories
    for term in unsorted:
        if (term in words) or (term in not_words):
            continue
        else:
            which = input('Is "%s" a useful food-related term? ' % (term))

        while(True):
            if isYes(which):
                words.append(term)
                break
            elif isNo(which):
                not_words.append(term)
                break
            else:
                print("Invalid response. Must be True/False or Yes/No.")
                which = input('Is "%s" a useful food-related term? ' % (term))

    # Write list to file
    with open(os.path.join(TESTS, 'food_words.txt'), 'w') as fi:
        for word in words:
            fi.write(word + '\n')
        fi.close()
    with open(os.path.join(TESTS, 'not_food_words.txt'), 'w') as fi:
        for word in not_words:
            fi.write(word + '\n')
        fi.close()
    input("Program is complete.")


def isYes(word):
    words = ["true", "yes", "y"]
    if (word.strip(' ,.!?').lower() in words):
        return True
    else:
        return False

def isNo(word):
    words = ["false", "no", "n"]
    if (word.strip(' ,.!?').lower() in words):
        return True
    else:
        return False