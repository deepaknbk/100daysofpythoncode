import csv
from collections import defaultdict, namedtuple
import pprint

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS =10
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors=defaultdict(list)
    with open(MOVIE_DATA,encoding="utf-8") as csvfile:
        moviefile=csv.DictReader(csvfile)
        for row in moviefile:
            director=row['director_name']
            title_movie=row['movie_title']
            title_year=row['title_year']
            title_score=row['imdb_score']
            m=Movie(title=title_movie,year=title_year,score=title_score)
            directors[director].append(m)
    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    nominated_directors = {}
    i=0
    for director, movies in directors.items():
        if len(movies) > MIN_MOVIES:
            #avg_score=10
            #pprint(director,movies)
            nominated_directors[(director, _calc_mean(movies))] = movies
    return nominated_directors



def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    avg_score=0
    #print('start')
    for row in movies:
        avg_score +=float(row.score)
    #print(avg_score/len(movies))
    return round(avg_score / len(movies),1)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60
    report = sorted(directors.items(), key=lambda x: float(x[0][1]), reverse=True)
    for i in range(NUM_TOP_DIRECTORS):
        print(fmt_director_entry.format(counter=i + 1, director=report[i][0][0], avg=report[i][0][1]))
        print(sep_line)
        for movie in report[i][1]:
            #print(movie)
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print()


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    pp = pprint.PrettyPrinter()
    directors = get_movies_by_director()
    directors = get_average_scores(directors)
    #pp.pprint(directors)
    print_results(directors)


if __name__ == '__main__':
    main()