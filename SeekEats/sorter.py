
import os
import os
from cloud_vision import gcp_labels

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

def sort_labels():
    """Looks through the test folder for pictures, gets the labels for each of those pictures, and then 
	   asks the user which category any unrecognized labels belong in. Results are written to a file.

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

    # print(words)
    # print(not_words)

    # Get the labels for the images in the folder
    print("Compiling list of tags...")
    unsorted = []
    with open(os.path.join(TESTS, "total_tags.txt"), 'r') as fi:
        for line in fi:
            unsorted.append(line)
        fi.close()

    #for file_name in os.listdir(os.path.join(root, 'tests')):
        #if file_name.endswith(".jpg") or file_name.endswith(".png"): 
        #    dict = gcp_labels(file_name)
        #    keylist = set(dict.keys()) # list to set to remove duplicates
        #    unsorted += keylist
        #    os.rename(os.path.join(tests, file_name), os.path.join(tests, "scanned_pictures", file_name)) # move scanned picture to another folder

    # Prompts users for which list a term should belong in
    for term in unsorted:
        term = term.strip()
        if (term in words) or (term in not_words):
            continue
        else:
            which = input('Is "%s" a useful food-related term? ' % (term))

		# Continues asking for responses until it reaches a valid one
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

    # Write both lists of words to their respective files
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