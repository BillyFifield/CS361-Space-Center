import wikipedia
import sys
import os

def wiki_search(object):
    """A Wikipedia scraper to get space craft information for The Space Center application.
    This file can be used for any information pulled from Wikipedia (not just for the Space center).
    The wiki_search function will take a string of an object to search on Wikipedia and return the summary
    of the object as well a list of picture of the object.
    """
    result = wikipedia.search(object)[0]

    summary = wikipedia.page(result).summary
    images = wikipedia.page(result).images

    data = {
            'description': summary,
            'images': images
           }
    
    return data


if __name__ == '__main__':
    try:
        wiki_search()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
