import re
import math
import sys
import requests
from bs4 import BeautifulSoup as bs
import computer
headers = {
    'referer': 'https://www.google.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64;'\
        ' x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}
def spider(max_pages, key_word, lSpider_links, lSpider_titles):
    url1 = 'https://www.google.com/search?q='
    word = key_word
    url2 = '&newwindow=1&rlz=1C1CHBD_koKR845KR845&ei=KxMvXd7lArCVr7wPqP-6OA&start='
    url3 = '&sa=N&ved=0ahUKEwiep-7x-LvjAhWwyosBHai_DgcQ8tMDCNYB&biw=1820&bih=956'
    urls = []
    for num in range(0, max_pages):
        urls.append(url1 + word + url2 + str(num*10) + url3)
    page = 3
    ## spider_links = []
    ## spider_titles = []
    ## spider_contents = []
    while page < len(urls):
        url = urls[page]
        print(url)
        response = requests.get(url, headers=headers).text
        ##print(response)
        soup = bs(response, 'html.parser')
        ## print(soup)
        page += 1
        links = soup.select('#rso > div > div > div > div > div.rc > div.r > a')
        ##print(len(links))
        for link in links:
            href = link.get('href')
            titles = link.select('h3')
            link_titles = []
            for title in titles:
                link_titles.append(title.text)
            print(href)
            lSpider_links.append(href)
            print(link_titles)
            lSpider_titles.append(link_titles)
    return(lSpider_links, lSpider_titles)

def spider_contents(lSpider_links, lSpider_contents):
    page = 0

    for url in lSpider_links:
        response = requests.get(url, headers=headers).text
        soup = bs(response, 'html.parser')
        result = soup.select()

website = {
    'bbc': 'www.bbc.com',
    'businesspost':'www.businesspost.co.kr',
    'chosun':'www.chosum.com',
    'esquirekorea':'esquirekorea.co.kr'
    'hani':'www.hani.co.kr',
    'hanjyung':'www.hankyung.com',
    'instagram':'www.instagram.com',
    'korea':'www.korea.kr',
    'koreasummit':'koreasummit.kr',
    'mafra':'www.mafra.go.kr',
    'mk':'www.mk.co.kr',
    'monthly.chosun':'monthly.chosun.com',
    'msn':'www.msn.com',
    'news.naver':'news.naver.com',
    'naver':'www.naver.com',
    'newsnjoy':'www.newsnjoy.or.kr',
    'newstof':'newstof.com',
    'nocutnews':'www.nocutnews.com',
    'todayboda':'todayboda.net',
    'twitter':'twitter.com',
    'joins':'www.joins.com',
    'facebook':'www.facebook.com',
    'wspaper':'wspaper.org',
    'yes24':'www.yes24.com',
    'yna':'www.yna.co.kr',
    'ytn':'www.ytn.co.kr',
}
spider_links = []
spider_titles = []
spider_contents = []
spider(4, '문재인', spider_links, spider_titles)
## sys.stdout = open('google.txt', 'w', -1, 'utf-8')
## print(spider_links)
computer.mac()
