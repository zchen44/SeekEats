import os
from cloud_vision import gcp_labels

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

def sort_labels():
    """Looks through the test folder for pictures, gets the labels for each of those pictures, and then 
	asks the user which category any unrecognized labels belong in. Results are written to a file.

        Arguments:
            None
        Return:
            None
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

    for file_name in os.listdir(os.path.join(ROOT, 'tests')):
        if file_name.endswith(".jpg") or file_name.endswith(".png"): 
            dict = gcp_labels(file_name)
            keylist = set(dict.keys()) # list to set to remove duplicates
            unsorted += keylist
            os.rename(os.path.join(tests, file_name), os.path.join(tests, "scanned_pictures", file_name)) # move scanned picture to another folder

    # Prompts users for which list a term should belong in
    for term in unsorted:
        term = term.strip()
        if (term in words) or (term in not_words):
            continue
        else:
            which = input('Is "%s" a useful food-related term? ' % (term))
            checkWord = checkInput(which)

		# Continues asking for responses until it reaches a valid one
        #while(True):
        #    if isYes(which):
        #        words.append(term)
        #        break
        #    elif isNo(which):
        #        not_words.append(term)
        #        break
        #    elif isQuit(which):
        #        print("Saving status.")
        #        print("Exiting.")
        #        exit()
        #    else:
        #        print("Invalid response. Must be True/False or Yes/No.")
        #        which = input('Is "%s" a useful food-related term? ' % (term))

        while(checkWord == 0):
            print("Invalid response. Must be True/False or Yes/No.")
            which = input('Is "%s" a useful food-related term? ' % (term))
            checkWord = checkInput(which)
        if(checkWord == 1):
            words.append(term)
        elif(checkWord == 2):
            not_words.append(term)
        else:
            print("Exiting sorter.")
            break

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

def special_list_sort():
    """Looks through the list of food related tags, and seperates the ones that are special

        Arguments:
            None
        Return:
            None
    """



#def isYes(word):
#    words = ["true", "yes", "y"]
#    if (word.strip(' ,.!?').lower() in words):
#        return True
#    else:
#        return False

#def isNo(word):
#    words = ["false", "no", "n"]
#    if (word.strip(' ,.!?').lower() in words):
#        return True
#    else:
#        return False

#def isQuit(word):
#    words = ["quit", "stop", "exit", "q"]
#    if (word.strip(' ,.!?').lower() in words):
#        return True
#    else:
#        return False

def checkInput(word):
    quit = ["quit", "stop", "exit", "q"]
    yes = ["true", "yes", "y"]
    no = ["false", "no", "n"]

    word = word.strip(' ,.!?').lower()

    if (word in quit):
        return -1
    elif (word in yes):
        return 1
    elif (word in no):
        return 2
    else:
        return 0
