#! /usr/bin/python3
#coding: utf-8

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) \
AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

all_url = 'http://www.hxs6.xyz'
#all_url = 'https://www.baidu.com'

start_url = requests.get(all_url, headers=headers)

Soup = BeautifulSoup(start_url.text, 'lxml')
print(Soup.decode('utf-8'))
