import json
import re
import requests


TVMAZE_URL = 'http://api.tvmaze.com/'
SHOW_SEARCH = 'search/shows?q={}'
EPISODE_LIST = 'shows/{}/episodes'
SPECIALS_QUERYSTRING = '?specials=1'


def search_shows(query):
    """Takes a search string and returns the results in a 
    list of dictionaries with name and show_id.
    Returns None if the search results are empty.
    """
    try:
        response = requests.get(TVMAZE_URL + SHOW_SEARCH.format(query))
        results_json = response.json()
        if len(results_json) > 0:
            results = []
            for show in results_json:
                results.append({
                    'name': show['show']['name'],
                    'show_id': show['show']['id']
                })
            return results
        else:
            return None
    except Exception as e:
        print('Something went wrong retrieving the data.\nError: {}'.format(e))


def episodes_list(show_id, specials=False):
    """Takes a show id and a boolean whether to include specials
    and returns a complete list of episodes from that show with
    episode name, season number, episode number, and description
    """
    request_url = TVMAZE_URL + EPISODE_LIST.format(show_id)
    if specials:
        request_url += SPECIALS_QUERYSTRING 
    try:
        response = requests.get(TVMAZE_URL + EPISODE_LIST.format(show_id))
        results_json = response.json()
        results = []
        for episode in results_json:
            description = re.sub(r"\</?p\>", "", episode['summary'])
            results.append({
                'name': episode['name'],
                'season': episode['season'],
                'number': episode['number'],
                'description': description
            })
        return results
    except Exception as e:
        print('Something went wrong retrieving the data\nError: {}'.format(e))