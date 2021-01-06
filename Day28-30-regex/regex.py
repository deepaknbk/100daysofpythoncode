import re

# COURSE = ('Introduction 1 Lecture 01:47'
#           'The Basics 4 Lectures 32:03'
#           'Getting Technical!  4 Lectures 41:51'
#           'Challenge 2 Lectures 27:48'
#           'Afterword 1 Lecture 05:02')
COURSE = ('00:40 Lesson introduction'
              '01:33 Your 3 day overview'
              '08:12 Learning datetime and date'
              '06:07 Datetime timedelta usage'
              '04:02 Concepts: what did we learn')
TWEET = ('PyBites My Reading List | 12 Rules for Life - #books '
             'that expand the mind! '
             'http://pbreadinglist.herokuapp.com/books/'
             'TvEqDAAAQBAJ#.XVOriU5z2tA.twitter'
             ' #psychology #philosophy')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    return re.findall(r'(\d+:\d+)',course)


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    return re.findall(r'((?:#|http)\S+)',tweet)


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    m=re.search(r'(<p>.*?</p>)',html)

    return re.sub('<[^<]+?>','',m.group())

print(extract_course_times(COURSE))
print(get_all_hashtags_and_links(TWEET))
print(match_first_paragraph(HTML))