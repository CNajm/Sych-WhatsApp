import requests
import json
"""
Searches wikipedia and returns dictionary of data

The opensearch api request is detailed as such:
https://en.wikipedia.org/w/api.php
?action=opensearch
&search=zyz          search query
&limit=1             return only the first result
&namespace=0         search only articles, ignoring Talk, Mediawiki, etc.
&profile=fuzzy       search profile to use, it defaults to fuzzy which supports typo correction.
&redirects=resolve   follow redirects and resolve them
"""
def SearchWiki(query):
    endpoint = "https://en.wikipedia.org/w/api.php?action=opensearch&search={}&limit=1&namespace=0&redirects=resolve"
    search = requests.get(endpoint.format(query.replace(" ", "%20")))
    search.raise_for_status()
    try:
        data = json.loads(search.text)
    except:
        print("invalid data")
        return False
    try:
        return {
        "inputquery"  :    data[0],
        "title"       :    data[1][0],
        "content"     :    data[2][0],
        "url"         :    data[3][0]
        }
    except IndexError:
        return False
