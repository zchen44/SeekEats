import os

ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
TESTS = os.path.join(ROOT, 'tests')

def yelp_search(category, location = "Syracuse, NY"):
    """Looks through the test folder for pictures, gets the labels for each of those pictures, and then 
	   asks the user which category any unrecognized labels belong in. Results are written to a file.

            @parameter: category, the category to be used for filtering searches
                        location, a city to search for the tag in. Default is "Syracuse, NY"
            @return: A json file of the top 5 restaurants given the input tags
    """

    # Import list of tags
    with open(os.path.join(TESTS, 'yelp_tags.txt'), 'r') as fi:
        words = fi.read().splitlines()
        fi.close()