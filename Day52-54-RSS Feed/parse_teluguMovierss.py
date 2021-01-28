
import feedparser

feed_file = "telugu_movie_review.xml"

feed = feedparser.parse(feed_file)
data=[]
for entry in feed.entries:
    print(f'{entry.title} published on {entry.published} url is {entry.link}' )
    data.append(entry.title)

print(data)