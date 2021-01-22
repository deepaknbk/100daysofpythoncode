import requests
import bs4

url="https://pybit.es/pages/projects.html"
def site_ping():
    raw_site=requests.get(url)
    raw_site.raise_for_status()
    return raw_site

def scrape_site(site):
    podcast_list=[]

    soup=bs4.BeautifulSoup(site.text,'html.parser')
    #print(soup.body.header.nav.gettext())
    podcast_headers=soup.select('.projectHeader')

    for podcast in podcast_headers:
        podcast_list.append(podcast.getText())
        print(podcast.getText())

    print(podcast_list)

if __name__=='__main__':
    site=site_ping()
    scrape_site(site)