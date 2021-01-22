import bs4

def scrape():

    with open('videocourse.txt','r',encoding='utf-8') as f:
        content = f.read()

    soup=bs4.BeautifulSoup(content,'html.parser')
    print(soup.prettify())
    print('\n')
    print(soup.select('.card-deck'))



if __name__ == '__main__':
    scrape()
