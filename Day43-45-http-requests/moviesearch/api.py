import requests

def find_movie_by_title(keyword):

    url=f'http://movie_service.talkpython.fm/api/search/{keyword}'
    resp=requests.get(url)
    resp.raise_for_status()
    results=resp.json()
    #print(results)
    return results.get('hits')
