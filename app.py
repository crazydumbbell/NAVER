import requests
from bs4 import BeautifulSoup


종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']


def 현재가(구멍) :
    데이터 = requests.get(f'https://finance.naver.com/item/sise.naver?code={구멍}')
    soup = BeautifulSoup(데이터.content, 'html.parser')
    print(soup.find_all('strong', id = '_nowVal')[0].text)
    print(soup.find_all('span', class_ = 'tah')[5].text) 
    return soup.find_all('strong', id = '_nowVal')[0].text


f = open ( 'a.text','w')

for i in 종목들 :
    f.write(현재가(i) + "\n")

f.close()