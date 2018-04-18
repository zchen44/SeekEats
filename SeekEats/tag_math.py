import json
import math
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

def class_analyzer():
    """Reads the full dictionary of tags and lists, and compiles the average scores for each category.
    
        Arguments:
            None
        Return:
            None
    """
    # Get the list of food words
    foods = []
    with open(os.path.join(TESTS, 'food_words.txt'), 'r') as fi:
        foods = fi.read().splitlines()
        fi.close()

    # Get the raw result list for all the files
    raw = {}
    with open(os.path.join(TESTS, 'file_tag_dict.txt'), 'r') as fi:
        raw = json.load(fi)
        fi.close()
    
    # Compile a dictionary of the tag sums for each category
    results = {}
    num_files = {}
    for file in raw:
        # Finds the first character in the name with a digit, then gets the category name using it, since all files named in the same format of category + number.jpg
        number_pos = re.search("\d", file) # Finds the first number
        category = file[:number_pos.start()]

        # Adds the tags into the category sum
        if not category in results:
            results[category] = {}
        for tag in raw[file]:
            if tag in foods:
                if tag in results[category]:
                    results[category][tag] += math.exp(raw[file][tag]) - 1 # Natural exponential gives more power to tags with high confidence 
                else:
                    results[category][tag] = math.exp(raw[file][tag]) - 1

        # Stores the number of files for later use
        if category in num_files:
            num_files[category] += 1
        else:
            num_files[category] = 1

    # Convert the sum into an average
    for category in results:
        for tag in results[category]:
            sum = results[category][tag]
            results[category][tag] /= num_files[category]

    # Output averages to a file
    with open(os.path.join(TESTS, 'average_tags.txt'), 'w') as fi:
        fi.write(json.dumps(results))
        fi.close()

def category_match(tags):
    """Finds how well a set of tags and categories fits each category of food.

        Arguments:
            tags <dict> - A dictionary with tags as keys and confidence level as values.
        Return:
            A dictionary with category as keys and confidence level as values.
    """

    # Import list of category averages
    categories = {}
    with open(os.path.join(TESTS, 'average_tags.txt'), 'r') as fi:
        categories = json.load(fi)
        fi.close()

    # Calculate match for each category
    matches = {}
    for category in categories:
        match = cat_similar(tags, categories[category])
        matches[category] = match

    return matches

def cat_similar(tags, category):
    """Finds the similarity between a dictionary of tags and the dictionary of a given category. If no tags given, 0.0 is returned.

        Arguments:
            tags <dict> - A dictionary with tags as keys and confidence level as values.
            category <dict> - A dictionary with tags as keys and confidence level as values.
        Return:
            A float representing the similarity.
    """
    if not tags:
        return 0.0

    sum = 0.0
    for tag in tags:
        if tag in category:
            sum += tags[tag] * category[tag]
    sum = sum / len(tags)
    return sum