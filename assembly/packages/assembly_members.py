## 정규식 패키지
import re
## 웹 페이지 요청 패키지
import requests
## 웹 페이지 번역 패키지
from bs4 import BeautifulSoup as bs

url = ''
response = requests.get(url).text
soup = bs(response, 'html.parser')
results = soup.select('')
for result in results:
    