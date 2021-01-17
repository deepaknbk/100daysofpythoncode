import api

def main():
    print('In Main')
    title=input('Entry the keyword to search:')
    movies=api.find_movie_by_title(title)
    #print(movies.get('hits'))
    for movie in moviesjob:
         print(f"{movie.get('title')} with code {movie.get('imdb_code')} has score {movie.get('imdb_score')}")
    pass

if __name__=='__main__':
    main()
