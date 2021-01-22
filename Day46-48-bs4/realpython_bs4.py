import requests
import bs4

url="https://realpython.com/courses/"
def site_ping():
    raw_site=requests.get(url)
    raw_site.raise_for_status()
    return raw_site

def write_file(site):
    with open('videocourse.txt','w',encoding='utf-8') as a:
        a.write(site.text)

def scrape_site(site):
    podcast_list=[]

    soup=bs4.BeautifulSoup(site.text,'html.parser')
    print(soup.select('.card-deck'))
    print(soup.body.div.div.div.div.h2.a)

if __name__=='__main__':
    site=site_ping()
    write_file(site)
    scrape_site(site)
