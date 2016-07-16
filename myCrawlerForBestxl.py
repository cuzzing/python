#!/usr/bin/env python
# encoding=utf-8

__author__='steady_animal'

import codecs
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://www.9kkz.com/'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html,'html.parser')
    movie_list_soup = soup.find('tbody', attrs={'class': 'tbody'})

    movie_name_list = []

    for movie_tr in movie_list_soup.find_all('tr'):
        detail = movie_tr.find('td', attrs={'style': 'text-align:left;'})
        if detail != None:
            detail2 = detail.find('a', attrs={'target': '_blank'})
            movie_name = detail2.getText()
            movie_url = detail2['href']
            movie_name_list.append(movie_name + '   ' + movie_url)

    # next_page = soup.find('div', attrs={'class': 'pages clear'}).find('a')
    # if next_page:
    #     return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list


def main():
    url = DOWNLOAD_URL

    with codecs.open('movies from bestxl', 'wb', encoding='utf-8') as fp:
        # while url:
        html = download_page(url)
        movies = parse_html(html)
        fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()