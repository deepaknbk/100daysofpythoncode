
import requests



if __name__=='__main__':
    url = 'https://telugu.filmibeat.com/rss/filmibeat-telugu-box-office-fb.xml'

    response = requests.get(url)

    with open('telugu_movie_review.xml','wb') as f:
        f.write(response.content)
