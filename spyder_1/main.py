#! /usr/bin/python3
#!coding: utf-8

from bs4 import BeautifulSoup
import urllib.request

#headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) \
#AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

all_url = 'http://www.hxs6.xyz'
#all_url = 'https://www.baidu.com'
#all_url = 'https://www.bilibili.com/'

start_url = urllib.request.urlopen(all_url)

Soup = BeautifulSoup(start_url, 'lxml')
name_list  = Soup.find('div', class_ = 'list' ).find_all('li')

for name in name_list:
    print(name)
   # print(name.find('div', class_ = 'T1').find_all('a')[3].get_text())
