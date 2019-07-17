import re
import sys
import requests
from bs4 import BeautifulSoup as bs
headers = {
    'User-Agent':'Chrome/66.0.3359.181'
}
def spider(max_pages):
    link_lists = []
    content_lists = []
    page = 1
    ## sys.stdout = open ('boolean.txt','w')
    while page < max_pages:
        url = 'https://booolean.tistory.com/' + str(page)
        #print(url)
        response = requests.get(url, headers=headers).text
        #print(response)
        soup = bs(response, 'html.parser')
        #print(soup)
        page += 1
        links = soup.select('h2 span.subj a')
        ##print(len(links))
        for link in links:
            link_list = []
            href = 'https://booolean.tistory.com' + link.get('href')
            title = link.string
            ## print(href)
            link_list.append(href)
            ## print(title)
            link_list.append(title)
            ## print(link_list)
        link_lists.append(link_list)
        contents = soup.select('#entry > div.article')
        for content in contents:
            content_lists.append(content.text)

    for i in range(0, len(link_lists)):
        print(link_lists[i])
        print(content_lists[i])
        


spider(100)

